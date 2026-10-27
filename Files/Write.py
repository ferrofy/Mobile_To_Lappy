import pyautogui

def Write_Text(Text):
    for Letter in Text:
        pyautogui.write(Letter)