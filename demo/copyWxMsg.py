import pyautogui,pyperclip,time,json
import platform

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

COPY_TMP1=''
if platform.platform().index('Windows')!=-1:
  commandOrctrl = 'ctrl'
else:
  commandOrctrl = 'command'


def paste():
  pyautogui.hotkey(commandOrctrl,'v')

def copy():
  pyautogui.hotkey(commandOrctrl,'c')

def enter():
  pyautogui.press('enter')
  
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
  global COPY_TMP1
  pyautogui.click(410,480,clicks=2)
  copy()
  COPY_TMP2 = pyperclip.paste()
  print(COPY_TMP2 )
  if COPY_TMP2 != COPY_TMP1:
    COPY_TMP1 = COPY_TMP2
    pyautogui.click(350,570)
    paste()
  # enter()

chooseUser('古惑仔')
while(True):
  time.sleep(1)
  copyLastMsg()