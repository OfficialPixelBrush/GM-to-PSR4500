import sys
import os
from mido import MidiFile, MidiTrack, Message
from enum import Enum

class PSR(Enum):
	SYNTH_BRASS_1           = 0
	JAZZ_ORGAN              = 1
	PIPE_ORGAN_1            = 2
	PIANO_1                 = 3
	HARPISCHORD_1           = 4
	ELECTRIC_PIANO_1        = 5
	CELESTA                 = 6
	VIBRAPHONE              = 7
	MARIMBA                 = 8
	STEEL_DRUM              = 9
	VIOLIN_1                = 10
	CELLO                   = 11
	JAZZ_GUITAR             = 12
	ROCK_GUITAR_1_DISTORTION= 13
	WOOD_BASS_1             = 14
	TRUMPET                 = 15
	TROMBONE                = 16
	HORN                    = 17
	SAX                     = 18
	CLARINET                = 19
	FLUTE                   = 20
	OBOE                    = 21
	HARMONICA               = 22
	WHISTLE                 = 23
	MUSIC_BOX               = 24
	HONKY_TOY_PIANO         = 25
	TOY_PIANO               = 26
	ROCK_ORGAN              = 27
	TREMOLO_ORGAN           = 28
	PIPE_ORGAN_2            = 29
	FUNKY_CLAVI             = 30
	ACCORDION               = 31
	GLOCKENSPIEL            = 32
	HAWAIIAN_GUITAR         = 33
	BANJO                   = 34
	BOWED_BASS              = 35
	FOLK_GUITAR             = 36
	HARP                    = 37
	ELECTRIC_BASS_1         = 38
	SLAP_BASS               = 39
	UKULELE                 = 40
	STRINGS_1               = 41
	ALPENHORN               = 42
	BAGPIPE                 = 43
	MUTE_TRUMPET            = 44
	SYNTH_REED_1            = 45
	JUG                     = 46
	PAN_FLUTE               = 47
	ICE_BLOCK               = 48
	REED_ORGAN              = 49
	STRINGS_2               = 50
	SYNTH_STRINGS           = 51
	PIANO_2                 = 52
	HARPSICHORD_2           = 53
	ELECTRIC_PIANO_2        = 54
	GLASS_CELESTA           = 55
	BANDONEON               = 56
	STREET_ORGAN            = 57
	SYNTH_BASS_1            = 58
	XYLOPHONE               = 59
	SYNTH_PERCUSSION        = 60
	KALIMBA                 = 61
	TUBULAR_BELLS           = 62
	HAND_BELL               = 63
	CARILLION               = 64
	PIZZICATO_VIOLIN        = 65
	TIMPANI                 = 66
	VIOLIN_2                = 67
	ROCK_GUITAR_2           = 68
	ROCK_GUITAR_3           = 69
	ROCK_GUITAR_4           = 70
	PEDAL_STEEL_GUITAR      = 71
	TWELVE_STRING_GUITAR    = 72
	CLASSIC_GUITAR          = 73
	MANDOLIN                = 74
	SITAR                   = 75
	KOTO                    = 76
	SHAMISEN                = 77
	PIZZICATO_STRINGS       = 78
	ELECTRIC_BASS_2         = 79
	ELECTRIC_BASS_3         = 80
	WOOD_BASS_2             = 81
	SYNTH_BRASS_2           = 82 # The manual calls this SYNTH BASS 2 on the Midi-in side, but SYNTH BRASS 2 on the PSR side
	WOW_TRUMPET             = 83
	TUBA                    = 84
	SYNTH_REED_2            = 85
	SYNTH_BASS_2            = 86
	FLUGELHORN              = 87
	RECORDER                = 88
	OCARINA                 = 89
	ORCHESTRA_HIT           = 90
	SAMBA_WHISTLE           = 91
	BRASS_ENSEMBLE          = 92
	WOODWIND_ENSEMBLE       = 93
	HUMAN_VOICE_1           = 94
	HUMAN_VOICE_2           = 95
	HUMAN_CHORUS            = 96
	KAZOO                   = 97
	MUSIC_SAW               = 98
	SIN_WAVE                = 99 # **Sine wave?
	# Past this I need to use the PSR Label
	BAMBOO_MARIMBA          = 100
	GAMELAN                 = 101
	SYNTH_STRINGS_2         = 102
	AQUA                    = 103
	LANDSCAPE               = 104
	METALLIC                = 105
	CRYSTAL                 = 106
	SAXOPHONE_2             = 107
	POWER_BRASS             = 108
	HOLLOW_SYNTH            = 109
	SOFT_CLOUD              = 110
	DAYBREAK                = 111
	SUNBEAM                 = 112
	ARABESQUE               = 113
	GLASS_BELLS             = 114
	SYNTH_BELLS             = 115
	BELL_FOUNTAIN           = 116
	SYNTHERIMBA             = 117
	AFRICAN_PERCUSSION      = 118
	AFTER_BURNER            = 119
	WAVE                    = 120
	FUNNY                   = 121
	MONSTER                 = 122
	HA_HA_HA                = 123
	EMERGENCY               = 124
	RACING_CIRCUIT          = 125
	STORM                   = 126
	NO_CHANGE               = 127

