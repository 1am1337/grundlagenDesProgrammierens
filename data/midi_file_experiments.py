import mido
from pathlib import Path


midifile_path = Path(__file__).parent / 'bwv772.mid' # __file__: Default-Variable, die zur aktuellen Datei zeigt
midifile = mido.MidiFile(midifile_path)

for msg in midifile:
    if msg.type == 'set_tempo':
        tempo = msg.tempo


# class MidiNote:

#     def __init__(self, note, velocity, time_on, time_off):
#         self.note = note
#         self.velocity = velocity
#         self.time_on = time_on
#         self.time_off = time_off

#     def __repr__(self):
#         return f'<MidiNote: note: {self.note}, velocity: {self.velocity}, on: {self.time_on}, off: {self.time_off}>'


onset_notes = {
    # expected data structure:
    # 60: [MidiNote(note=60, velocity=64, time_on=0, time_off=0)],
}
sequence = []
abs_time = 0

# track 1
track1 = midifile.tracks[1]
for i, msg in enumerate(track1):

        # msg.time sind immer die Zeit-Unterschiede zwischen den aufeinanderfolgenden Events (egal ob note-on oder -off)
        abs_time += mido.tick2second(msg.time, midifile.ticks_per_beat, tempo)

        if msg.type == 'note_on':
            onset_notes[msg.note] = [MidiNote(note=msg.note, velocity=msg.velocity, time_on=abs_time, time_off=0)]
        if msg.type == 'note_off':
            midinote = onset_notes.get(msg.note).pop(0)
            midinote.time_off = abs_time
            sequence.append(midinote)


[print(note) for note in sequence]


# Übungsaufgabe bis nächste Woche: 
# MidiNote und MidiSequence aktualisieren, sodass sie mit dem
# Auslesen der Midi-Files kompatibel sind (draft siehe die Klasse in dieser Datei)

# --> nicht mehr die `MidiNote`-Klasse verwenden, die hier in der
# Datei implementiert wurde, sondern:

# from ..midi_toolbox.note import MidiNote
# from ..midi_toolbox.sequence import MidiSequence
