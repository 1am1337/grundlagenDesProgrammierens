import mido
import os
from pathlib import Path

midifile_path = Path(__file__). parent / "bwv772.mid"
midifile = mido.MidiFile(midifile_path)

class MidiNote:
    def __init__(self, note, velocity, time_on, time_off):
        self.note = note
        self.velocity = velocity
        self.time_on = time_on
        self.time_off = time_off
    def __repr__(self):
        return f"<MidiNote: note: {self.note}, velocity: {self.velocity}, on: {self.time_on}, off: {self.time_off}>"

onset_notes = {}
sequence = []
track1 = midifile.tracks[1]
abs_time = 0
for msg in midifile:
    if msg.type == "set_tempo":
        tempo = msg.tempo


for i, msg in enumerate(track1):
    abs_time += mido.tick2second(msg.time, midifile.ticks_per_beat, tempo)
    if msg.type == "note_on":
        onset_notes[msg.note] = [MidiNote(note=msg.note, velocity=msg.velocity, time_on=abs_time, time_off=0)]
    if msg.type == "note_off":
        midinote = onset_notes.get(msg.note).pop(0)
        midinote.time_off = abs_time
        sequence.append(midinote)
[print(note) for note in sequence]