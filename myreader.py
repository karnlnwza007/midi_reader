import mido

# quarter , eighth, sixteenth , 32th...
note_resolution = 4
after_last_note = 0
filename = 'test.mid'
midi = mido.MidiFile(filename)
ticks_per_beat = midi.ticks_per_beat
beat_divider = ticks_per_beat /(note_resolution/4)

beat_list = []
note_in_beat = []
max_layer = 0
note_counts_in_beat = 0

for i, track in enumerate(midi.tracks):
    current_tick = 0
    for msg in track:
        current_tick += msg.time
        if msg.type == 'note_on':
            # print(msg)
            beat = int(current_tick / beat_divider)
            if beat in beat_list:
                #add another note to same beat
                note_counts_in_beat += 1
                if(note_counts_in_beat > max_layer):
                    max_layer = note_counts_in_beat
                note_in_beat[beat_list.index(beat)].append(msg.note)
            else:
                #add new beat and new note
                note_counts_in_beat = 1
                if(note_counts_in_beat > max_layer):
                    max_layer = note_counts_in_beat
                beat_list.append(beat)
                note_in_beat.append([msg.note])
print(f"max layer is {max_layer}")
print(f"beat_list has {len(beat_list)}. note_in_beat has {len(note_in_beat)}")
for i in range(len(beat_list)):
    print(f"i={i} >> ",end ="")
    print(beat_list[i],end =":")
    print(note_in_beat[i])
#print result in desired format
for i in range(max_layer):
    print("[",end="")
    for j in range(beat_list[-1]+ 1 + after_last_note):
        #if that beat has note
        if j in beat_list:
            #if note can fit in earlier layer
            if(len(note_in_beat[beat_list.index(j)]) >= i+1):
                print(f"{note_in_beat[beat_list.index(j)][i]}",end = "")
            #if beat has note but not as many as max_layer
            else:
                print(" 0",end ="")
        #if there's no note in that beat
        else:
            print(" 0",end ="")
        if(j == beat_list[-1] + 1 + after_last_note -1):
            print("",end="")
        else:
           print(",",end = "")
    print("]")