class PSR_Rhythm(Enum):
	REVERSE_CYMBAL		= 33
	HIGH_COWBELL		= 34
	HIGH_CRASH_CYMBAL	= 35
	PEDAL_HIGH_HAT		= 36
	CLOSED_TRIANGLE		= 37
	SYNTH_SNARE			= 38
	OPEN_TRIANGLE		= 39
	SYNTH_TOM_BASS		= 40
	SYNTH_TOM_LOW		= 41
	SYNTH_TOM_MID		= 42
	SYNTH_TOM_HI		= 43
	BASS_DRUM_2			= 44
	BASS_DRUM_1			= 45
	RIM_SHOT_2			= 46
	BASS_TOM			= 47
	LOW_TOM				= 48
	SNARE_HI			= 49
	MID_TOM				= 50
	RIM_SHOT			= 51
	SNARE_LO			= 52
	HI_TOM				= 53
	HAND_CLAP			= 54
	COWBELL				= 55
	SHAKER_CABASA		= 56
	HI_HAT_CLOSE		= 57
	BRUSH_HIT			= 58
	HI_HAT_OPEN			= 59
	CRASH_CYMBAL		= 60
	SPLASH_CYMBAL		= 61
	RIDE_CYMBAL_CUP		= 62
	RIDE_CYMBAL			= 63
	CONGA_LOW			= 64
	CONGA_HI_OPEN		= 65
	CONGA_HI_MUTE		= 66
	BONGO_LOW			= 67
	BONGO_HI			= 68
	TIMBALES_LOW		= 69
	TIMBALES_HIGH		= 70
	TAMBOURINE			= 71
	CASTANET			= 72
	CLAVES				= 73
	AGOGO_LOW			= 74
	AGOGO_HI			= 75
	CUICA_LOW			= 76
	CUICA_HI			= 77
	WHISTLE				= 78
	BRUSH				= 79
	# Afer this, taken from PSR side
	HIGH_SAMBA_WHISTLE	= 80
	BIRD_1				= 81
	BIRD_2				= 82
	BIRD_3				= 83
	CAR_HORN			= 84
	BREAKING_GLASS		= 85
	EXPLOSION			= 86
	LOW_SCRATCH			= 87
	HIGH_SCRATCH		= 88
	MALE_LAUGH			= 89
	CHIPMUNK_LAUGH		= 90
	FEMALE_YEAH			= 91
	MALE_YEAH			= 92
	MALE_HA				= 93
	KABUKI_WO			= 94
	TSUZUMI_DRUM		= 95
	APPLAUSE			= 96

