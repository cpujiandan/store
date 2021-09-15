import random

list = ["孙佳伟", "刘浩", "瘦子", "特朗普", "拜登"]
ran = random.randint(1, 51)
for i in range(5):
    n = int(input("输入编号:"))
    print(list[n-1], "被处罚了", ran, "遍")
