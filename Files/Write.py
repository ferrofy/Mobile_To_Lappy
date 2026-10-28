import pyautogui
from time import sleep as Wait

# 5 Sec Wait Before Start

print("Printing Some Text In 5 Sec...")
Wait(5)
print("Started...")

def Write_Text(Text):
    for Letter in Text:
        pyautogui.write(Letter)