import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import random
from genres import GENRES

SCOPE = 'user-top-read playlist-modify-public playlist-modify-private'



def create_connection():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))


def get_current_top_artist(sp):
    return sp.current_user_top_artists(limit=30)

def obtain_genres(data):
    genres = [genre for artist in data['items'] for genre in artist['genres']]
    return [genre for words in genres for genre in words.split()]

def find_tracks(sp: spotipy.Spotify,genres):
    random_genres = random.sample(genres, 15)
    uris = []
    for genre in random_genres:
        query = f'genre:{genre}'
        songs = sp.search(limit=5, q=query, type='track')
        uri = [item['uri'] for item in songs['tracks']['items']]
        uris.extend(uri)
    return uris


def create_playlist(sp: spotipy.Spotify):
    user_details = sp.me()
    user_name = sp.me()['display_name']
    playlist_name = f'Randomlist for {user_name}'
    playlist = sp.user_playlist_create(
        user=user_details['id'],
        name=playlist_name,
        public=True,
        collaborative=False,
        description='Playlist created by Franjelou'
    )
    return playlist

def add_songs_to_playlist(sp: spotipy.Spotify, uris, playlist):
    sp.playlist_add_items(
        items=uris,
        playlist_id=playlist['id'])

def generateRandomPlaylist():
    sp = create_connection()
    top_artists = get_current_top_artist(sp)
    listened_genres = obtain_genres(top_artists)
    not_listened_genres = [genre for genre in GENRES if genre not in listened_genres]
    uris = find_tracks(sp, not_listened_genres)
    playlist = create_playlist(sp)
    add_songs_to_playlist(sp, uris=uris, playlist=playlist)
    return playlist['external_urls']['spotify']
    


if __name__ == "__main__":
    print(main())
    