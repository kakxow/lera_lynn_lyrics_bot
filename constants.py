import os

import dotenv

dotenv.load_dotenv()

lyrics_api = "http://api.musixmatch.com/ws/1.1/"
lyrics_token = os.environ["MUSIXMATCH_TOKEN"]
lyrics_params = {"apikey": lyrics_token}

ifttt_token = os.environ["IFTTT_TOKEN"]
event_name = "lera_lynn_quote"
ifttt_api_url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{ifttt_token}"
