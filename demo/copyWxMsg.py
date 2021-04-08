import pyautogui,cv2,pyperclip,time,json

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

def paste():
  pyautogui.hotkey('command','v')

def chooseUser(name):
  # while()
  pyautogui.click(1172,1055)
  pyautogui.click(100,54,duration=0.3) 
  pyperclip.copy(name)
  paste()
  pyautogui.hotkey('enter')

def copyLastMsg():
  # pyautogui.moveTo(x=408,y=487,duration=0.3)
  # time.sleep(2)
  pyautogui.click()
  pyautogui.click()
  pyautogui.mouseDown()

# chooseUser('此用户已成仙')
copyLastMsg()