# Installation
```
git clone https://github.com/CantCode023/py_audiotag
```

# Getting Started
```py
from py_audiotag import AudioTag

audiotag = AudioTag("YOUR_SESSION_ID_HERE") # You can get this from audiotag cookies called "PHPSESSID"
tracks = audiotag.recognize("path_to_your_song.mp3")
print(tracks[0])
```

# How to find cookies
1. Open inspect element with `ctrl+shift+i`
2. Open "Application" tab
3. Open "Cookies" dropdown at the sidebar and click "https://audiotag.info"
4. Find PHPSESSID and copy the cookie.