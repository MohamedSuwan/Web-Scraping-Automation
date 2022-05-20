import datetime
# from threading import Timer
from datetime import datetime
import pyautogui as gu
# x=datetime.today()
# y=x.replace(microsecond=50)
# delta_t=y-x
# secs=delta_t.seconds+1
# do something every ten seconds
def recur():
    
    while 1:
        x=((datetime.now()))
        print(x.strftime("%d %b %Y   %H:%M:%S"))
        gu.sleep(1)
        sec=[i for i in range(0,60,10)]
        if x.second in sec:
            print(f"Do something at seconds {sec} of each minute as long as the program is running")
            recur()
recur()
# t=Timer(secs,bomb)
# t.start()
# print(datetime.date.month())
