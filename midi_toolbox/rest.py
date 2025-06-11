from event import MidiEvent


class MidiRest(MidiEvent):

    def __init__(self, dur: float):
        super().__init__(dur)


if __name__ == '__main__':

    rest = MidiRest(1/2)
    print(f'Rest duration: {rest.getDuration()}')