class GM(Enum):
	# Piano
	ACOUSTIC_GRAND_PIANO = 1
	BRIGHT_ACOUSTIC_PIANO = 2
	ELECTRIC_GRAND_PIANO = 3
	HONKY_TONK_PIANO = 4
	ELECTRIC_PIANO_1 = 5
	ELECTRIC_PIANO_2 = 6
	HARPSICHORD = 7
	CLAVINET = 8

	# Chromatic Percussion
	CELESTA = 9
	GLOCKENSPIEL = 10
	MUSIC_BOX = 11
	VIBRAPHONE = 12
	MARIMBA = 13
	XYLOPHONE = 14
	TUBULAR_BELLS = 15
	DULCIMER = 16

	# Organ
	DRAWBAR_ORGAN = 17
	PERCUSSIVE_ORGAN = 18
	ROCK_ORGAN = 19
	CHURCH_ORGAN = 20
	REED_ORGAN = 21
	ACCORDION = 22
	HARMONICA = 23
	TANGO_ACCORDION = 24

	# Guitar
	ACOUSTIC_GUITAR_NYLON = 25
	ACOUSTIC_GUITAR_STEEL = 26
	ELECTRIC_GUITAR_JAZZ = 27
	ELECTRIC_GUITAR_CLEAN = 28
	ELECTRIC_GUITAR_MUTED = 29
	OVERDRIVEN_GUITAR = 30
	DISTORTION_GUITAR = 31
	GUITAR_HARMONICS = 32

	# Bass
	ACOUSTIC_BASS = 33
	ELECTRIC_BASS_FINGER = 34
	ELECTRIC_BASS_PICK = 35
	FRETLESS_BASS = 36
	SLAP_BASS_1 = 37
	SLAP_BASS_2 = 38
	SYNTH_BASS_1 = 39
	SYNTH_BASS_2 = 40

	# Strings
	VIOLIN = 41
	VIOLA = 42
	CELLO = 43
	CONTRABASS = 44
	TREMOLO_STRINGS = 45
	PIZZICATO_STRINGS = 46
	ORCHESTRAL_HARP = 47
	TIMPANI = 48

	STRING_ENSEMBLE_1 = 49
	STRING_ENSEMBLE_2 = 50
	SYNTH_STRINGS_1 = 51
	SYNTH_STRINGS_2 = 52
	CHOIR_AAHS = 53
	VOICE_OOHS = 54
	SYNTH_VOICE = 55
	ORCHESTRA_HIT = 56

	# Brass
	TRUMPET = 57
	TROMBONE = 58
	TUBA = 59
	MUTED_TRUMPET = 60
	FRENCH_HORN = 61
	BRASS_SECTION = 62
	SYNTH_BRASS_1 = 63
	SYNTH_BRASS_2 = 64

	# Reed
	SOPRANO_SAX = 65
	ALTO_SAX = 66
	TENOR_SAX = 67
	BARITONE_SAX = 68
	OBOE = 69
	ENGLISH_HORN = 70
	BASSOON = 71
	CLARINET = 72

	# Pipe
	PICCOLO = 73
	FLUTE = 74
	RECORDER = 75
	PAN_FLUTE = 76
	BLOWN_BOTTLE = 77
	SHAKUHACHI = 78
	WHISTLE = 79
	OCARINA = 80

	# Synth Lead
	LEAD_1_SQUARE = 81
	LEAD_2_SAWTOOTH = 82
	LEAD_3_CALLIOPE = 83
	LEAD_4_CHIFF = 84
	LEAD_5_CHARANG = 85
	LEAD_6_VOICE = 86
	LEAD_7_FIFTHS = 87
	LEAD_8_BASS_LEAD = 88

	# Synth Pad
	PAD_1_NEW_AGE = 89
	PAD_2_WARM = 90
	PAD_3_POLYSYNTH = 91
	PAD_4_CHOIR = 92
	PAD_5_BOWED = 93
	PAD_6_METALLIC = 94
	PAD_7_HALO = 95
	PAD_8_SWEEP = 96

	# Synth Effects
	FX_1_RAIN = 97
	FX_2_SOUNDTRACK = 98
	FX_3_CRYSTAL = 99
	FX_4_ATMOSPHERE = 100
	FX_5_BRIGHTNESS = 101
	FX_6_GOBLINS = 102
	FX_7_ECHOES = 103
	FX_8_SCI_FI = 104

	# Ethnic
	SITAR = 105
	BANJO = 106
	SHAMISEN = 107
	KOTO = 108
	KALIMBA = 109
	BAG_PIPE = 110
	FIDDLE = 111
	SHANAI = 112

	# Percussive
	TINKLE_BELL = 113
	AGOGO = 114
	STEEL_DRUMS = 115
	WOODBLOCK = 116
	TAIKO_DRUM = 117
	MELODIC_TOM = 118
	SYNTH_DRUM = 119

	# Sound effects
	REVERSE_CYMBAL = 120
	GUITAR_FRET_NOISE = 121
	BREATH_NOISE = 122
	SEASHORE = 123
	BIRD_TWEET = 124
	TELEPHONE_RING = 125
	HELICOPTER = 126
	APPLAUSE = 127
	GUNSHOT = 128

