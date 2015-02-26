#!/bin/bash

cd /mnt/usb/camera

COUNTER=0
while [  $COUNTER -lt $1 ]; do
  DATE=$(date +"%Y-%m-%d_%H%M%S")
  sudo raspistill -hf -vf -q $2 -o /mnt/usb/camera/img-$DATE.jpg
  sleep $3
  let COUNTER=COUNTER+1 
done

DATE=$(date +"%Y-%m-%d_%H%M%S")
sudo ls /mnt/usb/camera/*.jpg > /home/pi/camera/stills.txt
sudo mv /home/pi/camera/stills.txt /mnt/usb/camera/stills-$DATE.txt

sudo mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o /mnt/usb/camera/timelapse-$DATE.avi -mf type=jpeg:fps=$4 mf://@stills-$DATE.txt

#sudo rm /mnt/usb/camera/*.jpg
#sudo rm /mnt/usb/camera/*.txt

#./pic.sh 48 50 6 26   
#sudo mount -t vfat /dev/sda1 /mnt/usb
