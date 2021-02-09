#!/usr/bin/env python3

import os
import mido
import random

harpsichord=6

m_file = mido.MidiFile("variations.mid", clip=True)

print(m_file)
print(m_file.play())

#INFO

mid = mido.MidiFile()

live = ["note_on", "note_off"]

#Instruments 
synth_bass = [38, 39]
synth_pad = [i for i in range(88, 96)]

#All
all_instruments = synth_bass + synth_pad

min_note = 20
max_note = 60
max_program = 127

min_time = 2000
max_time = 3000

min_pause_time = 1000
max_pause_time = 5000

#Create drawn-out, streams of synth sound 

def random_track():
    track = mido.MidiTrack()
    track.append(mido.Message("program_change", program=random.choice(all_instruments), time=0))
    note = random.randint(min_note, max_note)

    for i in range(100):
        #track.append(mido.Message("program_change", program=harpsichord, time=0))
        track.append(mido.Message("note_on", note=note, time=random.randint(min_time, max_time)))
        track.append(mido.Message("note_off" , note=note, time=random.randint(min_pause_time, max_pause_time)))
        note += random.randint([1,-1])
        #track.append(mido.Message(random.choice(live), note=random.randint(0, max_note), time=random.randint(0, max_time)))

    return track

voices = 4
for i in range(voices):
    mid.tracks.append(random_track())

mid.save("random_synth.mid")

'''
n_file = mido.MidiFile()
for track in m_file.tracks:
    n_track = []
    for msg in track:
        print(msg.type)
        if msg.type in ["note_on", "note_off"]:
            print(msg.velocity)
            n_msg = msg.copy(velocity=int(random.random() * msg.velocity), time=int(random.random() * msg.time))
            print(n_msg.velocity)
            n_track.append(n_msg)
        else:
            n_track.append(msg)
    n_file.tracks.append(n_track)

print(n_file)
n_file.save("test.mid")
'''