# New remapped instrument (example: changing all instrument patches to Piano)
#REMAP_TO_INSTRUMENT = 0  # 0 corresponds to Acoustic Grand Piano in General MIDI
# Index = Mapped Instrument
InstrumentLUT = [
	# Piano
	PSR.PIANO_1,                	# 01 Acousting Grand Piano  = 00/03 Piano 1
	PSR.PIANO_2,                	# 02 Bright Acoustic Piano  = 01/52 Piano 2
	PSR.ELECTRIC_PIANO_1,       	# 03 Electric Grand Piano   = 03 Elec. Piano 1  - 05 Electric Piano 1
	PSR.HONKY_TOY_PIANO,        	# 04 Honky-tonk Piano       = 02/25 Honky Tonk Piano
	PSR.ELECTRIC_PIANO_1,       	# 05 Electric Piano 1       = 03 Elec. Piano 1  - 05 Electric Piano 1
	PSR.ELECTRIC_PIANO_2,       	# 06 Electric Piano 2       = 04 Elec. Piano 2  - 54 Electric Piano 2
	PSR.HARPISCHORD_1,          	# 07 Harpsichord            = 05/04 Harpsichord
	# Chromatic Percussion
	PSR.FUNKY_CLAVI,            	# 08 Clavinet               = 06 Clavi          - 30 Funky Clavi
	PSR.CELESTA,                	# 09 Celesta                = 07/06 Celesta
	PSR.GLOCKENSPIEL,           	# 10 Glockenspiel           = 10 Glocken        - 32 Glockenspiel
	PSR.MUSIC_BOX,             		# 11 Music Box              = 19/24 Music Box
	PSR.VIBRAPHONE,             	# 12 Vibraphone             = 09 Vibes          - 07 Vibraphone
	PSR.MARIMBA,                	# 13 Marimba                = 13/08 Marimba
	PSR.XYLOPHONE,              	# 14 Xylophone              = 08/59 Xylophone
	PSR.TUBULAR_BELLS,          	# 15 Tubular Bells          = 11 Chimes         - 62 Tubular Bells
	PSR.HARPSICHORD_2,				# 16 Dulcimer               = 05 Harpsichord    - 04 Harpsichord 1
	# Organ	
	PSR.PIPE_ORGAN_2, 				# 17 Drawbar Organ          = 48 Pipe Organ     - 29 Pipe Organ 2
	PSR.ROCK_ORGAN, 				# 18 Percussive Organ       = 50 Rock Organ     - 27 Rock Organ
	PSR.ROCK_ORGAN, 				# 19 Rock Organ             = 50 Rock Organ     - 27 Rock Organ
	PSR.PIPE_ORGAN_2, 				# 20 Church Organ           = 48 Pipe Organ     - 29 Pipe Organ 2
	PSR.PIPE_ORGAN_1, 				# 21 Reed Organ             = 51 Street Organ   - 49 Reed Organ
	PSR.ACCORDION, 					# 22 Accordion              = 37/31 Accordion
	PSR.HARMONICA, 					# 23 Harmonica              = 37/22 Harmonica
	PSR.ACCORDION, 					# 24 Tango Accordion        = 37/31 Accordion
	# Guitar	
	PSR.CLASSIC_GUITAR, 			# 25 Acoustic Guitar (nylon)= 55/73 Classic Guitar
	PSR.FOLK_GUITAR, 				# 26 Acoustic Guitar (steel)= 56/36 Folk Guitar
	PSR.JAZZ_GUITAR, 				# 27 Electric Guitar (jazz) = 57/12 Jazz Guitar
	PSR.ROCK_GUITAR_2, 				# 28 Electric Guitar (clean)= 58 Rock Guitar    - 68 Rock Guitar 2
	PSR.ROCK_GUITAR_4, 				# 29 Electric Guitar (muted)= 60 Mute Guitar    - 70 Rock Guitar 4
	PSR.ROCK_GUITAR_3, 				# 30 Overdriven Guitar      = 58 Rock Guitar    - 68 Rock Guitar 3
	PSR.ROCK_GUITAR_1_DISTORTION, 	# 31 Distortion Guitar      = 58 Rock Guitar    - 13 Rock Guitar 1 (Dist)
	PSR.ROCK_GUITAR_3, 				# 32 Guitar harmonics       = 58 Rock Guitar    - 69 Rock Guitar 3
	# Bass
	PSR.WOOD_BASS_1, 				# 33 Acoustic Bass          = 66 Acoustic Bass  - 14 Wood Bass 1
	PSR.ELECTRIC_BASS_1,			# 34 Electric Bass (finger) = 68 Elec. Bass 1   - 38 Electric Bass 1
	PSR.ELECTRIC_BASS_2,			# 35 Electric Bass (pick)   = 69 Elec. Bass 2   - 79 Electric Bass 2
	PSR.ELECTRIC_BASS_3,			# 36 Fretless Bass          = 71 Fretless Bass  - 80 Electric Bass 3
	PSR.SLAP_BASS, 					# 37 Slap Bass 1            = 70/39 Slap Bass
	PSR.SLAP_BASS, 					# 38 Slap Bass 2            = 70/39 Slap Bass
	PSR.WOOD_BASS_2, 				# 39 Synth Bass 1           = 72 Synth Bass 1 	- 81 Wood Bass 2
	PSR.SYNTH_BASS_2, 				# 40 Synth Bass 2           = 73 Synth Bass 2 	- 58 Synth Bass 1
	# Strings			
	PSR.VIOLIN_1, 					# 41 Violin                 = 25 Violin         - 10 Violin 1
	PSR.VIOLIN_1,					# 42 Viola                  = 25 Violin         - 10 Violin 1
	PSR.CELLO, 						# 43 Cello                  = 26/11 Cello
	PSR.CELLO, 						# 44 Contrabass             = 26/11 Cello
	PSR.STRINGS_2, 					# 45 Tremolo Strings        = 21/50 Strings 2
	PSR.PIZZICATO_STRINGS, 			# 46 Pizzicato Strings      = 22 Pizz. Strings  - 78 Pizzicato Strings
	PSR.HARP, 						# 47 Orchestral Harp        = 27/37 Harp
	PSR.TIMPANI, 					# 48 Timpani                = 15/66 Timpani
	# Strings (continued)
	PSR.STRINGS_1, 					# 49 String Ensemble 1      = 20/41 Strings 1
	PSR.STRINGS_2, 					# 50 String Ensemble 2      = 21/50 Strings 2
	PSR.SYNTH_STRINGS, 				# 51 Synth Strings 1        = 23 Synth Strings 1- 51 Synth Strings
	PSR.VIOLIN_2, 					# 52 Synth Strings 2        = 24 Synth Strings 2- 67 Violin 2
	PSR.HUMAN_VOICE_1, 				# 53 Choir Aahs             = 52 Human Vox      - 94 Human Voice 1
	PSR.HUMAN_VOICE_2, 				# 54 Voice Oohs             = 53 Husky          - 95 Human Voice 2
	PSR.HUMAN_CHORUS, 				# 55 Synth Voice            = 52 Human Vox      - 96 Human Chorus
	PSR.ORCHESTRA_HIT, 				# 56 Orchestra Hit          = 99/90 Orchestra Hit
	# Brass			
	PSR.TRUMPET, 					# 57 Trumpet                = 39/15 Trumpet
	PSR.TROMBONE, 					# 58 Trombone               = 41/16 Trombone
	PSR.TUBA, 						# 59 Tuba                   = 43/84 Tuba
	PSR.MUTE_TRUMPET, 				# 60 Muted Trumpet          = 40/44 Mute Trumpet
	PSR.HORN, 						# 61 French Horn            = 42/17 Horn
	PSR.BRASS_ENSEMBLE, 			# 62 Brass Section          = 44 Brass Ensemble - 92 Brass Ensemble 1
	PSR.SYNTH_BRASS_1, 				# 63 Synth Brass 1          = 00 Synth Brass 1
	PSR.SYNTH_BRASS_2, 				# 64 Synth Brass 2          = 82 Synth Brass 2
	# Reed			
	PSR.SAX, 						# 65 Soprano Sax            = 34 Saxophone 1    - 18 Sax
	PSR.SAX, 						# 66 Alto Sax               = 34 Saxophone 1    - 18 Sax
	PSR.SAXOPHONE_2, 				# 67 Tenor Sax              = 35 Saxophone 2    - 42 Alpenhorn
	PSR.SAXOPHONE_2, 				# 68 Baritone Sax           = 35 Saxophone 2    - 42 Alpenhorn
	PSR.OBOE, 						# 69 Oboe                   = 32/21 Oboe
	PSR.HORN, 						# 70 English Horn           = 42/17 Horn
	PSR.KAZOO, 						# 71 Bassoon                = 33 Basson         - 97 Kazoo
	PSR.CLARINET, 					# 72 Clarinet               = 31/19 Clarinet
	# Pipe
	PSR.FLUTE, 						# 73 Piccolo                = 28/20 Flute
	PSR.FLUTE, 						# 74 Flute                  = 28/20 Flute
	PSR.RECORDER, 					# 75 Recorder               = 30/88 Recorder
	PSR.PAN_FLUTE, 					# 76 Pan Flute              = 29/47 Pan Flute
	PSR.JUG, 						# 77 Blown Bottle           = 76 Soft Cloud		- 46 Jug
	PSR.JUG, 						# 78 Shakuhachi             = 76 Soft Cloud		- 46 Jug
	PSR.WHISTLE, 					# 79 Whistle                = 54/23 Whistle
	PSR.OCARINA, 					# 80 Ocarina                = 54 Whistle		- 89 Ocarina
	# Synth Lead
	PSR.WOOD_BASS_2, 				# 81 Lead 1 (square)        = 72 Synth Bass 1   - 81 Wood Bass 2
	PSR.SYNTH_BASS_1, 				# 82 Lead 2 (sawtooth)      = 73 Synth Bass 2   - 58 Synth Bass 1
	PSR.DAYBREAK, 					# 83 Lead 3 (calliope)      = 77 Daybreak       - 53 Harpischord 2
	PSR.JUG, 						# 84 Lead 4 (chiff)         = 76 Soft Cloud     - 46 Jug
	PSR.ROCK_GUITAR_3, 				# 85 Lead 5 (charang)       = 79 Arabesque      - 69 Rock Guitar 3
	PSR.HUMAN_CHORUS, 				# 86 Lead 6 (voice)         = 52 Human Vox      - 96 Human Chorus
	PSR.PEDAL_STEEL_GUITAR, 		# 87 Lead 7 (fifths)        = 89 Syntherimba    - 71 Pedal Stel Guitar
	PSR.BANDONEON, 					# 88 Lead 8 (bass + lead)   = 78 Sunbeam        - 56 Bandneon
	# Synth Pad
	PSR.ELECTRIC_PIANO_1, 			# 89 Pad 1 (new age)        = 03/05 Electric Piano
	PSR.SIN_WAVE, 					# 90 Pad 2 (warm)           = 81 Landscape      - 99 Sine Wave
	PSR.SYNTH_REED_2, 				# 91 Pad 3 (polysynth)      = 91 After Burner   - 85 Synth Reed 2
	PSR.HUMAN_VOICE_2, 				# 92 Pad 4 (choir)          = 53 Husky          - 95 Human Voice 2
	PSR.HAND_BELL, 					# 93 Pad 5 (bowed)          = 85 Glass Bell 2   - 63 Hand Bell
	PSR.SYNTH_REED_1, 				# 94 Pad 6 (metallic)       = 82 Metallic       - 45 Synth Reed
	PSR.GLASS_CELESTA, 				# 95 Pad 7 (halo)           = 90 African Percuss- 55 Glass Celesta
	PSR.DAYBREAK,	 				# 96 Pad 8 (sweep)          = 77 Daybreak       - 53 Harpiscord 2
	# Synth Effects (TODO)
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	# Ethnic
	PSR.SITAR,
	PSR.BANJO,
	PSR.SHAMISEN,
	PSR.KOTO,
	PSR.KALIMBA,
	PSR.BAGPIPE,
	PSR.VIOLIN_1,
	PSR.OBOE,
	# Percussive, (TODO)
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.STEEL_DRUM,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	# Sound Effects (TODO)
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1,
	PSR.PIANO_1
]

