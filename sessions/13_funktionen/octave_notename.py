
# immutable type
# tuple
notenames = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
# globale variable

# mutable collection types
# mylist = [1, 2, 3]
# dict = {'key1': 1, 'key2': 2, 'key3': 3}

def get_notename(midinum):

    # notenames = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
    # lokale variable

    # modulo: %, divisionsrest
    # 0 % 12  --> 0
    # 12 % 12 --> 0
    # 13 % 12 --> 1
    # 14 % 12 --> 2

    return notenames[midinum % 12]

def get_octave(midinum):
    # ganzzahl-division //
    return (midinum // 12) - 1

def get_notename_octave(midinum):

    print(get_notename(midinum), get_octave(midinum))

get_notename_octave(60)
get_notename_octave(57)

print(notenames)
