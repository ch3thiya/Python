from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = ""
SCOPE = "playlist-modify-private playlist-modify-public"


date = input("Which date do you want to travel to? YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
mainpage = response.text
soup = BeautifulSoup(mainpage, "html.parser")
titles = soup.select("li ul li h3")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI, scope=SCOPE,
                                               show_dialog=True, cache_path="token.txt"))
user_id = sp.current_user()["id"]

year = date.split("-")[0]
song_list = []

for title in titles:
    song = ((title.getText()).strip())
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_list.append(uri)
    except IndexError:
        print(f"Song '{song}' not found on Spotify. Skipped.")

print(song_list)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=True, collaborative=False,
                                   description="Made this playlist as a part of a project.")

play_id = playlist["id"]

sp.playlist_add_items(playlist_id=play_id, items=song_list, position=None)

print("Playlist Created!")
