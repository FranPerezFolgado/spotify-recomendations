import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
from genres import GENRES

class Recommendation:

    def __init__(self):
        self.scope = 'user-top-read playlist-modify-public playlist-modify-private'

    def create_connection(self):
        return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))


    def get_current_top_artist(self,sp):
        return sp.current_user_top_artists(limit=30)

    def obtain_genres(self,data):
        genres = [genre for artist in data['items'] for genre in artist['genres']]
        return [genre for words in genres for genre in words.split()]

    def find_tracks(self, sp: spotipy.Spotify,genres):
        random_genres = random.sample(genres, 15)
        uris = []
        for genre in random_genres:
            query = f'genre:{genre}'
            songs = sp.search(limit=5, q=query, type='track')
            uri = [item['uri'] for item in songs['tracks']['items']]
            uris.extend(uri)
        return uris


    def create_playlist(self,sp: spotipy.Spotify):
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

    def add_songs_to_playlist(self,sp: spotipy.Spotify, uris, playlist):
        sp.playlist_add_items(
            items=uris,
            playlist_id=playlist['id'])

    def generate_random_playlist(self):
        sp = self.create_connection()
        top_artists = self.get_current_top_artist(sp)
        listened_genres = self.obtain_genres(top_artists)
        not_listened_genres = [genre for genre in GENRES if genre not in listened_genres]
        uris = self.find_tracks(sp, not_listened_genres)
        playlist = self.create_playlist(sp)
        print(playlist)
        self.add_songs_to_playlist(sp, uris=uris, playlist=playlist)
        return playlist['external_urls']['spotify']
        
