# from time import sleep
# import pyttsx3
#
# engine = pyttsx3.init()
#
# voices = engine.getProperty('voices')
# rate = engine.getProperty('rate')
#
# engine.setProperty('rate', rate - 70)
# engine.setProperty('age', 10)
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
#
#
# def saveMp3(submission):
#     engine.save_to_file('{a}\n{b}'.format(a=submission.title, b=submission.selftext),r'C:\Users\Akschansh Rai\Desktop\python praw practice\voicenotes\voice_{s}.mp3'.format(s=submission.title[0:10]))
#     engine.runAndWait()
#     sleep(5)

from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import which


def saveMp3(submission):
    AudioSegment.converter = which("ffmpeg")
    text = '{a}\n{b}'.format(a=submission.title, b=submission.selftext)
    tts = gTTS(text=text, lang='en-us', tld='com')
    tts.save('./voicenotes/voice_{s}_slow.mp3'.format(
        s=submission.title[0:10]))
    audio = AudioSegment.from_mp3('./voicenotes/voice_{s}_slow.mp3'.format(
        s=submission.title[0:10]))
    faster_audio = audio.speedup(playback_speed=1.2)
    faster_audio.export('./voicenotes/voice_{s}.mp3'.format(
        s=submission.title[0:10]), format="mp3")