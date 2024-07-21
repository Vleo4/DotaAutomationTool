import pyautogui
import cv2
import numpy as np
import time


def locate_and_click_button(lang, confidence=0.6):
    try:
        image_path = f'accept_button_{lang}.png'

        # Read the button image and convert to grayscale
        button_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        button_height, button_width = button_image.shape[:2]

        # Take a screenshot and convert to grayscale
        screenshot = pyautogui.screenshot()

        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # Match the template
        result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Check if confidence is above threshold
        if max_val >= confidence:
            print(f"Button found with confidence {max_val:.2f}")
            # Get the center of the button
            center_x = max_loc[0] + button_width // 2
            center_y = max_loc[1] + button_height // 2
            # Move the mouse to the button and click it
            pyautogui.moveTo(center_x, center_y)
            pyautogui.click()
            print("Button clicked!")
        else:
            print("Button not found.")
    except pyautogui.ImageNotFoundException:
        print("Button image not found on the screen.")
    except cv2.error as e:
        print(f"OpenCV error: {e}")


if __name__ == "__main__":
    # Dota language (Ukrainian/English)
    language = 'ukr'

    while True:
        locate_and_click_button(language)
        time.sleep(2)