import json
import logging
import sys
import requests
from config import config

def fetch_playlist_items_page(google_api_key, playlist_id, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems", params={
        "key": google_api_key, 
        "playlistId": playlist_id, 
        "part": "contentDetails", 
        "pageToken": page_token, 

        })

    payload = json.loads(response.text)
    logging.debug("GOT %s", payload)
    return payload

def fetch_playlist_items(google_api_key, playlist_id, page_token=None):
    payload = fetch_playlist_items_page(google_api_key, playlist_id, page_token)

    yield from payload["items"]

    next_page_token = payload.get("nextPageToken")

    if next_page_token is not None:
        yield from fetch_playlist_items(google_api_key, playlist_id, next_page_token)

def main():
    logging.info("START")

    ### Make sure to have a config.py file in root with a dictionary that contains your api key and the playlist you want
    google_api_key = config["google_api_key"]
    playlist_id = config["youtube_playlist_id"]

    video_items = fetch_playlist_items(google_api_key, playlist_id)
    for item in video_items:
        logging.info("GOT %s", item)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())