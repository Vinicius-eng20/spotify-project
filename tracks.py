import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class Tracks:
    def __init__(self, client_id, client_secret):
        self.id = client_id
        self.secret = client_secret

        client_credentials_manager = SpotifyClientCredentials(client_id=self.id, client_secret=self.secret)
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)    

    
    def get_playlist(self, playlist_id, limit):
        spotify = self.spotify

        tracks = spotify.playlist_tracks(playlist_id)['items'] # playlist cbjr
        sorted_tracks = sorted(tracks, key=lambda x: x['track']['popularity'], reverse=True)
        list_tracks = []

        for track in sorted_tracks[:limit]:
            track_info = track['track']
            list_tracks.append({
                'name': track_info['name'],
                'artists': [artist['name'] for artist in track_info['artists']],
                'popularity': track_info['popularity']
            })

        return list_tracks

    def get_popular_categories(self):
        spotify = self.spotify

        playlists = spotify.category_playlists('toplists')['playlists']['items']

        popular_categories = []

        for category in playlists:
            popular_categories.append({
                'id': category['id'],
                'name': category['name'], 
                'description': category['description']
            })
        return popular_categories

    def get_songs_for_artist(self, artist_name):
        spotify = self.spotify
        limit = 10

        results = spotify.search(q=f'artist:{artist_name}', type='artist', limit=1)

        if results['artists']['items']:
            artist_id = results['artists']['items'][0]['id']
            top_tracks = spotify.artist_top_tracks(artist_id)['tracks']
            sorted_tracks = sorted(top_tracks, key=lambda x: x['popularity'], reverse=True)

            list_tracks = []

            for track in sorted_tracks[:limit]:
                list_tracks.append({
                    'name': track['name'],
                    'popularity': track['popularity']
                })
            
            if top_tracks:
                return list_tracks
            else:
                print("Nenhuma música encontrada para o artista.")
                return []
                
        else:
            print(f"Artista {artist_name} não encontrado. ")
            return

    def get_top_tracks_by_country(self, country_code, limit):
        spotify = self.spotify

        playlists = spotify.search(q=f'top 50 {country_code}', type='playlist', limit=1)

        if playlists['playlists']['items']:
            playlist_id = playlists['playlists']['items'][0]['id']
            return self.get_playlist(playlist_id, limit)

        else:
            print(f"Playlist para o país '{country_code}' não encontrada.")
            return []

    def get_top_tracks_by_genre(self, genre, limit):
        spotify = self.spotify

        playlists = spotify.search(q=f'{genre} top', type='playlist', limit=1)

        if playlists['playlists']['items']:
            playlist_id = playlists['playlists']['items'][0]['id']
            return self.get_playlist(playlist_id, limit)

        else:
            print(f"Playlist para o gênero '{genre}' não encontrada.")
            return []    

# ---------------------------------------------------------------------------------
    ## ATENÇÃO: Essas funções serão retiradas posteriormente
    # Só precisamos das listas, isso aqui é só pra deixar bonitinho
    def display_top_tracks(self, list_tracks):
        if list_tracks:
            for i, track in enumerate(list_tracks, start=1):
                artists_str = ', '.join(track['artists'])
                print(f"{i}. {track['name']} - {artists_str} | Popularidade: {track['popularity']}")
        else:
            print('Not found. :(')

    def display_top_tracks_for_artist(self, list_tracks):
        if list_tracks:
            for i, track in enumerate(list_tracks, start=1):
                print(f"{i}. {track['name']} | Popularidade: {track['popularity']}")
        else:
            print('Not found. :(')

    def display_popular_categories(self, pop_categories):
        if pop_categories:
            print(f"\nTop {len(pop_categories)} Categorias Populares:")
            for i, category in enumerate(pop_categories, start=1):
                print(f"{i}. {category['name']} (ID: {category['id']}) | {category['description']}")
        else:
            print("Nenhuma categoria encontrada para o local.")
# ---------------------------------------------------------------------------------


        