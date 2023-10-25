from pytube import YouTube, Playlist
import os

#Download de Video-------------------------------------------------------------------------------

VIDEO_URL = 'https://www.youtube.com/watch?v=YRc5dp-hYnY&list=PL02zxenLLmrZ35b_BrLOu8WqaQ2ds0ije'
yt = YouTube(VIDEO_URL)

for stream in yt.streams:
    print(stream)


video = yt.streams.get_highest_resolution()
video.download("./midias1")

#Download de Playlist Video-------------------------------------------------------------------------
PLAYLIST_URL = 'https://www.youtube.com/watch?v=YRc5dp-hYnY&list=PL02zxenLLmrZ35b_BrLOu8WqaQ2ds0ije'

playlist = Playlist(PLAYLIST_URL)

for videos in playlist.videos:
    videos.streams.get_highest_resolution().download('./midias2')
