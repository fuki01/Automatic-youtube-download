import time
import datetime

with open('video.txt', 'r') as f:
    kw_list = f.read().split("\n")

from pytube import YouTube

time = time.time()
dateTime = datetime.datetime.fromtimestamp(time)

print(dateTime)

cntItem = 0

for item in kw_list:
  url = item
  nowDateTime = datetime.datetime.fromtimestamp(time)
  yt = YouTube(url)
  cntItem += 1
  print(str(cntItem)+"個目")
  print("ダウンロード中...")
  yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('./download/'+str(dateTime),str(nowDateTime))
  print("ダウンロード完")