PercussionLUT = {
	35: PSR_Rhythm.BASS_DRUM_2, 	# 35 Bass Drum 2    -> 44 Low Bass Drum
	36: PSR_Rhythm.BASS_DRUM_1, 	# 36 Bass Drum 1    -> 45 Bass Drum
	38: PSR_Rhythm.SNARE_HI, 		# 38 Snare Drum 1   -> 49 Light Snare Drum
	39: PSR_Rhythm.HAND_CLAP, 		# 39 Hand Clap      -> 54 Claps
	40: PSR_Rhythm.SNARE_LO, 		# 40 Snare Drum 2   -> 52 Heavy Snare Drum
	41: PSR_Rhythm.LOW_TOM, 		# 41 Low Tom 2      -> 48 Low Tom
	42: PSR_Rhythm.HI_HAT_CLOSE, 	# 42 Closed Hi-hat  -> 48 Closed Hi-Hat
	43: PSR_Rhythm.BASS_TOM, 		# 43 Low Tom 1      -> 47 Bass Tom
	45: PSR_Rhythm.MID_TOM, 		# 45 Mid Tom 2      -> 50 Middle Tom
	46: PSR_Rhythm.HI_HAT_OPEN, 	# 46 Open Hi-hat    -> 59 Open Hi-Hat
	47: PSR_Rhythm.SYNTH_TOM_MID, 	# 47 Mid Tom 1      -> 42 Middle Synth Tom
	48: PSR_Rhythm.HI_TOM,			# 48 High Tom 2     -> 53 High Tom
	49: PSR_Rhythm.CRASH_CYMBAL, 	# 49 Crash Cymbal 1 -> 60 Crash Cymbal
	50: PSR_Rhythm.SYNTH_TOM_HI, 	# 50 High Tom 1     -> 43 High Synth Tom
	51: PSR_Rhythm.RIDE_CYMBAL, 	# 51 Ride Cymbal 1  -> 64 Ride Symbal
	
	54: PSR_Rhythm.TAMBOURINE,
	55: PSR_Rhythm.SPLASH_CYMBAL,

	60: PSR_Rhythm.BONGO_HI,
	61: PSR_Rhythm.BONGO_LOW,
	62: PSR_Rhythm.CONGA_HI_MUTE,
	63: PSR_Rhythm.CONGA_HI_OPEN,
	64: PSR_Rhythm.CONGA_LOW,
	65: PSR_Rhythm.TIMBALES_HIGH,
	66: PSR_Rhythm.TIMBALES_LOW,
	67: PSR_Rhythm.AGOGO_HI,
	68: PSR_Rhythm.AGOGO_LOW,
	69: PSR_Rhythm.SHAKER_CABASA,

	71: PSR_Rhythm.WHISTLE,
	
	75: PSR_Rhythm.CLAVES,

	78: PSR_Rhythm.CUICA_LOW,
	79: PSR_Rhythm.CUICA_HI,
	80: PSR_Rhythm.OPEN_TRIANGLE,
	81: PSR_Rhythm.CLOSED_TRIANGLE
}

