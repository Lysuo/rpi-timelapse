# rpi-timelapse
useful script to make timelapse videos with Rpi

# Installation
copy paste this line into the /etc/rc.local file : sudo mount -t vfat /dev/sda1 /mnt/usb
crontab line : 12 03 * * * sudo /root/timelapse.sh 50 100 7 26

# How to set up the arguments
first argument is the number of pictures to take
second one is the quality of the pictures from 1 to 100
third one : time between each shot minus 6 (it takes 6 to 7s to the rpi to take a pic, setting this argument to 7 will distance successive pictures by 13-14s)
last one is the fps parameter of the video file in output

# How to determine the arguments 1 and 3
say you want 30s of video with fps = 26, that makes 30*26 = 780 pics in total
now depending on the time you've got and the phenomenom you're watching you adjust these two arguments to match your criteria. 
setting $3 to 7s makes you wait 13*780 = 10140s to get all pictures

# Be careful with the quality of the pictures. 100 quality means 2.5Mb pictures, times 780 ... you'd better save some space on your usb stick!
