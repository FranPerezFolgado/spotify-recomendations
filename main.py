import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_top_artists(limit=20)
print(json.dumps(results, indent=4))