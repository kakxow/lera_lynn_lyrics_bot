import requests

from constants import url_post_tweet, twitter_headers


def send_tweet(text: str) -> tuple[str, str]:
    r = requests.post(url_post_tweet, json=text, headers=twitter_headers)
    response_data = r.json()
    return response_data["data"]["id"], response_data["data"]["text"]
