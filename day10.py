
# # 水杯
# class cup:
#     __high = 0
#     __volume = 0
#     __color = ""
#     __texture = ""
#
#     def sethigh(self,high):
#         if high >= 15:
#             self.__high = high
#         else:
#             print("别瞎输")
#
#     def gethigh(self):
#         return self.__high
#
#     def setvolume(self,volume):
#         if volume > 100:
#             self.__volume = volume
#         else:
#             print("别瞎弄")
#
#     def get__volume(self):
#         return self.__volume
#
#     def setcolor(self,color):
#         self.__color = color
#
#     def getcolor(self):
#         return self.__color
#
#     def settexture(self,texture):
#         self.__texture = texture
#
#     def gettexture(self):
#         return self.__texture
#
#
#     def showcup(self):
#         print("一个高度",self.__high,"厘米",self.__color,self.__texture,"材质的水杯,可以存放",self.__volume,"毫升的液体")
#
#
# a = cup()
# a.setcolor("粉色")
# a.settexture("玻璃")
# a.sethigh(25)     #高度
# a.setvolume(500)  #存放液体
#
# a.showcup()
#
#
#
# #笔记本电脑
#
# class computer:
#     __screen = 0  #屏幕
#     __money = 0  #价格
#     __cpu = ""   #cpu型号
#     __memory = 0 #内存
#     __waiting = 0 #待机时长
#
#     def setscreen(self,screen):
#         if screen >= 14.5:
#             self.__screen = screen
#         else:
#             print("别瞎弄")
#
#     def getscreen(self):
#         return self.__screen
#
#     def setmoney(self,money):
#         if money >= 5000:
#             self.__money = money
#         else:
#             print("这么便宜谁卖给你？")
#
#     def getmoney(self):
#         return self.__money
#
#     def setcpu(self,cpu):
#         self.__cpu = cpu
#
#     def getcpu(self):
#         return self.__cpu
#
#     def setmemory(self,memory):
#         if memory >= 512:
#             self.__memory = memory
#         else:
#             print("没那么小的")
#
#     def getmemory(self):
#         return self.__memory
#
#     def setwaiting(self,waiting):
#         if waiting >= 24:
#             self.__waiting = waiting
#         else:
#             pring("太垃圾了不买")
#
#     def getwaiting(self):
#         return self.__waiting
#
#     def showcomputer(self):
#         print("一台屏幕",self.__screen,"寸的电脑，价值",self.__money,"元,cpu型号为",self.__cpu,",内存有",self.__memory,"g,更有超长待机，长达",self.__waiting,"小时,您可以放心打字、玩游戏、看视频")
#
#
#
# b = computer()
# b.setscreen(20)
# b.setmoney(10000)
#
# b.setcpu(3080)
# b.setmemory(10024)
# b.setwaiting(48)
#
# b.showcomputer()
#
#
#
#
#
#
# # 车
# class car:
#     __model = ""  #型号
#     __num = 0     #车轮
#     __color = ""  #颜色
#     __weight = 0  #重量
#     __diesel = 0  #油箱
#     __name = ""   #品牌
#     __speed = 0   #加速
#
#
#     def setmodel(self,model):
#         self.__model = model
#
#     def getmodel(self):
#         return self.__model
#
#     def setnum(self,num):
#         if num <= 3:
#             print("没有这种型号的车子")
#         else:
#             self.__num = num
#
#     def getnum(self):
#         return self.__num
#
#
#     def setcolor(self,color):
#         self.__color = color
#
#     def getcolor(self):
#         return self.__color
#
#     def setweight(self,weight):
#         if weight <= 1000:
#             print("没有这么轻的车子")
#         else:
#             self.__weight = weight
#
#     def getweight(self):
#         return self.__weight
#
#     def setdiesel(self,diesel):
#         if diesel <= 50:
#             print("油箱太小了")
#         else:
#             self.__diesel = diesel
#
#     def getdiesel(self):
#         return self.__diesel
#
#     def setname(self,name):
#         self.__name = name
#
#     def getname(self):
#         return self.__name
#
#
#     def setspeed(self,speed):
#         if speed <= 0:
#             print("这是什么车？")
#         else:
#             self.__speed = speed
#
#     def getspeed(self):
#         return self.__speed
#
#     def showcar(self):
#         print("这辆",self.__color,("的"),self.__name,self.__model,"有",self.__num,"个轮子,车身重量为",self.__weight,"Kg,油箱最多可以存储",self.__diesel,"升柴油,百米加速仅需",self.__speed,"秒")
#
#
#
# c = car()
# c.setnum(4)
# c.setname("法拉利")
# c.setspeed(1)
# c.setdiesel(55)
# c.setweight(1200)
# c.setmodel(488)
# c.setcolor("红色")
#
# c.showcar()



