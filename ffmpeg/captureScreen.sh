#Capture your screen

 avconv  -f x11grab -r 25 -s 1920x1080 -i :0.0 -vcodec libx264 -threads 4 $HOME/output.avi