channelsUsedByTracks = {}
max_velocity_per_channel = {ch: 0 for ch in range(16)}  # channels 0–15

# Load the MIDI file specified by the first command-line argument
mid = MidiFile(sys.argv[1])
#channelsToBoost = sys.argv[2].split(',')

# Iterate over tracks to find and remap instrument change messages
for i, track in enumerate(mid.tracks):
	track_id = str(i)
	channelsUsedByTracks[track_id] = set()

	print('Track {}: {}'.format(i, track.name))
	for msg in track:
		if msg.type == 'note_on':
			channelsUsedByTracks[track_id].add(msg.channel)
			if msg.velocity > max_velocity_per_channel[msg.channel]:
				max_velocity_per_channel[msg.channel] = msg.velocity
			#if (msg.channel in channelsToBoost):
			#msg.velocity = min(msg.velocity*3,127)
		# Apparently the PSR-4500 ignores note_off commands
		if msg.type == 'note_off':
			msg.velocity = 0
		
		# Sound priority
		#if msg.type == 'note_on':
		#	# Throttle: avoid overlapping same note
		#	if msg.note in active_notes and msg.velocity > 0:
		#		continue  # skip duplicate
		#	elif msg.velocity == 0:
		#		active_notes.discard(msg.note)
		#	else:
		#		active_notes.add(msg.note)
		
		# Percussion Channel Translation
		if msg.type in ('note_on') and msg.channel == 9:  # Channel 10 (0-indexed)
			if msg.note in PercussionLUT:
				#print(f'Remapping percussion note {msg.note} to {PercussionLUT[msg.note]}')
				msg.note = PercussionLUT[msg.note].value  # Remap the note number
			else:
				# Workaround while some sounds aren't accounted for
				msg.note = 38
		
		# Instrument Conversion
		if msg.type == 'program_change':  # Look for instrument change events
			if (msg.program < len(InstrumentLUT)):
				print(f'{msg.channel}: Remapping instrument from {GM(msg.program+1).name} to {InstrumentLUT[msg.program].name}')
				msg.program = InstrumentLUT[msg.program].value  # Change instrument
			else:
				print(f'{msg.channel}: Unknown instrument {GM(msg.program+1).name}, assigning Piano')
				msg.program = PSR.PIANO_1.value

for track_id, channels in channelsUsedByTracks.items():
	print(f'Track {track_id} uses channels: {sorted(channels)}')
for ch in range(16):
	print(f'Channel {ch}: Max velocity = {max_velocity_per_channel[ch]}')
# Save the modified MIDI file
mid.save(os.path.basename(sys.argv[1]))
