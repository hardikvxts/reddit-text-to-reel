import random

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.fx.resize import resize

generator = lambda txt: TextClip(txt, font='Berlin-Sans-FB-Demi-Bold', fontsize=90 , size = (700 , None) , color='white' , stroke_width=3.5 , stroke_color='black' , method = 'caption')
audio = AudioFileClip('./voicenotes/voice_i stole fr.mp3')
duration = audio.duration

subtitles = SubtitlesClip('./subtitles/subtitle_i stole fr.srt', generator)
clip = VideoFileClip('./background/1.mp4')
start = random.randint(0 , 900)
clip = clip.subclip(start , start + duration)
clip = clip.resize(height=1920)
clip = clip.crop(x_center=1706, y_center=960, width=1080, height=1920)
print(duration)
clip.audio = CompositeAudioClip([audio])

result = CompositeVideoClip([clip, subtitles.set_position(("center" , "center"))])

result.write_videofile("subtitlecheck.mp4")