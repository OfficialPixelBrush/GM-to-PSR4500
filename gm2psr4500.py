import sys
import os
from mido import MidiFile, MidiTrack, Message

# Load the MIDI file specified by the first command-line argument
mid = MidiFile(sys.argv[1])

# New remapped instrument (example: changing all instrument patches to Piano)
#REMAP_TO_INSTRUMENT = 0  # 0 corresponds to Acoustic Grand Piano in General MIDI
# Index = Mapped Instrument
InstrumentLUT = [
    # Piano
     3, # 01 Acousting Grand Piano  = 00/03 Piano 1
    52, # 02 Bright Acoustic Piano  = 01/52 Piano 2
     5, # 03 Electric Grand Piano   = 03 Elec. Piano 1  - 05 Electric Piano 1
    25, # 04 Honky-tonk Piano       = 02/25 Honky Tonk Piano
     5, # 05 Electric Piano 1       = 03 Elec. Piano 1  - 05 Electric Piano 1
    54, # 06 Electric Piano 2       = 04 Elec. Piano 2  - 54 Electric Piano 2
     4, # 07 Harpsichord            = 05/04 Harpsichord
    # Chromatic Percussion
    30, # 08 Clavinet               = 06 Clavi          - 30 Funky Clavi
     6, # 09 Celesta                = 07/06 Celesta
    32, # 10 Glockenspiel           = 10 Glocken        - 32 Glockenspiel
    24, # 11 Music Box              = 19/24 Music Box
     7, # 12 Vibraphone             = 09 Vibes          - 07 Vibraphone
     8, # 13 Marimba                = 13/08 Marimba
    59, # 14 Xylophone              = 08/59 Xylophone
    62, # 15 Tubular Bells          = 11 Chimes         - 62 Tubular Bells
     4, # 16 Dulcimer               = 05 Harpsichord    - 04 Harpsichord 1
    # Organ
    29, # 17 Drawbar Organ          = 48 Pipe Organ     - 29 Pipe Organ 2
    27, # 18 Percussive Organ       = 50 Rock Organ     - 27 Rock Organ
    27, # 19 Rock Organ             = 50 Rock Organ     - 27 Rock Organ
    29, # 20 Church Organ           = 48 Pipe Organ     - 29 Pipe Organ 2
    49, # 21 Reed Organ             = 51 Street Organ   - 49 Reed Organ
    31, # 22 Accordion              = 37/31 Accordion
    22, # 23 Harmonica              = 37/22 Harmonica
    31, # 24 Tango Accordion        = 37/31 Accordion
    # Guitar
    73, # 25 Acoustic Guitar (nylon)= 55/73 Classic Guitar
    36, # 26 Acoustic Guitar (steel)= 56/36 Folk Guitar
    12, # 27 Electric Guitar (jazz) = 57/12 Jazz Guitar
    68, # 28 Electric Guitar (clean)= 58 Rock Guitar    - 68 Rock Guitar 2
    70, # 29 Electric Guitar (muted)= 60 Mute Guitar    - 70 Rock Guitar 4
    68, # 30 Overdriven Guitar      = 58 Rock Guitar    - 68 Rock Guitar 3
    13, # 31 Distortion Guitar      = 58 Rock Guitar    - 13 Rock Guitar 1 (Dist)
    69, # 32 Guitar harmonics       = 58 Rock Guitar    - 69 Rock Guitar 3
    # Bass
    14, # 33 Acoustic Bass          = 66 Acoustic Bass  - 14 Wood Bass 1
    38, # 34 Electric Bass (finger) = 68 Elec. Bass 1   - 38 Electric Bass 1
    79, # 35 Electric Bass (pick)   = 69 Elec. Bass 2   - 79 Electric Bass 2
    80, # 36 Fretless Bass          = 71 Fretless Bass  - 80 Electric Bass 3
    39, # 37 Slap Bass 1            = 70/39 Slap Bass
    39, # 38 Slap Bass 2            = 70/39 Slap Bass
    81, # 39 Synth Bass 1           = 72 Synth Bass 1 - 81 Wood Bass 2
    58, # 40 Synth Bass 2           = 73 Synth Bass 2 - 58 Synth Bass 1
    # Strings
    10, # 41 Violin                 = 25 Violin         - 10 Violin 1
    10, # 42 Viola                  = 25 Violin         - 10 Violin 1
    11, # 43 Cello                  = 26/11 Cello
    11, # 44 Contrabass             = 26/11 Cello
    50, # 45 Tremolo Strings        = 21/50 Strings 2
    78, # 46 Pizzicato Strings      = 22 Pizz. Strings  - 78 Pizzicato Strings
    37, # 47 Orchestral Harp        = 27/37 Harp
    66, # 48 Timpani                = 15/66 Timpani
    # Strings (continued)
    41, # 49 String Ensemble 1      = 20/41 Strings 1
    50, # 50 String Ensemble 2      = 21/50 Strings 2
    51, # 51 Synth Strings 1        = 23 Synth Strings 1- 51 Synth Strings
    67, # 52 Synth Strings 2        = 24 Synth Strings 2- 67 Violin 2
    94, # 53 Choir Aahs             = 52 Human Vox      - 94 Human Voice 1
    95, # 54 Voice Oohs             = 53 Husky          - 95 Human Voice 2
    96, # 55 Synth Voice            = 52 Human Vox      - 96 Human Chorus
    90, # 56 Orchestra Hit          = 99/90 Orchestra Hit
    # Brass
    15, # 57 Trumpet                = 39/15 Trumpet
    16, # 58 Trombone               = 41/16 Trombone
    84, # 59 Tuba                   = 43/84 Tuba
    44, # 60 Muted Trumpet          = 40/44 Mute Trumpet
    17, # 61 French Horn            = 42/17 Horn
    92, # 62 Brass Section          = 44 Brass Ensemble - 92 Brass Ensemble 1
     0, # 63 Synth Brass 1          = 00 Synth Brass 1
    82, # 64 Synth Brass 2          = 82 Synth Brass 2
    # Reed
    18, # 65 Soprano Sax            = 34 Saxophone 1    - 18 Sax
    18, # 66 Alto Sax               = 34 Saxophone 1    - 18 Sax
    42, # 67 Tenor Sax              = 35 Saxophone 2    - 42 Alpenhorn
    42, # 68 Baritone Sax           = 35 Saxophone 2    - 42 Alpenhorn
    21, # 69 Oboe                   = 32/21 Oboe
    17, # 70 English Horn           = 42/17 Horn
    97, # 71 Bassoon                = 33 Basson         - 97 Kazoo
    19, # 72 Clarinet               = 31/19 Clarinet
    # Pipe
    20, # 73 Piccolo                = 28/20 Flute
    20, # 74 Flute                  = 28/20 Flute
    88, # 75 Recorder               = 30/88 Recorder
    47, # 76 Pan Flute              = 29/47 Pan Flute
    46, # 77 Blown Bottle           = 76 Soft Cloud - 46 Jug
    46, # 78 Shakuhachi             = 76 Soft Cloud - 46 Jug
    23, # 79 Whistle                = 54/23 Whistle
    23, # 80 Ocarina                = 54 Whistle - 89 Ocarina
    # Synth Lead
    81, # 81 Lead 1 (square)        = 72 Synth Bass 1   - 81 Wood Bass 2
    58, # 82 Lead 2 (sawtooth)      = 73 Synth Bass 2   - 58 Synth Bass 1
    53, # 83 Lead 3 (calliope)      = 77 Daybreak       - 53 Harpischord 2
    46, # 84 Lead 4 (chiff)         = 76 Soft Cloud     - 46 Jug
    69, # 85 Lead 5 (charang)       = 79 Arabesque      - 69 Rock Guitar
    96, # 86 Lead 6 (voice)         = 52 Human Vox      - 96 Human Chorus
    71, # 87 Lead 7 (fifths)        = 89 Syntherimba    - 71 Pedal Stel Guitar
    56, # 88 Lead 8 (bass + lead)   = 78 Sunbeam        - 56 Bandneon
    # Synth Pad
     5, # 89 Pad 1 (new age)        = 03/05 Electric Piano
    99, # 90 Pad 2 (warm)           = 81 Landscape      - 99 Sine Wave
    85, # 91 Pad 3 (polysynth)      = 91 After Burner   - 85 Synth Reed 2
    95, # 92 Pad 4 (choir)          = 53 Husky          - 95 Human Voice 2
    63, # 93 Pad 5 (bowed)          = 85 Glass Bell 2   - 63 Hand Bell
    45, # 94 Pad 6 (metallic)       = 82 Metallic       - 45 Synth Reed
    55, # 95 Pad 7 (halo)           = 90 African Percuss- 55 Glass Celesta
    53, # 96 Pad 8 (sweep)          = 77 Daybreak       - 53 Harpiscord 2
]

