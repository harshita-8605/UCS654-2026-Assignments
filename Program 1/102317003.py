import sys
import os
import yt_dlp
from pydub import AudioSegment


# checking command line arguments
if len(sys.argv) != 5:
    print("Usage: python file.py <SingerName> <NumberOfVideos> <Duration> <OutputFile>")
    sys.exit()

singer = sys.argv[1]

try:
    num_videos = int(sys.argv[2])
    duration = int(sys.argv[3])
except:
    print("Number of videos and duration must be integers.")
    sys.exit()

output_file = sys.argv[4]

if num_videos <= 10:
    print("Number of videos must be greater than 10.")
    sys.exit()

if duration <= 20:
    print("Duration must be greater than 20 seconds.")
    sys.exit()


# create folders if not present
if not os.path.exists("downloads"):
    os.makedirs("downloads")

if not os.path.exists("output"):
    os.makedirs("output")


# clear old files
for file in os.listdir("downloads"):
    os.remove(os.path.join("downloads", file))


print("Downloading songs...")

search_query = f"ytsearch{num_videos}:{singer} songs"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'quiet': True
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])
except:
    print("Error while downloading videos.")
    sys.exit()


print("Creating mashup...")

merged_audio = AudioSegment.empty()

for file in os.listdir("downloads"):
    path = os.path.join("downloads", file)
    try:
        audio = AudioSegment.from_file(path)
        trimmed = audio[:duration * 1000]  
        merged_audio += trimmed
    except:
        print("Skipping file:", file)


try:
    merged_audio.export(os.path.join("output", output_file), format="mp3")
    print("Mashup created successfully!")
except:
    print("Error while exporting final file.")
