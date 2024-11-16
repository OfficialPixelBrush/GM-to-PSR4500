# GM-to-PSR4500
 A python script to turn a General Midi-compliant Midi into one that a Yamaha PSR-4500 can play back correctly

# How to use
## Setup
1. Connect a Computer to the Midi input of the Yamaha PSR-4500
2. Power the Keyboard up
3. Hold the MIDI Button down
4. Press VOICE SELECT number "0" to put the Keyboard into Standard Voice Mode
5. Press VOICE SELECT number "9" to set which Channel is the Rhymth Channel
6. Press Key E1 to select voice 10 (though this can vary on some Midi Tracks)

For more info, consult the Yamaha PSR-4500 Manual.

## Converting the file
Simply run the Python file with the path to the desired midi after it
```bash
python3 ./gm2psr4500.py midis/test.mid
```
This will place the converted file into the directory where the Python file is.

## Playing the file back
First need to determine the port that your Keyboard is accessibly through, which can be found out via `aconnect` on Linux.
```bash
aconnect -l
```

Then you can simply use `aplaymidi` to play the file back.

```bash
aplaymidi -p [port] test.mid
```