class People:
    age = 0
    gender = ""
    name = ""

class worker(People):
    def working(self):
        print("一名", self.age, "岁的", self.gender, "性工人名叫", self.name, "他正在努力干活")

class student(People):
    STUnumber=""
    def study(self,number):
        self.STUnumber=number
        print("一名学号为",self.STUnumber,"的",self.gender,"生学生名叫",self.name,"他的年龄为",self.age,"开始学习")

    def sing(self):
        print("一名学号为",self.STUnumber,"的",self.gender,"生学生名叫",self.name,"他的年龄为",self.age,"正在唱歌")




# a = worker()
# a.age = (int(input("请输入年龄")))
# a.gender = (input("请输入性别"))
# a.name = (input("请输入姓名"))
# a.working()

b = student()
b.name = input("请输入姓名")
b.gender = input("请输入性别")
b.age = int(input("请输入年龄"))
b.study(input("请输入学号："))
b.sing()





