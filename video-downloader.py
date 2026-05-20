"""
command line tool

input: youtube video link from command line
    ./video-downloader.py <link>
output: downloaded video

Utilizes the pytubefix library
https://github.com/JuanBindez/pytubefix

"""
import sys
from pytubefix import YouTube

from pytubefix.cli import on_progress


def main():
    if len(sys.argv) != 2:
        print("Usage: ./video-downloader.py <link>")
        sys.exit()
    
    url = sys.argv[1]
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()


if __name__=="__main__":
    main()

    

