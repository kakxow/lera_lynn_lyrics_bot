import re
import random

import bs4
import requests

from constants import lyrics_params, twitter_message_limit, lyrics_api


def _get_all_tracks_urls(artist: str) -> list[str]:
    url_search = f"{lyrics_api}track.search"
    all_tracks_urls = []
    page = 1
    params = lyrics_params | {"q_artist": artist, "page_size": 100, "page": page}
    while 1:
        response = requests.get(url_search, params=params)
        response.raise_for_status()
        response_data = response.json()
        try:
            track_list = response_data["message"]["body"]["track_list"]
        except TypeError:
            breakpoint()
        if not track_list:
            break
        for track in track_list:
            track_url = track["track"]["track_share_url"]
            if "?" in track_url:
                track_url, _ = track_url.split("?")
            all_tracks_urls.append(track_url)
        page += 1
        params.update({"page": page})
    return all_tracks_urls


def _get_lyrics_from_url(url: str) -> str | None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
    }
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    a = soup.findAll("span", attrs={"class": re.compile("lyrics__content__.*")})
    if not a:
        return None
    return a[-1].text  # type: ignore


def split_to_verses(text: str) -> list[str]:
    """makes verses longer than one line"""
    verses: list[str] = []
    verse = []
    for line in text.split("\n"):
        line = line.strip()
        if line:
            verse.append(line)
        elif len(verse) > 1:
            verses.append("\n".join(verse))
    else:
        verses.append("\n".join(verse))
    return verses


def _get_quote(text: str) -> str | None:
    prepared_verses = split_to_verses(text)
    verses = [q for q in prepared_verses if len(q) < twitter_message_limit]
    if not verses:
        quote = _get_random_lines("\n".join(prepared_verses), 4)
    else:
        quote = random.choice(verses)
    return quote


def _get_random_lines(text: str, number_of_lines: int) -> str | None:
    """
    gets random subsequent lines from the text as a quote
    if quote is longer than twitter limit, another random number is drawn
    until eligible quote is found or ammount of tries exceeds total lines in a text
    after that number of lines is lowered by 1 and the process repeats
    """
    if number_of_lines == 0:
        return None
    counter = 0
    lines = text.split("\n")
    last_eligible_line_number = len(lines) - number_of_lines
    while 1:
        first_line = random.randint(0, last_eligible_line_number)
        quote = "\n".join(lines[first_line : first_line + number_of_lines])
        if len(quote) < twitter_message_limit:
            break
        counter += 1
        if counter >= len(lines):
            return _get_random_lines(text, number_of_lines - 1)

    return quote


def get_random_quote(artist: str) -> str | None:
    tracks_urls = _get_all_tracks_urls(artist)
    url = random.choice(tracks_urls)
    text = _get_lyrics_from_url(url)
    print("random quote from here", url)
    if text:
        quote = _get_quote(text)
        if quote:
            return quote
    return None


def get_random_quote_sure(artist: str) -> str:
    tracks_urls = _get_all_tracks_urls(artist)
    while 1:
        url = random.choice(tracks_urls)
        text = _get_lyrics_from_url(url)
        if text:
            quote = _get_quote(text)
            if quote:
                return quote
            else:
                print("failed to find quote", url)
        print("failed to find text", url)


