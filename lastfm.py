#!/usr/bin/env python
import pylast

from subprocess import Popen

API_KEY = "40887e583290b0d8932e3c872ac7aae5"
API_SECRET = "6605f506e40adf0ad7eb29da94fafa42"

username = "Vintendo"
password_hash = "c9c952008479e67d04709809ac61fc57"

def getTrack():
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET,
                            username = username, password_hash = password_hash)

    user = network.get_authenticated_user()
    track = user.get_now_playing()

    if not track:
        track = user.get_recent_tracks(limit = 1)[0]

    return track;


if __name__ == '__main__':
    track = getTrack()
    
    question = "Do you want to love %s?" % track

    proc = Popen("zenity --question --text='%s'" % question, shell=True)
    proc.communicate()
    if proc.returncode is 0:
        track.love()
