from ifttt import send_tweet
from lyrics_local import get_random_quote

artist = "Lera Lynn"
quote = get_random_quote(artist)
if quote:
    send_tweet(quote)
