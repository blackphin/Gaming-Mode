import pyautogui,time,subprocess,os
pyautogui.FAILSAFE=False

#Close Useless Softwares

subprocess.Popen(["D:\Program Files (x86)\Gaming-Mode\Files\Gaming Mode.bat"])
time.sleep(7)

#OC CPU

pyautogui.press("win")
time.sleep(0.5)
pyautogui.write(message="dragon center")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(16)
pyautogui.click(x=673, y=441)
time.sleep(10)
pyautogui.click(x=1671, y=112)
time.sleep(1)

#Change Mouse Profile

os.startfile("D:\Program Files (x86)\Gaming Mouse\Monitor.exe")
time.sleep(1)
pyautogui.doubleClick(x=1655, y=1053) #1610
time.sleep(2)
pyautogui.click(x=1024, y=860)
time.sleep(1)
pyautogui.moveTo(x=505, y=822)
time.sleep(0.5)
pyautogui.click()
time.sleep(1)

#Change Resolution

pyautogui.press("win")
time.sleep(0.5)
pyautogui.click(x=29, y=940)
time.sleep(0.5)
pyautogui.click(x=278, y=312)
time.sleep(0.5)
pyautogui.click(x=607, y=791)
time.sleep(0.5)
pyautogui.click(x=598, y=873)
time.sleep(0.5)
pyautogui.click(x=999, y=473)
time.sleep(0.5)
pyautogui.click(x=26, y=16)
time.sleep(0.5)

#Hide Task bar

pyautogui.click(x=303, y=443)
time.sleep(1)
pyautogui.click(x=190, y=644)
time.sleep(1)
pyautogui.click(x=460, y=263)
time.sleep(1)
pyautogui.hotkey("alt","f4")

#Open CS:GO

os.startfile("steam://rungameid/730")
time.sleep(30)

#Change In-Game Resolution

pyautogui.click(x=40,y=475)
time.sleep(0.5)
pyautogui.click(x=136,y=140)
time.sleep(0.5)
pyautogui.click(x=1081,y=503)
time.sleep(0.5)
pyautogui.click(x=1078,y=589)
time.sleep(0.5)
pyautogui.click(x=1391,y=884)

#Change Game Mode to Competitive

time.sleep(2)
pyautogui.click(x=98,y=156)
time.sleep(0.5)
pyautogui.click(x=204, y=198)