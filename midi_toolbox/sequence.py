from event import MidiEvent
from rest import MidiRest
from note import MidiNote


class MidiSequence():

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
