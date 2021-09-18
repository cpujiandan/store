# 有一个列表，[“北京”,”上海”,”广东”]
# 1)将中国所有省会城市添加到上述列表中
list = ["北京", "上海", "广东"]
list1 = ["山东", "河北", "吉林", "黑龙江", "辽宁", "内蒙古", "新疆", "甘肃", "宁夏", "山西", "陕西", "河南", "安徽", "江苏", "浙江", "福建", "江西", "海南", "广西", "贵州", "湖南", "湖北", "四川", "云南", "西藏", "青海", "台湾"]
# for i in range(len(list1)):
#     list.append(list1[i])
list.extend(list1)
print(list)
# 2)广东成为第二大发达城市，将广东排在上海前面
for j in range(len(list)):
    a = list[j]
    if a == "上海":
        break
list.remove("广东")
list.insert(j, "广东")
print(list)

# 3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
list2 = [36710.36, 35427.10, 29863.23, 29667.39, 27665.36, 27650.45, 27620.38, 25369.20]
num = 0
for i in range(len(list2)):
    num = num + list2[i]
print("GDP总和:%.2f  平均GDP:%.2f" %(num, num/8))

# 有以下一个列表，求其中是5的倍数的和
# a = [1,5,21,30,15,9,30,24]
list3 = [1, 5, 21, 30, 15, 9, 30, 24]
num = 0
for i in range(len(list3)):
    a = list3[i]
    if a % 5 == 0:
        num = num + a
print(num)

# 有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list5 = []
# for i in range(len(list4), 0, -1):
#     list5.append(list4[i-1])
for i in range(len(list4)):
    list5.append(list4.pop())
list4 = list5
print(list4)

# 请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
list6 = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
a = 0
for i in range(10):
    a = a + 1
    b = 0
    for j in range(len(list6)):
        if list6[j] == a:
            b = b + 1
    print("%d出现了:%d次"%(a, b))
