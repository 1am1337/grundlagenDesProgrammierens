import mido

# with open("/Users/danielhopfner/Desktop/grundlagen-des-programmierens-2024-2025/data/bwv772.mid", "rb") as file:
# # with open("bwv772.mid", "rb") as file:
#     content = file.read()
#     print(content[14:14 + 22])


midifile = mido.MidiFile('/Users/danielhopfner/Desktop/grundlagen-des-programmierens-2024-2025/data/bwv772.mid')

# for i, msg in enumerate(midifile):

#     print(msg)

#     if i == 40:
#         break

# print()
for track in midifile.tracks:

    print(f'Track Name: "{track.name}", Number of messages: {len(track)}')

# track 1
track1 = midifile.tracks[1]
for i, msg in enumerate(track1):

    if i < 40:

        if msg.type == 'note_on':
            print(msg.note)
