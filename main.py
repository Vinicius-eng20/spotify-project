from tracks import Tracks
from decouple import config

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

playlist = Tracks(CLIENT_ID, CLIENT_SECRET)

tracks_by_artist = playlist.get_songs_for_artist("Bon Jovi")
playlist.display_top_tracks_for_artist(tracks_by_artist)







