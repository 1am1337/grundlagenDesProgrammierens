# Datei: midi_app.py
import streamlit as st
import mido

# st.title("MIDI-Info")
uploaded = st.file_uploader("MIDI-Datei hochladen", type="mid")

if uploaded:
    mid = mido.MidiFile(file=uploaded)
    for i, track in enumerate(mid.tracks):
        st.write(f"Track {i}: {track.name}, Events: {len(track)}")

# Terminal: streamlit run streamlit.py
