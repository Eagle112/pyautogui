import pyautogui
import cv2
# document url https://pyautogui.readthedocs.io/en/latest/quickstart.html
# TK_SILENCE_DEPRECATION=1
# print(pyautogui.position())# current mouse x and y
# print(pyautogui.size())# current screen resolution width and height
# print(pyautogui.onScreen(10000, 20)) # True if x & y are within the screen.
# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 1
# pyautogui.moveTo(10, 10,0)

# pyautogui.moveRel(20,200,0)
# pyautogui.dragRel(20, 20,1,button='left')  # drag mouse to XY
# pyautogui.scroll(10)
# pyautogui.alert(text='123', title='123', button='OK')
button7location = pyautogui.locateOnScreen('123.png', grayscale=False,confidence=0.7)
print(button7location)