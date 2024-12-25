import assemblyai as aai

aai.settings.api_key = "api key"

FILE_URL = "./test.mp3"


transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)

srt = transcript.export_subtitles_srt(chars_per_caption=32)

with open("subtitle_example.srt", "w") as f:
    f.write(srt)