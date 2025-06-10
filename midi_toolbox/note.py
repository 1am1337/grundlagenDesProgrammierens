from event import MidiEvent


class MidiNote(MidiEvent):

    def __init__(self, pitch:int, dur:float):
        super().__init__(dur)
        self.pitch = pitch

    def getPitch(self) -> int:
        return self.pitch

    def getNoteName(self) -> str:
        noteNames = ('C', 'Cis', 'D', 'Dis', 'E', 'F', 'Fis', 'G', 'Gis', 'A', 'Ais', 'H')
        return noteNames[self.pitch % 12]

    def getOctave(self) -> int:
        return self.pitch // 12 - 1

    def getFrequency(self) -> float:
        return 440 * 2 ** ((self.pitch - 69) / 12)

    # desruktiv
    def transpose(self, amount):
        self.pitch += amount
    
    # nicht-destruktiv
    def getTransposed(self, amount) -> 'MidiNote':
        return MidiNote(self.pitch + amount, self.dur)


if __name__ == "__main__":

    for i in range(128):
        note = MidiNote(i, 1/4)
        print(f'-----------------------------')
        print(f'Pitch: {note.getPitch()}')
        print(f'Note: {note.getNoteName()}')
        print(f'Octave: {note.getOctave()}')
        print(f'Frequency: {note.getFrequency()}')

    myNote = MidiNote(60, 1/2)
    print(f'Note pitch: {myNote.getPitch()}, name: {myNote.getNoteName()}')
    myNote.transpose(-7)
    print(f'Note pitch: {myNote.getPitch()}, name: {myNote.getNoteName()}')
