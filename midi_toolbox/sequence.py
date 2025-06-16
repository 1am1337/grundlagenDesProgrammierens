from event import MidiEvent
from rest import MidiRest
from note import MidiNote


class MidiSequence():
    INTERVALS_MAJOR = [0, 2, 4, 5, 7, 9, 11]
    INTERVALS_MINOR = [0, 2, 3, 5, 7, 8, 10]
    INTERVALS_CHROMATIC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # `events`` kann eigentlich auch MidiChords beinhalten (sobald die Klasse implementiert ist)
    def __init__(self, events: list[MidiEvent]) -> 'MidiSequence':
        self.events = events

    def __callEventMethodInLoop(self, method, includeRests):
        values = []
        for event in self.events:
            if includeRests:
                if isinstance(event, MidiNote):
                    values.append(getattr(event, method)())
                else:
                    values.append(0)
            else:
                if isinstance(event, MidiNote):
                    values.append(getattr(event, method)())
        return values

    def getPitches(self, includeRests=False) -> list[int]:
        return self.__callEventMethodInLoop('getPitch', includeRests)

    def getOctaves(self, includeRests=False) -> list[int]:
        return self.__callEventMethodInLoop('getOctave', includeRests)

    def getDurations(self, includeRests=True) -> list[float]:
        durations = []
        for event in self.events:
            if includeRests:
                durations.append(event.getDuration())
            else:
                if isinstance(event, MidiNote):
                    durations.append(event.getDuration())
        return durations

    def transposeRelative(self, offset) -> None:
        for event in self.events:
            if isinstance(event, MidiNote):
                event.transpose(offset)

    def transposeAbsolute(self, destination) -> None:
        # Getting the first note in the sequence.
        firstNote = None
        for event in self.events:
            if isinstance(event, MidiNote):
                firstNote = event
                break
            if firstNote == None:
                print('Cannot transpose sequence without notes!')
                return

        offset = 0
        if isinstance(destination, MidiNote):
            offset = destination.pitch
        elif isinstance(destination, int):
            offset = destination
        else:
            print('Invalid destination!')
            return

        offset -= firstNote.pitch
        self.transposeRelative(offset)

    @staticmethod
    def generateScale(fundamental: MidiNote, intervals: list[int]):
        midi_seq = MidiSequence([MidiNote(interval, 1.) for interval in intervals])
        midi_seq.transposeAbsolute(fundamental)
        return midi_seq


if __name__ == '__main__':

    mySequence = MidiSequence([
        MidiNote(60, 1/4),
        MidiNote(62, 1/4),
        MidiNote(64, 1/4),
        MidiNote(65, 1/4),
        MidiNote(67, 1/4),
        MidiRest(1/4),
        MidiNote(69, 1/4),
        MidiNote(71, 1/4),
        MidiNote(72, 1/4)
    ])

    print(f'Pitches: {mySequence.getPitches(includeRests=True)}, octaves: {mySequence.getOctaves()},\ndurations: {mySequence.getDurations()}')
