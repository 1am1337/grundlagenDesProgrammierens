

- Midi-Toolbox
	- MidiNote
	- MidiRest
	- Sequence (bisher ohne Ton-Überlappungen)
		- Oktave
		- Notennamen
		- transponieren
		- Umkehrung
		- Krebs
		- Analyse
			- Intervalle zählen
			- Noten zählen
			- histogramme der intervalle
			- rhythmische Dichte
		- generate scale
		- generate chord
		- pattern generatoren (z.b. euclidean rhythms)
		- velocity curves
		- arpeggiate
		- "humanisierung"
			- random micro-timing
			- random velocity fluctuation
	- Abspielen
		- mtof <->
	- MidiDateien
	- visualisierung 
		- ascii-piano roll oder matplotlib
- utility Funktionen
	- input (Überprüfungsmöglichkeiten)
	- Funktionen auswählen

```mermaid
classDiagram

	%% Basisklassen
	class MidiEvent{
		+float duration
	}
	
	class MidiRest {
	}
	
	class MidiNote {
		+int pitch
		+float velocity
        +getPitch()
		+getOctave()
		+getFrequency()
		+getNoteName()
		+transpose(amount)
		%%+invert()
		%%+retrograde()
	}

	class MidiChord {
		+List~MidiNote~ notes
		+transpose(amount)
		+invert()
		+arpeggiate(mode)
	}
	
	class MidiSequence {
		+List~MidiEvent|MidiChord~ events
        +getPitches()
        +getDurations()
		+getOctaves()
		+getFrequencys()
		+getNoteNames()
		+transpose(amount)
		+invert()
		+retrograde()
		+countIntervals()
		+countMidiNotes()
		+generateScale(scaleType)
		+generateChord(chordType)
		+generatePattern(patternType)
		+applyVelocityCurve(curveType)
		+humanize(timingVariance, velocityVariance)
		+analyzeIntervals()
		+intervalHistogram()
		+visualize(ascii=true)
		+play()
	}

	%% Visualisierung & Playback
	class Visualizer {
		+plotPianoRoll(sequence)
		+asciiRoll(sequence)
	}

	class MidiPlayer {
		+play(sequence)
	}

	%% File IO
	class MidiFileHandler {
		+load(filename)
		+save(sequence, filename)
	}

	%% Utilities
	class Utils {
		+validateInput(obj)
		+selectFunction(options)
	}

	%% Beziehungen
	MidiEvent <|-- MidiRest
	MidiEvent <|-- MidiNote
	MidiSequence o-- MidiEvent
	MidiSequence o-- MidiChord
	MidiChord o-- MidiNote
	MidiSequence --> Visualizer
	MidiSequence --> MidiPlayer
	MidiSequence --> MidiFileHandler
	MidiSequence --> Utils
```

- Assoziation
	- Composition
	- Aggregation
