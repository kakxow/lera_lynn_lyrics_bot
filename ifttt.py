import requests

from constants import ifttt_api_url


def send_tweet(text: str):
    params = {"value1": text}
    response = requests.post(ifttt_api_url, params=params)
    print(response, response.text)
    return response
