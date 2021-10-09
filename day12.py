#买蛋糕

from threading import Thread
import time

cake = 0  # 蛋糕
money = 300  # 钱
# 厨师类
class cher(Thread):
    def run(self) -> None:
        global money
        global cake
        while True:
            if cake == 200:
                time.sleep(3)
            if cake < 200:
                cake += 3
            print("还有",cake,"个蛋糕")
            if money == 0:
                break

# 顾客
class client(Thread):
    name = ""
    count = 0
    def run(self) -> None:
        global money
        global cake
        while money >= 2:
            if cake > 0:
                money -= 2
                cake -= 1
                self.count = self.count + 1
                # print()
            elif cake == 0:
                time.sleep(3)
            print(self.name,"总共抢了",self.count,"个,还剩",money,"元")
A1 = cher()
A2 = cher()
A3 = cher()

B1 = client()
B2 = client()
B3 = client()
B4 = client()
B5 = client()
B6 = client()

B1.name = "小明"
B2.name = "小红"
B3.name = "小刚"
B4.name = "小绿"
B5.name = "小蓝"
B6.name = "小黑"


A1.start()
A2.start()
A3.start()
B1.start()
B2.start()
B3.start()
B4.start()
B5.start()
B6.start()

