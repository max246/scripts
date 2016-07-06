## This script takes all the images from the current folder and convert into an mp4 video

ffmpeg -y -framerate 7  -pattern_type glob -i '*.jpg' -c:v libx264 -r 30 -preset ultrafast out.mp4
