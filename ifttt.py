import requests

from constants import ifttt_api_url


def send_tweet(text: str):
    params = {"value1": text}
    response = requests.post(ifttt_api_url, params=params)
    return response


send_tweet("Hello world!")
