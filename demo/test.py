import pyautogui
from cycleLinkList import *

ll = SinCycLinkedlist()
ll.add('古惑仔')
ll.add('李伟昂')
cur = ll._head
while(True):
    print(cur.item)
    cur = cur.next