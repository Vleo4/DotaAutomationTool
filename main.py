import pyautogui
import cv2
import numpy as np
import time


def locate_and_click_element_by_image(image_path, confidence=0.6):
    try:
        # Read the button image and convert to grayscale
        button_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        button_height, button_width = button_image.shape[:2]

        # Take a screenshot and convert to grayscale
        screenshot = pyautogui.screenshot()

        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence:
            print(f"Button found with confidence {max_val:.2f}")

            center_x = max_loc[0] + button_width // 2
            center_y = max_loc[1] + button_height // 2

            pyautogui.moveTo(center_x, center_y)
            pyautogui.click()
            print("Button clicked!")
            return True
        else:
            print("Button not found.")
            return False
    except pyautogui.ImageNotFoundException:
        print("Button image not found on the screen.")
        return False
    except cv2.error as e:
        print(f"OpenCV error: {e}")
        return False

def locate_by_image(image_path, confidence=0.6):
    try:
        # Read the button image and convert to grayscale
        button_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Take a screenshot and convert to grayscale
        screenshot = pyautogui.screenshot()

        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence:
            print(f"Image found with confidence {max_val:.2f}")
            print("Image clicked!")
            return True
        else:
            print("Image not found.")
            return False
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen.")
        return False
    except cv2.error as e:
        print(f"OpenCV error: {e}")
        return False


def locate_hero(hero_name):
    try:
        pyautogui.write(hero_name)
        pyautogui.press('enter')
        print(f"Typed {hero_name} and enter.")

        for _ in range(len(hero_name)):
            pyautogui.press('backspace')
    except Exception as e:
        print(f"An error occurred: {e}")

def check_game_acceptance():
    image_path = f'static/before_pick.png'
    return locate_by_image(image_path=image_path, confidence=0.7)

def accept_game(language):
    image_path = f'static/accept_button_{language}.png'
    while True:
        locate_and_click_element_by_image(image_path=image_path, confidence=0.6)
        if check_game_acceptance():
            break
        time.sleep(1)

def check_hero_pick():
    image_path = f'static/after_pick.png'
    return locate_by_image(image_path=image_path, confidence=0.7)

def pick_hero():
    image_path = f'static/pick_hero_button.png'
    while True:
        # Set full name of your preferred hero
        locate_hero("pudge")
        locate_and_click_element_by_image(image_path=image_path, confidence=0.7)
        if check_hero_pick():
            break


if __name__ == "__main__":
    # Dota language (Ukrainian/English)
    accept_game(language="ukr")
    pick_hero()
