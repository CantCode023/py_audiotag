import requests
from dataclasses import dataclass

@dataclass
class Track:
    track: str
    artist: str
    album: str
    year: int
    yt_link: str
    preview: str
    album_image: str

    def __post_init__(self):
        self.preview = "https://audiotag.info"+self.preview if self.preview != "" else ""
        self.album_image = "https://audiotag.info/covers/"+self.album_image if self.album_image != "" else ""

class AudioTag:
    def __init__(self, phpsessid):
        self._phpsessid = phpsessid

    def recognize(self, path_to_song:str):
        cookies = {
            'PHPSESSID': self._phpsessid,
        }
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            'Content-Type': 'audio/mpeg',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
            'FileName': 'song.mp3',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Origin': 'https://audiotag.info',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://audiotag.info/',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        data = open(path_to_song, 'rb')
        print("[!] Uploading song.")
        response = requests.post('https://audiotag.info/direct/', cookies=cookies, headers=headers, data=data)
        print("[!] Song uploaded.")
        if response.status_code != 200:
            raise Exception(response.status_code)
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://audiotag.info/',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get('https://audiotag.info/check', cookies=cookies, headers=headers)
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://audiotag.info',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://audiotag.info/result',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        data = {
            'check': 'true',
            'get': '',
        }
        print("[!] Recognizing.")
        response = requests.post('https://audiotag.info/result', cookies=cookies, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception(response.status_code)
        results = response.json()["session_result"]
        tracks = []
        for result in results:
            track = result[3][0]
            new_track = Track(track=track[0], artist=track[1], album=track[2], year=track[3], yt_link=track[4], preview=track[6], album_image=result[-1])
            tracks.append(new_track)
        return tracks