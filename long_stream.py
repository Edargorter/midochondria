#!/usr/bin/env python3

import os
import mido
import random

harpsichord=6

#INFO

mid = mido.MidiFile()

live = ["note_on", "note_off"]

#Instruments 
synth_bass = [38, 39]
synth_pad = [i for i in range(88, 96)]

#All
all_instruments = synth_bass + synth_pad

#Note jumps 
bass_note_movements = [7, -7, 3, -3, 4, -4, 5, -5]
tonal_movements = [2,1,-1, -2, 0]

#Time ranges
bass_time_range = [5000, 10000]
other_time_range = [2000, 5000]

min_note = 10
max_note = 100
max_program = 127

min_time = 2000
max_time = 5000

min_pause_time = 1000
max_pause_time = 5000

#Create drawn-out, streams of synth sound 

def random_track(instruments, note_range, note_movements, time_range):
    track = mido.MidiTrack()
    track.append(mido.Message("program_change", program=random.choice(instruments), time=0))
    note = random.randint(min_note, max_note)

    for i in range(100):
        #track.append(mido.Message("program_change", program=harpsichord, time=0))
        track.append(mido.Message("note_on", note=random.randint(note_range[0], note_range[1]), time=random.randint(time_range[0], time_range[1])))
        #track.append(mido.Message("note_off" , note=note, time=0))
        note = (note + random.choice(note_movements)) % max_note
        #track.append(mido.Message(random.choice(live), note=random.randint(0, max_note), time=random.randint(0, max_time)))

    return track

voices = 3
vocal_range = (max_note - min_note)/voices

#Bass
mid.tracks.append(random_track(synth_bass, [min_note, max_note], bass_note_movements, bass_time_range))

#Mid-high range instuments 
for i in range(voices):
    mid.tracks.append(random_track(synth_pad, [min_note + i*vocal_range, min_note + (i + 1)*vocal_range], tonal_movements, other_time_range))

mid.save("random_synth.mid")
