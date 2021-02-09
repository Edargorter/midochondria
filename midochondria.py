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
track = mido.MidiTrack()

live = ["note_on", "note_off"]
max_note = 127
max_program = 127
max_time = 50
mid.tracks.append(track)

'''
for i in range(max_program):
    track.append(mido.Message("program_change", program=6, time=0))
    track.append(mido.Message("note_on", note=random.randint(0, max_note), time=1000))
    track.append(mido.Message("note_off" , note=random.randint(0, max_note), time=1000))

mid.save("programs.mid")
'''

#Random output
for i in range(100):
    #track.append(mido.Message("program_change", program=harpsichord, time=0))
    track.append(mido.Message("program_change", program=random.randint(0, max_program), time=0))
    track.append(mido.Message("note_on", note=random.randint(0, max_note), time=random.randint(0, 150)))
    track.append(mido.Message("note_off" , note=random.randint(0, max_note), time=random.randint(0, 150)))
    #track.append(mido.Message(random.choice(live), note=random.randint(0, max_note), time=random.randint(0, max_time)))

mid.save("random.mid")


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
