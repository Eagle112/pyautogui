import pyautogui as pgui
import pyperclip

cmdStr = ['cd webroot/static && npx grunt devwatch','cd webroot/static && npx webpack -w']

pgui.hotkey('command',' ')
pgui.press('delete')
pgui.press(['i','c','o','enter'])
pgui.click(744,938)
pgui.hotkey('command','\\')

pgui.click(250,948)
pyperclip.copy(cmdStr[0]); pgui.hotkey('command','v'); pgui.press('enter')

pgui.click(1179,855)
pyperclip.copy(cmdStr[1]); pgui.hotkey('command','v'); pgui.press('enter')

# im1 = pgui.screenshot('part.png',region=(1046,1031,42,51))
# im2 = pgui.screenshot('my_screenshot.png')
# button7location = pgui.locateAllOnScreen('part.png', grayscale=False, confidence=0.8)
