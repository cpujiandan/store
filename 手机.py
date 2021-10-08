'''
    老手机：
        打电话：手机号，彩铃
    新手机：
        打电话：手机号，彩铃，归属地，大头贴，录音
'''
import time
class OldPhone:
    phoneNumber = ""
    voice = ""

    def call(self,number):
        print(self.phoneNumber,"正在打电话，打给：",number,"正在响铃：",self.voice)
        for i  in range(8):
            print(".",end="")
            time.sleep(1)
        print("对方已接通！！")

class NewPhone(OldPhone):
    # 归属地，大头贴，录音
    address = ""
    picture = ""
    mic = False

    def call(self,number):
        # 2个属性由老手机代码显示
        super().call(number)

        # 3个新属性由新手机自己显示
        self.mic = True
        print("本机归属地：",self.address,"，对方大头贴为：",self.picture,",已经开启了录音功能！")
        for i in range(8):
            print(".",end="")
            time.sleep(1)
        print("本次通话完成[5:36]！")


phone = NewPhone()
phone.phoneNumber = "13552648187"
phone.voice = "江南style"
phone.picture = "野猪佩奇"
phone.address = "北京移动"

# phone.call("13379854676")

class People:
    age = 0
    sex = None
    name = ""

class Worker(People):
    def work(self):
        print(self.name, "正在工作！")

class Student(People):
    sno = 0
    def study(self):
        print("学号为", self.sno, "的", self.name, "正在学习！")
    def sing(self):
        print("学号为", self.sno, "的", self.name, "正在唱歌！")

w = Worker()
w.name = "韩聪"
# w.work()
s = Student()
s.sno = 12
s.name = "许浩"
# s.study()
# s.sing()

class Chef:
    __name = ""
    __age = 0
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self, age):
        if age < 0 or age > 120:
            print("你家谁活这么大？")
        else:
            self.__age = age
    def getAge(self):
        return self.__age
    def cook(self):
        print("厨师正在做饭！")
class Chef1(Chef):
    def saute(self):
        print("厨师的儿子正在炒菜！")
class Chef2(Chef1):
    def cook(self):
        super().cook()
    def saute(self):
        super().saute()
c = Chef2()
c.cook()
c.saute()

















