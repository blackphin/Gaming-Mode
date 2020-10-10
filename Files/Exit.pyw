import pyautogui,time
pyautogui.FAILSAFE=False

#Change Resolution

pyautogui.press("win")
time.sleep(0.5)
pyautogui.click(21, 604)
time.sleep(0.5)
pyautogui.click(x=237,y=246)
time.sleep(0.5)
pyautogui.click(x=480,y=632)
time.sleep(0.5)
pyautogui.click(x=480,y=249)
time.sleep(0.5)
pyautogui.click(x=922,y=471)
time.sleep(0.5)
pyautogui.click(x=29,y=18)
time.sleep(0.5)

#Show Task bar

pyautogui.click(x=1303, y=250)
time.sleep(1)
pyautogui.click(x=158, y=519)
time.sleep(1)
pyautogui.click(x=366, y=214)
time.sleep(0.5)
pyautogui.hotkey("alt","f4")
time.sleep(1)

#Normalize CPU

'''pyautogui.doubleClick(x=1640, y=1053) #1685
# time.sleep(1)
# pyautogui.click(x=830, y=1053)
time.sleep(12)
pyautogui.click(x=1208, y=351)
time.sleep(10)
pyautogui.click(x=1671, y=112)
time.sleep(1)

#Change Mouse Profile

os.startfile("D:\Program Files (x86)\Gaming Mouse\Monitor.exe")
time.sleep(0.5)
pyautogui.doubleClick(x=1610, y=1053) #1655
time.sleep(2)
pyautogui.click(x=1272, y=860)
time.sleep(1)
pyautogui.moveTo(x=1671, y=20)
time.sleep(0.5)
pyautogui.click()'''