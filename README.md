# Miss FPS ("Fröken FPS")

This is an audi-based FPS counter. I'm not sure why anyone would need it, but it exists.
The name is a play of "Fröken Ur" (Miss Time) - https://www.ri.se/en/expertise-areas/services/froken-ur - a Swedish phone service you could call to have the current time read to you.

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

### Steam Overlay or similar FPS counter
The code reads the FPS counter visible on the screen. Screen region is configured for 1440p with steam overlay in the top left corner by default, but should work or be adjustable to fit most fps counters.

### OS
As long as Tesseract is supported, it should run on most OSes, but it's currently only tested on Windows.
