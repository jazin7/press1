import cv2
import numpy as np
import pyautogui
import time
import os

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def detect_image(screen, template, threshold):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val >= threshold

# script runs in same directory as the image
os.chdir(os.path.dirname(__file__))


image_path = "image.png"
template = cv2.imread(image_path, cv2.IMREAD_COLOR)
if template is None:
    raise FileNotFoundError(f"Template image not found: {image_path}")

# Detection threshold
threshold = 0.85

while True:
    screen = capture_screen()

    # Detect the image
    if detect_image(screen, template, threshold):
        print("Image detected on main monitor. Pressing 1.")
        pyautogui.press("1")

    time.sleep(0.1) 