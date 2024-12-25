from moviepy.editor import *
from moviepy.video.VideoClip import ImageClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.fx.resize import resize
from moviepy.video.tools.subtitles import SubtitlesClip
import assemblyai as aai
import random

def saveVideo(submission, bgcount, name):
    aai.settings.api_key = "api key"

    #audio initialized
    audio = AudioFileClip("./voicenotes/voice_{s}.mp3".format(s=submission.title[0:10]))

    #assemblyAI caption
    FILE_URL = "./voicenotes/voice_{s}.mp3".format(s=submission.title[0:10])
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)
    if transcript.status == aai.TranscriptStatus.error:
        print(transcript.error)
    else:
        print(transcript.text)
    srt = transcript.export_subtitles_srt(chars_per_caption=32)

    #write subtitles to foler subtitle
    with open("./subtitles/subtitle_{s}.srt".format(s=submission.title[0:10]), "w") as f:
        f.write(srt)

    #initialised text settings
    generator = lambda txt: TextClip(txt, font='Berlin-Sans-FB-Demi-Bold', fontsize=90, size=(700, None), color='white',
                                     stroke_width=3.5, stroke_color='black', method='caption')
    duration = audio.duration
    nums = random.randint(1, bgcount)

    #initialize subtitle
    subtitles = SubtitlesClip('./subtitle_example.srt', generator)

    #initialize video
    start = random.randint(0, 900)
    video = VideoFileClip("./background/{s}.mp4".format(s=nums)).subclip(start, start + duration)

    #change ratio to 9:16
    video = video.resize(height=1920)
    video = video.crop(x_center=1706, y_center=960, width=1080, height=1920)

    #image adding to video
    redditauthor = ImageClip("./screenshots/author_{s}.png".format(s=submission.title[0:10])).set_duration(5).set_pos("top", "center").margin(top=400, opacity=0)
    reddittitle = ImageClip("./screenshots/title_{s}.png".format(s=submission.title[0:10])).set_duration(5).set_pos("top", "center").margin(top=450, opacity=0)
    image1 = redditauthor.resize(1.5)
    image2 = reddittitle.resize(1.5)

    #add audio to video with image
    video.audio = CompositeAudioClip([audio])
    final = CompositeVideoClip([video, image1, image2])

    #add sub to video with image and audio
    final_withsub = CompositeVideoClip([final, subtitles.set_position(("center" , "center"))])
    final_withsub.write_videofile("./output/final_output_{s}.mp4".format(s=name))