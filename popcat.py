import pyautogui
# import mouse
import time
a=time.time()
pyautogui.pause=0.005
for i in range (4000):
    # mouse.click("left")
    pyautogui.click()

print(time.time()-a)