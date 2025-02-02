import cv2
import numpy as np
import pyautogui
import pytesseract
import time
import pyttsx3

# Path to Tesseract-OCR executable, downloaded from https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Constants should be in UPPERCASE
INTERVAL = 5  # seconds between readings
SCREEN_REGION = (0, 0, 90, 40)  # top left corner (x, y, w, h)
MIN_FPS = 1
MAX_FPS = 1000

# Initialize TTS settings
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 135)  # words per minute
tts_engine.setProperty('volume', 0.5)  # Volume (0 to 1)

def main():
    while True:
        start_time = time.time()

        # Capture screen
        screenshot = pyautogui.screenshot(region=SCREEN_REGION)

        # Convert to grayscale
        image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # Perform OCR
        fps_text = pytesseract.image_to_string(image, config='--psm 6')

        # Extract FPS (filter out non-numeric values)
        fps = ''.join(filter(str.isdigit, fps_text))

        try:
            fps = int(fps)
            if MIN_FPS < fps < MAX_FPS:
                tts_engine.say(f"You have {fps} fps.")
                tts_engine.runAndWait()
        except ValueError:
            pass

        # Sleep for the remaining time
        elapsed_time = time.time() - start_time
        sleep_time = max(0, INTERVAL - elapsed_time)
        time.sleep(sleep_time)

if __name__ == '__main__':
    main()
