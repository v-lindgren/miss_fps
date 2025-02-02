# Miss FPS ("Fröken FPS")

This is an audio-based FPS counter, which will read your current FPS to you every 5 seconds. I'm not sure why anyone would want it, but now it exists.

The name is a play on "Fröken Ur" (Miss Time) - https://www.ri.se/en/expertise-areas/services/froken-ur - a Swedish phone service you could call to have the current time read to you.

## Installation

1. Install the python requirements:

```powershell
py -m pip install requirements.txt
```

2. Download Tesseract from https://github.com/UB-Mannheim/tesseract/wiki and install it. Ensure that the tesseract_cmd variable in the code points to the correct path. 

3. Start it by running:

```powershell
py miss_fps.py
```

## Requirements

### FPS Counter
The code reads the FPS counter visible on the screen, so it can support any game or overlay that displays an FPS counter. Screen region is configured for 1440p with steam overlay in the top left corner by default, but should work with or be adjustable to fit any fps counter.

### OS
As long as Tesseract is supported, and pyttsx3 has a voice to use it should run on most OSes, but it's currently only tested on Windows.
