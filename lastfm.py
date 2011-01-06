#!/usr/bin/env python
import pylast

API_KEY = "40887e583290b0d8932e3c872ac7aae5"
API_SECRET = "6605f506e40adf0ad7eb29da94fafa42"

username = "Vintendo"
password_hash = "c9c952008479e67d04709809ac61fc57"

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET,
                        username = username, password_hash = password_hash)

user = network.get_authenticated_user()
track = user.get_now_playing()

if not track:
    track = user.get_recent_tracks(limit = 1)[0]

answer = raw_input("Do you want to love %s? (Y/n) " % track)

if answer is 'y' or not answer:
    track.love()
