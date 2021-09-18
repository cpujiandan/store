i = 0
num = 0
import random
# print("********************************************No.1")
#
# while i < 10:
#     i = i + 1
#     print("请输入第", i, "个数字:")
#     s = int(input())
#     num = num + s
# print(num)
# print("********************************************No.2")
# b = 0
# while i < 10:
#     i = i + 1
#     print("请输入第", i, "个数字:")
#     a = int(input())
#     num = num + a
#     if i > 1:
#         if b > a:
#             a = b
#         else:
#             a = a
#     else:
#         continue
#     b = a
# print("最大数是:", b)
# print("10个数的和:", num)
# print("平均数是:", num/10)
#
# print("********************************************No.3")
# c = random.randint(50, 150)
# print(c)
#
# print("********************************************No.4")
# c = 0
# while i < 3:
#     i = i + 1
#     print("请输入第", i, "个数字:")
#     x = int(input())
#     if i == 1:
#         a = x
#     if i == 2:
#         b = x
#     if i == 3:
#         c = x
# print(a, b, c)
# if a + b > c and a + c > b and b + c > a and a - b < c and a - c < b and b - c < a:
#     d = a ** 2
#     e = b ** 2
#     f = c ** 2
#     if d + e == f or d + f == e or e + f == d:
#         print("这是直角三角形")
#     elif a == b != c or a == c != b or b == c != a:
#         print("这是等腰三角形")
#     elif a == b == c:
#         print("这是等边三角形")
#     else:
#         print("这是普通三角形")
# else:
#     print("不能形成三角形")
#
# print("********************************************No.5")
# A = 56
# B = 78
# C = 0
# print(A, B)
# while True:
#     D = input("请输入+或—:")
#     if D == "+":
#         C = A
#         A = B
#         B = C
#         print(A, B)
#     elif D == "-":
#         C = A
#         A = B
#         B = C
#         print(A, B)
#
#
# print("********************************************No.6")
# while True:
#     i = i + 1
#     user = input("请输入用户名:")
#     pwd = input("请输入密码:")
#     if user == "root" and pwd == "admin":
#         print("输入正确")
#         break
#     elif user != "root":
#         print("用户名不存在")
#         if i == 3:
#             print("对不起，程序已锁定")
#             break
#     elif user == "root" and pwd != "admin":
#         print("密码错误")
#         if i == 3:
#             print("对不起，程序已锁定")
#             break
#
# print("********************************************No.7")
# space = " "
# star = "*"
# while i < 7:
#     j = 0
#     i = i + 1
#     print(space * (7-i), end="")
#     while j < i:
#         if j == i - 1:
#             print(star)
#         else:
#             print(star, end=" ")
#         j = j + 1
#
# print("********************************************No.8")
# print("方法一:")
# for i in range(1, 10):
#
#     for j in range(1, i+1):
#er
#         print("%dx%d=%d"%(j, i, i*j), end="\t")
#     print()
# print("方法二:")
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if i == j:
#             print(j, "*", i, "=", i * j)
#         else:
#             print(j, "*", i, "=", i * j, " ", end="")
# print("********************************************No.9")
# for i in range(9, 0, -1):
#     for j in range(1, 10):
#         if i == j:
#             print("%dx%d=%d"%(j, i, i * j))
#             break
#         else:
#             print("%dx%d=%d" % (j, i, i * j), end=" ")
#
# print("********************************************No.10")
# a = 3
# b = -2
# c = 20
# for i in range(1, 100):
#     c = c - a
#     if c <= 0:
#         print(i, "天")
#         break
#     c = c - b

print("********************************************No.11")
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(20, 0, -1):
    i = i - 1
    j = i
    s = 1
    while j > 0:
        s = list[j] * s
        j = j -1
    num = num + s
print("1! +2!+3!+…..+20!=", num)
