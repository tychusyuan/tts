from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

with open("text.txt","r") as f:
    text=f.read()
    tts=gTTS(text,lang="en",slow=False)

    tts.save("multimedia/hello.mp3")
    song=AudioSegment.from_mp3("multimedia/hello.mp3")
    play(song)