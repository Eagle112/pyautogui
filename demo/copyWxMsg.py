import pyautogui,pyperclip,time,json
import platform

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

if platform.platform().index('Windows')!=-1:
  commandOrctrl = 'ctrl'
else:
  commandOrctrl = 'command'


def paste():
  pyautogui.hotkey(commandOrctrl,'v')

def copy():
  pyautogui.hotkey(commandOrctrl,'c')

def chooseUser(name):
  # while()
  pyautogui.click(339,1061)
  pyautogui.click(102,37,duration=0.3) 
  pyperclip.copy(name)
  paste()
  pyautogui.hotkey('enter')

def copyLastMsg():
  # pyautogui.moveTo(x=408,y=487,duration=0.3)
  # time.sleep(2)
  pyautogui.click(410,480,clicks=2)
  copy()
  pyautogui.click(350,570)

chooseUser('古惑仔')
copyLastMsg()