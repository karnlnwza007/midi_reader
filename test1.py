import mido
from collections import defaultdict
import math

def read_midi_group_notes_by_beat(filename):
    midi = mido.MidiFile(filename)
    ticks_per_beat = midi.ticks_per_beat
    print(f"Ticks_per_beat = {ticks_per_beat}")
    beat_notes = defaultdict(list)

    for track in midi.tracks:
        current_tick = 0
        for msg in track:
            print(msg)
            current_tick += msg.time

            if msg.type == 'note_on' and msg.velocity > 0:
                beat_index = int(current_tick / ticks_per_beat)  # Floor to whole beat
                beat_notes[beat_index].append(msg.note)

    max_beat = max(beat_notes.keys()) if beat_notes else 0

    print(beat_notes)
    # Print every beat from 0 to max, even if there are no notes
    for beat in range(max_beat + 1):
        notes = beat_notes.get(beat, [0])
        note_list = ", ".join(map(str, notes))
        print(f"beat {beat} note {{{note_list}}}")

# Example usage:
filename = 'test.mid'
read_midi_group_notes_by_beat(filename)

