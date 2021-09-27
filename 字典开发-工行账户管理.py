import random
from DBUtils import update
from DBUtils import select
# bank = {12345678: {"username": 'xuhao', 'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002',  "money": 100},
#         12345677: {"username": 'xu', 'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002',  "money": 100}}
bank_name = "中国工商银行昌平支行"
def bankAddUser(account, username, password, country, province, street, door, money, bank_name):
        sql = "select count(*) from user"
        param = []
        sql1 = "select * from user where username = %s"
        param1 = [username]
        data = select(sql, param)
        data1 = select(sql1, param1)
        if len(data) >= 100:
                return 3
        elif len(data1) > 0:
                return 2
        else:
                sql2 = "insert into user(account, username, password, country, province, street, door, money, registerDate, bankname) " \
                       "values (%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
                param2 = [account, username, password, country, province, street, door, money, bank_name]
                update(sql2, param2)
                return 1

def addUserInfo():
        account = random.randint(10000000, 99999999)
        username = input("请输入你的姓名:")
        password = input("请输入你的密码:")
        print("请输入您的个人详细地址：")
        country = input("\t国家:")
        province = input("\t省份:")
        street = input("\t街道:")
        door = input("\t门牌号:")
        money = 0
        bankadd = bankAddUser(account, username, password, country, province, street, door, money, bank_name)
        if bankadd == 1:
                print("添加用户成功，以下是您的信息")
                info = '''
                         ------------个人信息------------
                            用户名:%s
                            账号：%s
                            密码：*****
                            国籍：%s
                            省份：%s
                            街道：%s
                            门牌号：%s
                            余额：%s
                            开户行名称：%s
                '''
                print(info % (username, account, country, province, street, door, money, bank_name))
                quit(quit)
        if bankadd == 2:
                print("用户已存在")
        if bankadd == 3:
                print("用户库已满")

def save():
        acc = int(input("请输入要存钱的账号:"))
        sql = "select money from user where account=%s"
        param = [acc]
        data = select(sql, param)
        if len(data) > 0:
                count = int(input("请输入要存入的金额"))
                sql1 = "update user set money=money+%s where account=%s"
                param1 = [count, acc]
                update(sql1, param1)
                # bank[acc]["money"] = count + bank[acc]["money"]
                print("存入成功")
                data1 = select(sql, param)
                print(data1[0][0],"元")
                quit(quit)
        else:
                print("账户不存在，请输入正确的账号")
def draw():
        acc = int(input("请输入要取钱的账号:"))
        sql = "select password from user where account=%s"
        param = [acc]
        data = select(sql, param)
        if len(data) == 0:
                print("账户不存在，请输入正确的账号")
        else:
                i = 0
                while i < 3:
                        i = i + 1
                        pwd = int(input("请输入密码:"))
                        if pwd != data[0][0]:
                                print("密码有误")
                        else:
                                count = int(input("请输入要取出的金额"))
                                sql1 = "select money from user where account=%s"
                                data1 = select(sql1, param)
                                if count > data1[0][0]:
                                        print("钱不够")
                                else:
                                        sql2 = "update user set money=money-%s where account=%s"
                                        param2 = [count, acc]
                                        update(sql2, param2)
                                        # bank[acc]["money"] = bank[acc]["money"] - count
                                        print("取出成功")
                                        data2 = select(sql1, param)
                                        print(data2[0][0],"元")
                                        quit(quit)
                                break
#
#
def trans():
        acc1 = int(input("请输入转出钱的账号:"))
        acc2 = int(input("请输入转入钱的账号:"))
        sql = "select password from user where account=%s"
        sql1 = "select money from user where account=%s"
        param = [acc1]
        param1 = [acc2]
        data = select(sql, param)
        data1 = select(sql1, param1)
        if len(data) == 0 or len(data1) == 0:
                print("账户不存在，请输入正确的账号")
        else:
                i = 0
                while i < 3:
                        i = i + 1
                        pwd = int(input("请输入转出账户密码:"))
                        if pwd != data[0][0]:
                                print("密码有误")
                        else:
                                count = int(input("请输入转账的金额"))
                                sql2 = "select money from user where account=%s"
                                data2 = select(sql2, param)
                                if count > data2[0][0]:
                                        print("钱不够")
                                else:
                                        sql3 = "update user set money=money-%s where account=%s"
                                        sql4 = "update user set money=money+%s where account=%s"
                                        param3 = [count, acc1]
                                        param4 = [count, acc2]
                                        update(sql3, param3)
                                        update(sql4, param4)
                                        print("转账成功")
                                        data3 = select(sql2, param)
                                        print("转出账户余额:", data3[0][0])
                                        quit(quit)
                                break
def select1():
        acc = int(input("请输入要查询的账号:"))
        sql = "select password from user where account=%s"
        param = [acc]
        data = select(sql, param)
        if len(data) == 0:
                print("该用户不存在")
        else:
                i = 0
                while i < 3:
                        i = i + 1
                        pwd = int(input("请输入账户密码:"))
                        if pwd != data[0][0]:
                                print("密码有误")
                        else:
                                info = '''
                                                         ------------个人信息------------
                                                            用户名:%s
                                                            账号：%s
                                                            密码：%s
                                                            国籍：%s
                                                            省份：%s
                                                            街道：%s
                                                            门牌号：%s
                                                            余额：%s
                                                            开户行名称：%s
                                                '''
                                sql1 = "select username from user where account=%s"
                                sql2 = "select country from user where account=%s"
                                sql3 = "select province from user where account=%s"
                                sql4 = "select street from user where account=%s"
                                sql5 = "select door from user where account=%s"
                                sql6 = "select money from user where account=%s"
                                sql7 = "select bankname from user where account=%s"
                                data1 = select(sql1, param)
                                data2 = select(sql2, param)
                                data3 = select(sql3, param)
                                data4 = select(sql4, param)
                                data5 = select(sql5, param)
                                data6 = select(sql6, param)
                                data7 = select(sql7, param)
                                print(info % (data1[0][0], acc, data[0][0],
                                              data2[0][0], data3[0][0],
                                              data4[0][0], data5[0][0],
                                              data6[0][0], data7[0][0]))
                                # quit = int(input("是(1)否(0)退出:"))
                                # while True:
                                #         if quit == 1:
                                #                 break
                                #         elif quit == 0:
                                #                 quit = int(input("是(1)否(0)退出:"))
                                quit(quit)
                                break
def quit(quit):
        quit = int(input("是(1)否(0)退出:"))
        while True:
                if quit == 1:
                        break
                else:
                        quit = int(input("是(1)否(0)退出:"))

while True:
        print("==============================================")
        print("|------------中国工商银行账户管理系统------------|")
        print("|------------1、开户              ------------|")
        print("|------------2、取钱              ------------|")
        print("|------------3、存钱              ------------|")
        print("|------------4、转账              ------------|")
        print("|------------5、查询              ------------|")
        print("|------------6、退出              ------------|")
        print("==============================================")
        begin = int(input("请选择业务:"))
        if begin == 1:
                addUserInfo()
        if begin == 2:
                draw()
        if begin == 3:
                save()
        if begin == 4:
                trans()
        if begin == 5:
                select1()
        if begin == 6:
                break

