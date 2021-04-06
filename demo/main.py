import pyautogui
# document url https://pyautogui.readthedocs.io/en/latest/quickstart.html
print(pyautogui.position())# current mouse x and y
print(pyautogui.size())# current screen resolution width and height
print(pyautogui.onScreen(10000, 20)) # True if x & y are within the screen.
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2.5
pyautogui.moveTo(10, 10, duration=2)

pyautogui.moveRel(20, 20, duration=2)