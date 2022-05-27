import os

import dotenv

dotenv.load_dotenv()

twitter_message_limit = 280
twitter_api = "https://api.twitter.com/2/"
twitter_token = os.environ["TWITTER_TOKEN"]
url_post_tweet = f"{twitter_api}tweets"
twitter_headers = {"Authorization": f"Bearer {twitter_token}"}

lyrics_api = "http://api.musixmatch.com/ws/1.1/"
lyrics_token = os.environ["MUSIXMATCH_TOKEN"]
lyrics_params = {"apikey": lyrics_token}

ifttt_token = os.environ["IFTTT_TOKEN"]
event_name = "lera_lynn_quote"
ifttt_api_url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{ifttt_token}"
