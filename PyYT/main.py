#YOUTUBE VIDEO DONLOADER
# pip install pytube
import pytube

# Get Yt Link
link = input('Enter Youtube Video Link :')

# Create YTlink Instance
yt = pytube.YouTube(link)

# Download Video
yt.streams.first().download()

# Finished download
print('Download Finished', link)
