#!/usr/bin/env python
import pylast
import sys
from subprocess import Popen

API_KEY = "40887e583290b0d8932e3c872ac7aae5"
API_SECRET = "6605f506e40adf0ad7eb29da94fafa42"

username = sys.argv[1]
password_hash = pylast.md5(sys.argv[2])

def getTrack():
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET,
                            username = username, password_hash = password_hash)

    user = network.get_authenticated_user()
    track = user.get_now_playing()
    print track

    if not track:
        track = user.get_recent_tracks(limit = 1)[0].track

    return track;


if __name__ == '__main__':
    track = getTrack()
    print track
    
    question = "Do you want to love %s?" % str(track)

    proc = Popen("zenity --question --text='%s'" % question, shell=True)
    proc.communicate()
    if proc.returncode is 0:
        track.love()
