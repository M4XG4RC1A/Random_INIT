import os
import datetime
from pydub import AudioSegment
from pydub.playback import play

os.system('cleart')
print("Welcome to Reminder\nTell me your activities\n(/ = Finish)")
cond = True;
Activities = []
Time = []
Day = []
while cond:
    Name = input("Activity Name ('/'=End): ")
    if Name != "/":
        Activities.append(Name)
        hmTime = input("Time (hh:mm): ")
        Time.append(hmTime.split(":"))
        dmyTime = input("Day (dd,mm,yyyy) ")
        Day.append(dmyTime.split(","))
    else:
        cond = False
os.system('cleart')
print("Reminder Start")
cond = True
while cond:
    delete = False
    idDel = 0
    for i in range(len(Activities)):
        if(datetime.datetime.now().day == dmyTime[i][1] and
           datetime.datetime.now().month == dmyTime[i][2] and
           datetime.datetime.now().year == dmyTime[i][3] and
           datetime.datetime.now().hour == hmTime[i][1] and
           datetime.datetime.now().minute == hmTime[i][2]):
           print("Alarm")
           print(Activities[i])
           song = AudioSegment.from_wav("sound.wav")
           play(song)
           idDel = i
           delete = True
    if delete:
        del Activities[idDel]
        del dmyTime[idDel]
        del hmTime[idDel]
    if Activities == []:
        cond = False
print("Alarms End")
