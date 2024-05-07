import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import random
from genres import GENRES

SCOPE = 'user-top-read'



def create_connection():
    
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))


def get_current_top_artist(sp):
    return sp.current_user_top_artists(limit=10)

def obtain_genres(data):
    genres = [genre for artist in data['items'] for genre in artist['genres']]
    return [genre for words in genres for genre in words.split()]

def find_tracks(sp: spotipy.Spotify,genres):
    random_genres = random.sample(genres, 15)
    uris = []
    for genre in random_genres:
        query = f'genre:{genre}'
        songs = sp.search(limit=1, q=query, type='track')
        uri = [item['uri'] for item in songs['tracks']['items']]
        uris.append(uri)
    return uris


    
        
# get random genres
# find 10 songs per genre
# acummulate uris in list
# create playlist
#add songs using uris

def main():
    sp = create_connection()
    top_artists = get_current_top_artist(sp)
    listened_genres = obtain_genres(top_artists)
    not_listened_genres = [genre for genre in GENRES if genre not in listened_genres]
    uris = find_tracks(sp, not_listened_genres)
    print(uris)
    


if __name__ == "__main__":
    main()