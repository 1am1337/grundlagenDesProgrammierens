 

class MidiEvent:

    def __init__(self, dur: float):
        self.dur = dur

    def getDuration(self) -> float:
        return self.dur


if __name__ == '__main__':

    myEvent = MidiEvent(1/2)
    print(f'Event duration: {myEvent.getDuration()}')
