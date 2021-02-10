#!/usr/bin/env python3

import os
import mido
import random

mid = mido.MidiFile()
max_note = 127

def add_track(note):
    track = mido.MidiTrack()
    track.append(mido.Message("program_change", program=38, time=0))
    
    for i in range(100):
        track.append(mido.Message("note_on", note=note, time=100))
        note = (note + 2) % max_note
        #track.append(mido.Message("note_off" , note=note, time=150))

    return track

voices = 2
n = 30
for track in range(voices):
    mid.tracks.append(add_track(n))
    n += 4

mid.save("okay.mid")
