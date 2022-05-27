import os
import random

from lyrics import _get_quote


def get_random_quote(lyrics_folder_path: str) -> str:
    all_files = os.listdir(lyrics_folder_path)
    file = random.choice(all_files)
    full_name = os.path.join(lyrics_folder_path, file)
    with open(full_name, encoding="utf-8") as f:
        text = f.read()
    quote = _get_quote(text)
    return quote
