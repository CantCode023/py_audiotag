from py_audiotag import AudioTag

audiotag = AudioTag("YOUR_SESSION_ID_HERE")
tracks = audiotag.recognize("./song1.mp3")
print(tracks[0])