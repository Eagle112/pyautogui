import pyautogui,cv2,pyperclip,time,json
from weather import *

# document url https://pyautogui.readthedocs.io/en/latest/quickstart.html
# TK_SILENCE_DEPRECATION=1
# print(pyautogui.position())# current mouse x and y
# print(pyautogui.size())# current screen resolution width and height
# print(pyautogui.onScreen(10000, 20)) # True if x & y are within the screen.
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5
# pyautogui.moveTo(10, 10,0)

# pyautogui.moveRel(20,200,0)
# pyautogui.dragRel(20, 20,1,button='left')  # drag mouse to XY
# pyautogui.scroll(10)
# pyautogui.alert(text='123', title='123', button='OK')
# button7location = pyautogui.locateOnScreen('123.png', grayscale=False,confidence=0.7)
def paste():
  pyautogui.hotkey('command','v')

def postMsg(name,city):
  wea7days = getWeather('北京')
  [day1,day2] = [wea7days[0].string,wea7days[1].string]
  info = city + '天气:'+day1+',明天:'+day2
  pyautogui.click(1215,1055)
  pyautogui.click(100,54,duration=0.3)  
  pyperclip.copy(name)
  paste()
  pyautogui.hotkey('enter')
  pyperclip.copy(info)
  paste()

# postMsg('古惑仔','北京')
print(type(pyperclip.paste()))





