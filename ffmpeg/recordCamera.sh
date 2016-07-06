vlc -vvv v4l2:///dev/video1:chroma=mjpg:width=1920:height=1080:fps=30 :input-slave=alsa://hw:2,0 --sout="#duplicate{dst=std{access=file,fps=30,mux=avi,dst=./test.avi},dst=display}"
#http://anders.tonfeldt.se/view_record_webcam_vlc.html
