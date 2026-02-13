import os
import yt_dlp
from pydub import AudioSegment


def create_mashup(singer, num_videos, duration):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    if not os.path.exists("output"):
        os.makedirs("output")

    # clear downloads
    for file in os.listdir("downloads"):
        os.remove(os.path.join("downloads", file))

    search_query = f"ytsearch{num_videos}:{singer} songs"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

    merged = AudioSegment.empty()

    for file in os.listdir("downloads"):
        path = os.path.join("downloads", file)
        audio = AudioSegment.from_file(path)
        trimmed = audio[:duration * 1000]
        merged += trimmed

    output_path = os.path.join("output", "mashup.mp3")
    merged.export(output_path, format="mp3")

    return output_path
