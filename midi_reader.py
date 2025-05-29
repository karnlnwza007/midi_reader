import mido

def read_midi_and_detect_note_on_quarter_beats(filename):
    midi = mido.MidiFile(filename)
    ticks_per_beat = midi.ticks_per_beat
    quarter_tick = ticks_per_beat // 4  # 1/4 beat in ticks
    print(f"ticks_per_beat = {ticks_per_beat}")
    print(f"Total tracks: {len(midi.tracks)}")

    note_on_events = []

    for i, track in enumerate(midi.tracks):
        current_tick = 0
        for msg in track:
            print(msg)
        for msg in track:
            print(f"adding {current_tick} + {msg.time} = {current_tick + msg.time}")
            current_tick += msg.time

            if msg.type == 'note_on':
                if current_tick % quarter_tick == 0:
                    print(f"msg = {msg} ")
                    print(f"current_tick = {current_tick} ; ticks_per_beat = {ticks_per_beat} beat = {current_tick/ticks_per_beat}")
                    time_in_beats = current_tick / ticks_per_beat
                    note_on_events.append({
                        'track': i,
                        'note': msg.note,
                        'velocity': msg.velocity,
                        'tick': current_tick,
                        'beat': time_in_beats
                        })

    return note_on_events

# Example usage
filename = 'test.mid'
events = read_midi_and_detect_note_on_quarter_beats(filename)

for e in events:
    print(f"Track {e['track']} | Beat {e['beat']:.2f} | Note {e['note']} | Velocity {e['velocity']}")

