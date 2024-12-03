import os
import pyautogui

EXPRESSION = "12+7="

buttons = {
    '1': 'button_1.png',
    '2': 'button_2.png',
    '+': 'button_plus.png',
    '7': 'button_7.png',
    '=': 'button_equals.png'
}

os.system("open -a Calculator")

pyautogui.PAUSE = 1


def click_button(button_image: str):
    try:
        # Находим центр кнопки и кликаем по нему
        pyautogui.click(
            pyautogui.locateCenterOnScreen(
                f'images/{button_image}', confidence=0.9))
    except pyautogui.ImageNotFoundException:
        print(f"Button {button_image} not found")


if __name__ == "__main__":
    for char in EXPRESSION:
        click_button(buttons[char])
