import os, time, sys, datetime, subprocess

def getDate():
  mylist = []
  today = datetime.datetime.today()
  d = list(today.timetuple())

  for i,e in enumerate(d):
    if e in range(0, 10):
      d[i] = '0'+str(e)

  date = "-".join([str(e) for i,e in enumerate(d) if i<6])
  return date

def init(path):
  os.system("mkdir "+path)

def record(path, nbPic, quality, width, height, sleeptime):
  count=0
  sleeptimeR = sleeptime-1
  while count <= nbPic: 
    filename = path+"/img-"+getDate()+".jpg"
    cmd = 'raspistill -o ' + filename + ' -t 1000 -ex auto -awb off -ev 0 -w ' + width + ' -h ' + height
    pid = subprocess.call(cmd, shell=True)
    #os.system("raspistill -n -ex auto -awb off -w "+width+" -h "+height+" -t 1000 -ev 0 -q "+quality+" -o "+path+"/img-"+getDate()+".jpg")
    time.sleep(sleeptimeR) 
    count += 1

def prepareConversion(path, date):
  os.system("ls "+path+"/*.jpg > /root/stills.txt")
  os.system("mv /root/stills.txt "+path+"/stills-"+date+".txt")

def convert(path, date, fps, width, height):
  os.system("mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale="+width+":"+height+" -o "+path+"/timelapse-"+getDate()+".avi -mf type=jpeg:fps="+fps+" mf://@"+path+"/stills-"+date+".txt")

#./timelapse.sh 6 100 10 26   
#sudo mount -t vfat /dev/sda1 /mnt/usb

if __name__ == "__main__":

  arg = sys.argv

  if len(arg) < 5:
    print 'Wrong use, you need to provide the total number of picture, their quality (1 to 100), the time in seconds between each picture and fps for output video'
    print '\t example:'
    print '\t python timelapse.py 6 100 10 3'
  else:
    date = getDate()
    path='/mnt/usb/'+date
    #path='/root/timelapse/'+date
    #width = '1280'
    #height = '720'
    width = '2592'
    height = '1458'

    init(path)
    record(path, float(arg[1]), arg[2], width, height, float(arg[3]))
    prepareConversion(path, date)
    convert(path, date, arg[4], width, height)
