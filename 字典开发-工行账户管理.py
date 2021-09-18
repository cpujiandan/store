import random
bank = {12345678: {"username": 'xuhao', 'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002',  "money": 100},
        12345677: {"username": 'xu', 'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002',  "money": 100}}
bank_name = "中国工商银行的昌平支行"
def bankAddUser(account, username, password, country, province, street, door, money):
        if account in bank:
                return 2
        elif len(bank) >= 100:
                return 3
        else:
                bank[account] = {
                        "username": username,
                        "password": password,
                        "country": country,
                        "province": province,
                        "street": street,
                        "door": door,
                        "money": money,
                        "bank_name": bank_name,

                }
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
        bankadd = bankAddUser(account, username, password, country, province, street, door, money)
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
        if acc in bank:
                count = int(input("请输入要存入的金额"))
                bank[acc]["money"] = count + bank[acc]["money"]
                print("存入成功")
                print(bank[acc]["money"])
                quit(quit)
        else:
                print("账户不存在，请输入正确的账号")
                return False
def draw():
        acc = int(input("请输入要取钱的账号:"))
        if acc not in bank:
                print("账户不存在，请输入正确的账号")
        else:
                i = 0
                while i < 3:
                        i = i + 1
                        pwd = input("请输入密码:")
                        if pwd != bank[acc]["password"]:
                                print("密码有误")
                        else:
                                count = int(input("请输入要取出的金额"))
                                if count <= bank[acc]["money"]:
                                        bank[acc]["money"] = bank[acc]["money"] - count
                                        print("取出成功")
                                        print(bank[acc]["money"])
                                        quit(quit)
                                break


def trans():
        acc1 = int(input("请输入转出钱的账号:"))
        acc2 = int(input("请输入转入钱的账号:"))
        if acc1 not in bank or acc2 not in bank:
                print("账户不存在，请输入正确的账号")
        else:
                i = 0
                while i < 3:
                        i = i + 1
                        pwd = input("请输入转出账户密码:")
                        if pwd != bank[acc1]["password"]:
                                print("密码有误")
                        else:
                                count = int(input("请输入转账的金额"))
                                if count <= bank[acc1]["money"]:
                                        bank[acc1]["money"] = bank[acc1]["money"] - count
                                        bank[acc2]["money"] = bank[acc2]["money"] + count
                                        print("转账成功")
                                        print("转出账户余额:", bank[acc1]["money"])
                                        print("转入账户余额:", bank[acc2]["money"])
                                        quit(quit)
                                break
def select():
        acc = int(input("请输入要查询的账号:"))
        if acc not in bank:
                print("该用户不存在")
        else:
                i = 0
                while i < 3:
                        i = i + 1
                        pwd = input("请输入账户密码:")
                        if pwd != bank[acc]["password"]:
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
                                print(info % (bank[acc]["username"], acc, bank[acc]["password"],
                                              bank[acc]["country"], bank[acc]["province"],
                                              bank[acc]["street"], bank[acc]["door"],
                                              bank[acc]["money"], bank_name))
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
                select()
        if begin == 6:
                break

