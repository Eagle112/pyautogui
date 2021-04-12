import pyautogui,pyperclip,time,json
import platform
import sys 
import win32gui,win32con

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3
print('屏幕分辨率:',pyautogui.size())

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
  pyautogui.click(339,1061)
  pyautogui.click(102,37,duration=0.3) 
  pyperclip.copy(name)
  paste()
  pyperclip.copy('')
  time.sleep(1)
  pyautogui.hotkey('enter')

def copyLastMsg():
  lastMsgX = 418; lastMsgY = 465
  if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == '微信':
    # print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    global COPY_TMP1
    # 移到最后一条消息
    pyautogui.moveTo(lastMsgX,lastMsgY)
    pyautogui.click(button='right')
    # 如果可以复制
    if pyautogui.pixelMatchesColor(lastMsgX+28,lastMsgY+10,(0,0,0)):
      pyautogui.move(32,12)
      pyautogui.click()
      COPY_TMP2 = pyperclip.paste()
      # win32gui.ShowWindow(2163398,win32con.SW_SHOWNORMAL)
      # print(COPY_TMP2)
      if COPY_TMP2 != COPY_TMP1:
        COPY_TMP1 = COPY_TMP2
        pyautogui.click(350,570)
        paste()
        enter()
  else:
    sys.exit(0)
  

chooseUser('古惑仔')
while(True):
  # time.sleep(1)
  copyLastMsg()
