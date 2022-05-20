import pyautogui as gu
# search for image and click it
# gu.scroll(200,350,200,700) no ides how this works
gu.click(gu.locateOnScreen("/home/roy/Pictures/music1.png"),duration=(.2))
# gu.click(165,750,duration =0.2)# icon
gu.sleep(1.1)# untill this fucker boots
# gu.click(670,690,duration =0.2)#play
if gu.locateOnScreen("/home/roy/Pictures/play.png"):
    gu.click(gu.locateOnScreen("/home/roy/Pictures/play.png"))
    
else:
    gu.click(gu.locateOnScreen("/home/roy/Pictures/pause.png"),duration=(.2))
gu.click(gu.locateOnScreen("/home/roy/Pictures/mini.png"),duration=(.2))
# gu.click(1247,35,duration =0.2)#minimize
# gu.moveTo(650,350,)