PercussionLUT = {
    35: 44, # 35 Bass Drum 2    -> 44 Low Bass Drum
    36: 45, # 36 Bass Drum 1    -> 45 Bass Drum
    38: 49, # 38 Snare Drum 1   -> 49 Light Snare Drum
    39: 54, # 39 Hand Clap      -> 54 Claps
    40: 52, # 40 Snare Drum 2   -> 52 Heavy Snare Drum
    41: 48, # 41 Low Tom 2      -> 48 Low Tom
    42: 57, # 42 Closed Hi-hat  -> 48 Closed Hi-Hat
    43: 47, # 43 Low Tom 1      -> 47 Bass Tom
    45: 50, # 45 Mid Tom 2      -> 50 Middle Tom
    46: 59, # 46 Open Hi-hat    -> 59 Open Hi-Hat
    47: 42, # 47 Mid Tom 1      -> 42 Middle Synth Tom
    48: 53, # 48 High Tom 2     -> 53 High Tom
    49: 60, # 49 Crash Cymbal 1 -> 60 Crash Cymbal
    50: 43, # 50 High Tom 1     -> 43 High Synth Tom
    51: 64, # 51 Ride Cymbal 1  -> 64 Ride Symbal
}

# Iterate over tracks to find and remap instrument change messages
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type in ('note_on', 'note_off') and msg.channel == 9:  # Channel 10 (0-indexed)
            if msg.note in PercussionLUT:
                #print(f'Remapping percussion note {msg.note} to {PercussionLUT[msg.note]}')
                msg.note = PercussionLUT[msg.note]  # Remap the note number
            else:
                # Workaround while some sounds aren't accounted for
                msg.note = 38
        if msg.type == 'program_change':  # Look for instrument change events
            if (msg.program < len(InstrumentLUT)):
                print(f'Remapping instrument from {msg.program} to {InstrumentLUT[msg.program]}')
                msg.program = InstrumentLUT[msg.program]  # Change instrument
            else:
                print(f'Unknown instrument {msg.program}, assigning Piano')
                msg.program = 3

# Save the modified MIDI file
mid.save(os.path.basename(sys.argv[1]))
