import requests

genius_api = "https://api.genius.com/"

response = requests.get("https://genius.com/Mitski-heat-lightning-lyrics")
print(response)
open("genius_try.html", "w", encoding="utf-8").write(response.text)
