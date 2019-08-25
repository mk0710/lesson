# -*- coding: utf-8 -*-
"""
代码风格
"""

# import random
# for i in range(5):
#     print(random.randint(1, 5))
#
# import random as r
# for i in range(5):
#     print(r.randint(1, 5))
#
# from random import randint
# for i in range(5):
#     pass
# print(randint(1, 5))

"""
理解变量
"""

# # num = 0
# # print(id(num))
# # mm = "3"
# print(id(mm))

# a = round(0.3213*3, 3)
# a = 1232134
# # 左边是 变量的名字 右边1
#
# b = 1232134
# print(id(a))
# print(id(b))
#
# print(a is b)
# name =  "python " \
#         "    " \
#         "java   " \
#         " ruby    " \
#         " c++"
# print(name.split())
# print(name)
#
# str = "this is string....wow!!! this is really string"
# str.replace("is", "was")
# strr = str.replace("is", "was", 3)
# print(str)
# print(strr)
# name =  "li lei"
# print(name. find("lei"))
# nums = ["我","sa","s"]
# nums.sort()
# print(nums)
# nums.sort(reverse = True)
# print(nums)
"""连接列表元素"""
languages = ['python', 'java', 'ruby']

print(languages)
print('&'.join(languages))

"""列表长度"""
# list2 = [[1, 2], [5, 6], '1997', 2000]
# print(len(list2))
# print(len(list2[0]))
# print(len(list2[2]))
"""文本文件处理案列"""
# data_file = open('C:/Users/Administrator/Desktop/F190327.txt')
# data = data_file.readlines()
# print(data)
# print(data[0])
# data_0 = data[0].split()
# print(data_0)
"""大小写顺序"""
# print(ord('a'),ord('A'))
"""函数sorted()"""
# letters = ['d', 'c', 'a', 'b']
# print("这是临时排序的列表:", sorted(letters))
# print("原始列表", letters)
# print("这是临时倒序的列表:", sorted(letters, reverse=True))
"""列表+"""
# languages = ['python', 'java', 'ruby']
# new_lang =['C++','C#','PHP']
# final_lang = languages + new_lang
# print(final_lang)

"""方法extend()"""
# languages = ['python', 'java', 'ruby']
# new_lang = ['C++', 'C#', 'PHP']
# languages.extend(new_lang)
# print(languages)
"""函数sorted()"""
# nums = [2, 5, 1, 1]
# nums.reverse()
# print(nums)
"""方法count()"""
# nums = [2, 5, '1', '1']
# print(nums.count('1'))
"""方法index"""
# nums = [2, 5, '1', '1']
# print(nums.pop(nums.index('1')))
# print(nums)
"""用循环修改列表"""
# index = 0
# a = [1, 2, 3]
# for aa in a:
#     aa *= 2
#     a[index] = aa
#     index += 1
#     print(index)
# print(a)
"""修改游戏人物的生命值"""
# HPs = [20, 30, 40, 50]
# HPs_new = []
# for HP in HPs:
#     HP = HP + 30
#     HPs_new.append(HP)
# print(HPs_new)
"""1到5的和"""
# print(sum([1,2,3,4,5]))
"""5的阶乘"""
# nums = [1, 2, 3, 4, 5]
# result = 1
# for num in nums:
#     result = result * num
# print(result)
# #########################
# nums = [1, 2, 3, 4, 5]
# result = 1
# for num in nums:
#     result *= num
# print(result)
########################
"""复制"""
# list2 = [1, 2, 3, 4.0, 5.0]
# list3 = ["a", "b", "c", "D"]
# print(list3*2)
"""if语句"""
# score = 80
# if score > 60:
#     print('及格')
# else:
#     print('不及格')
"""elif语句"""
# score = 85
# if score < 60:
#     print('差')
# elif score <= 75:
#     print('中')
# elif score <= 85:
#     print('良')
# else:
#     print('优')
"""if-if"""
# scores = [55, 60, 75, 100, 65, 70, 83, 91,100]
# notpass = 0
# perfect = 0
# for score in scores:
#     if score < 60:
#         notpass += 1
#     if score == 100:
#         perfect += 1
# print("不及格人数：", notpass, "\n满分人数：", perfect)
"""多个列表的操作"""
# a = [3, 5, 9, 'J', 'K']
# b = [1, 3, 7, 'J', 'Q']
# same_card = []
# for card in a:
#     if card in b:
#         same_card.append(card)
# print("相同的扑克牌：", end='')
# for card in same_card:
#     print(card, end=' ')
"""列表推导式"""
# a = [3, 5, 9, 'J', 'K']
# b = [1, 3, 7, 'J', 'Q']
# same_card = [card for card in a if card in b]
# print('相同的扑克牌：', same_card)
"""列表推导式0-9平方列表"""
# c = [x**2 for x in range(0, 10)]
# print(c)
"""列表推导式0-9平方的奇数列表"""
# cc = [x**2 for x in range(0, 10) if x**2 % 2 != 0]
# print(sum(cc))
"""处理字符串列表"""
# freshfruit = ['  banana', '  strawberry    ', '  apple   ']
# print([fruit.strip() for fruit in freshfruit])
"""列表推导式生成嵌套列表"""
# print([(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 2 == 1])
"""列表推导式练习"""
# rices = [2**i for i in range(20)]
# print(sum(rices))
"""while语句练习10个hello"""
# n = 10
# while n > 0:
#     print('hello python', end='\n')
#     n -= 1
"""while语句练习0到100偶数"""
# num = 1
# while num < 101:
#     if num % 2 == 0:
#         print(num, end=",")
#     num += 1
"""while语句练习剔除列表的固定值"""
# for语句
# nums = [5, 1, 3, 4, 5, 6, 2, 5]
# for num in nums:
#     if num == 5:
#         nums.remove(5)
# print(nums)
#  while语句
# num = [5, 1, 3, 4, 5, 6, 2, 5]
# while 5 in num:
#     num.remove(5)
# print(num)
"""break"""
# while True:
#     command = input('请输入指令：')
#     if command =='quit':
#         print('退出')
#         break

"""3times_code_1"""
# code = "123"
# n = 1
# while n <= 3:
#     imput_code = input('请输入密码：')
#     if imput_code == code:
#         print("你好")
#         break
#     else:
#         print("请重新输入！")
#     n += 1
# else:
#     print("对不起，错误次数超限")
"""3times_code_2"""
# code = "123"
# n = 1
# while n <= 3:
#     imput_code = input('请输入密码：')
#     if imput_code == code:
#         print("你好")
#         break
#     else:
#         if n != 3:
#             print("请重新输入！")
#     n += 1
# else:
#     print("对不起，错误次数超限")


lines = []
f = 1
while f:
    lines.append(input())
else:
    f = 0

print(lines)