# 猴子
class monkey:
    __sort = ""   #类别
    __gender = "" #性别
    __color = ""  #颜色
    __weight = 0  #体重

    def setsort(self,sort):
        self.__sort = sort

    def getsotr(self):
        return self.__sort

    def setgender(self,gender):
        if gender == "雄" or gender == "雌":
            self.__gender = gender

    def getgender(self):
        return self.__gender


    def setcolor(self,color):
        self.__color = color

    def getcolor(self):
        return self.__color


    def setweight(self,weight):
        if weight <= 0 or weight >=1000:
            print("这不符合常理")
        else:
            self.__weight = weight

    def getweight(self):
        return self.__color

    def setstudy(self,study):
        print("一只",self.__gender,"性",self.__sort,"体重可达",self.__weight,"Kg,它现在正在用",study,"取火")


    # def showM(self):
    #     print("一只",self.__gender,"性",self.__sort,"体重可达",self.__weight,"Kg,它现在正在用",study,"取火")


k = monkey()
k.setgender("雄")
k.setcolor("金色")
k.setsort("金丝猴")
k.setweight(75)
k.setstudy("石头")


# 打电话
# class people:
#     __name = ""         #姓名
#     __gender = ""       #性别
#     __age = 0           #年龄
#     __money = 0         #剩余话费
#     __brand = ""        #手机品牌
#     __cell = 0          #电池容量
#     __screen = 0        #手机屏幕
#     __wait = 0          #待机时长
#     __integral = 0      #积分
#
#
#     def setname(self,name):
#         self.__name = name
#
#     def getname(self):
#         return self.__name
#
#     def setgender(self,gender):
#         self.__gender = gender
#
#     def getgender(self):
#         return self.__gender
#
#     def setage(self,age):
#         if age >120 or age <= 0:
#             print("年龄非法")
#         else:
#             self.__age = age
#
#     def getage(self):
#         return self.__age
#
#
#     def setmoney(self,money):
#         self.__money = money
#
#     def getmoney(self):
#         return self.__money
#
#
#     def setbrand(self,brand):
#         self.__brand = brand
#
#     def getbrand(self):
#         return self.__brand
#
#
#     def setcell(self,cell):
#         if cell <= 1000:
#             print("电池容量太小了")
#         else:
#             self.__cell = cell
#
#     def getcell(self):
#         return self.__cell
#
#
#     def setscreen(self,screen):
#         if screen <= 1:
#             print("手机屏幕太小了")
#         else:
#             self.__screen = screen
#
#     def getscreen(self):
#         return self.__screen
#
#     def setwait(self,wait):
#         if wait <= 8:
#             print("什么破手机？")
#         else:
#             self.__wait = wait
#
#     def getwait(self):
#         return self.__wait
#
#
#     def setintegral(self,integral):
#         if integral <= 0:
#             print("很抱歉，您没有积分")
#         else:
#             self.__integral = integral
#
#     def getintegral(self):
#         return self.__integral
#
#
#     def showphone(self):
#         print("姓名:",self.__name,"性别:",self.__gender,"年龄:",self.__age,"岁,您的剩余话费为:",self.__money,"元,您的手机品牌是:",
#               self.__brand,"电池容量为:",self.__cell,"毫安,手机屏幕为",self.__screen,"寸,手机最大待机时长为:",self.__wait,
#               "年,您所拥有的积分还剩",self.__integral,"分")
#
#
# j = people()
# j.setname(input("请输入姓名"))
# j.setgender(input("请输入性别"))
# j.setage(int(input("请输入年龄")))
# j.setmoney(float(input("请输入剩余话费")))
# j.setbrand(input("请输入手机品牌"))
# j.setcell(float(input("请输入电池容量")))
# j.setscreen(float(input("请输入手机尺寸")))
# j.setwait(int(input("请输入手机最大待机时长")))
# j.setintegral(int(input("请输入所剩积分")))
#
# j.showphone()













