from gtts import gTTS

text = "Hello, this is a test message! , how are you doing today my lord my saviour lebron james"

tts = gTTS(text=text, lang='en-us' , tld = 'com')

tts.save("outputUS.mp3")

print("MP3 file has been saved as output.mp3")