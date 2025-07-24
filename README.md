# GM-to-PSR4500
 A python script to turn a General Midi-compliant Midi into one that a Yamaha PSR-4500 can play back correctly

# How to use
## Setup
1. Connect a Computer to the Midi input of the Yamaha PSR-4500
2. Power the Keyboard up
3. Hold the MIDI Button down
4. Press VOICE SELECT number "0" to put the Keyboard into Standard Voice Mode
5. Press VOICE SELECT number "9" to set which Channel is the Rhymth Channel
6. Press Key A1 to select voice 10 (though this can vary on some Midi Tracks)

For more info, consult the Yamaha PSR-4500 Manual.

## Converting the file
Simply run the Python file with the path to the desired midi after it
```bash
python3 ./gm2psr4500.py midis/test.mid
```
This will place the converted file into the directory where the Python file is.

## Playing the file back
First need to determine the port that your Keyboard is accessible through, which can be found out via `aconnect` on Linux.
```bash
aconnect -l
```

Then you can simply use `aplaymidi` to play the file back.

```bash
aplaymidi -p [port] test.mid
```

## Adding more instruments
**Important Note**: LMMS and the official General Midi spec indexes it's Midi Instruments with 1, while the PSR-4500 and most code interacting with the data start at 0!

The formatting I've tried to maintain in the code is laid out as follows.
```
New instrument number, # (GM Instrument) =  (PSR-4500 Name) - (Midi In/Out Name)
```
This way it can easily be found out what instrument maps to what else.