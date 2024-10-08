import logging
import sys
import requests
from config import config

def main():
    logging.info("START")

    ### Make sure to have a config.py file in root with a dictionary that contains your api key and the playlist you want
    google_api_key = config["google_api_key"]
    playlist_id = config["youtube_playlist_id"]

    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems", 
                            params={"key": google_api_key, "playlistId": playlist_id, "part": "contentDetails", })

    logging.debug("GOT %s", response.text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())