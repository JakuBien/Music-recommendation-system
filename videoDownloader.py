from __future__ import unicode_literals
import yt_dlp
import ffmpeg
import sys

class VideoDownloader():
    def __init__(self):
        self.ydl_opts = {
            'outtmpl': 'youtube_wav_files/youtube_video',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
        }
        self.ydl = yt_dlp.YoutubeDL(self.ydl_opts)

    def download_from_url(self, url):
        self.ydl.download([url])
        stream = ffmpeg.input('output.m4a')
        stream = ffmpeg.output(stream, 'output.wav')

    def convert(self, url):
        args = sys.argv[1:]
        if len(args) > 1:
            print("Too many arguments.")
            print("Usage: python youtubetowav.py <optional link>")
            print("If a link is given, it will automatically convert it to .wav. Otherwise, a prompt will be shown.")
            return

        if len(args) == 0:
            self.download_from_url(url)
        else:
            self.download_from_url(args[0])
