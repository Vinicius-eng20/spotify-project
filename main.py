from tracks import Tracks
from decouple import config

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

playlist = Tracks(CLIENT_ID, CLIENT_SECRET)

tracks_by_country = playlist.get_top_tracks_by_country('BR', 10)
playlist.display_top_tracks(tracks_by_country)







