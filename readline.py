from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os,random,time

readlist=[]
interval=6
with open("readline.txt","r") as f:
    idx=0
    for line in f.readlines():
        idx+=1
        name="multimedia/{idx}.mp3".format(idx=idx)
        tts=gTTS(line,lang="en",slow=False)
        tts.save(name)
        readlist.append(name)

random.shuffle(readlist)

for mp3 in readlist:
    song=AudioSegment.from_mp3(mp3)
    play(song)
    time.sleep(interval)
    play(song)
    time.sleep(interval)