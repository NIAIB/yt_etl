from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
print("dotenv_path:", dotenv_path)

load_dotenv(dotenv_path)  # load exactly what was found

print("YOUTUBE_API_KEY present?", bool(os.getenv("YOUTUBE_API_KEY")))
print("YOUTUBE_API_KEY value:", os.getenv("YOUTUBE_API_KEY"))






import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
        try:
            url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={YOUTUBE_API_KEY}"

            response = requests.get(url)
            response.raise_for_status()
    
            data = response.json()

        

            channel_items = data['items'][0]
            channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']
            #print(channel_playlistId)
            return channel_playlistId
        except requests.exceptions.RequestException as e:
            raise e
    
if __name__ == "__main__":
    get_playlist_id()