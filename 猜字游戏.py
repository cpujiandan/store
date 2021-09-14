import random

start = 0
m = int(input("赶紧输入要充值的金额，我可没时间等你:"))
while True:
    if m < 1000:
        print("充值金额不能少于1000，给我重新输！！！")
        m = int(input("快点！！！:"))
    else:
        break
start = int((start+m)*(1+m*0.0001))
print("资金剩余：", start)
j = -1
while j < 0:
    a = input("输入1（开始）或Q（退出）游戏")
    ran = random.randint(1, 10)
    # print(ran)
    if start < 500:
        print("把钱冲够了再来玩吧！穷鬼！！！")
        m = int(input("赶紧输入要充值的金额，我可没时间等你:"))
        while True:
            if m < 1000:
                print("充值金额不能少于1000，给我重新输！！！")
                m = int(input("快点！！！:"))
            else:
                break
        start = int((start + m) * (1 + m * 0.0001))
        print("资金剩余：", start)
        # break
    else:
        if a == "1":
            i = 0
            while i < 5:
                s = int(input("输入一个0-10的数:"))
                if ran == s:
                    print("妈呀你可终于猜对了！！！")
                    print("资金剩余：", start)
                    break
                else:
                    if s < ran:
                        print("小了笨蛋！！！就剩", 4-i, "次了")
                    else:
                        print("大了废物！！！就剩", 4-i, "次了")
                    i = i+1
                    if start < 500:
                        start = 0
                    else:
                        start = start - 500
                    print("资金剩余：", start)
                    if start <= 0:
                       break
        elif a == "Q":
            break