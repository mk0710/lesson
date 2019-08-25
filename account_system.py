# -*- coding: utf-8 -*-
#
# """注册账户逻辑demo1"""
# print('------------------Welcome！-------------------')
# print('1.注册账户')
# num = input('请选择您需要的操作：')
# accounts = ['mk710', 'mk0710']
# passwords = ['000', '0000']
# if num == '1':
#     account_name = input('请输入账户名称：')
#     if account_name in accounts:
#         print('此账号已被注册，请重新输入!')
#     else:
#         accounts.append(account_name)
#         password = input('请输入密码：')
#         passwords.append(password)
#         print(accounts,passwords)

"""
注册账户逻辑
"""
print('------------------Welcome！-------------------')
print('1. 注册账户\n2. 登录账户\n3. 修改密码\n4. 注销账户')
num = input('请选择您需要的操作：')
# 打开账户信息文件
with open('account_code.txt') as f:
    file = f.readlines()
    # print(file)
    account_info = [line.split() for line in file]
    print(account_info)
accounts = account_info[0]
passwords = account_info[1]
flag = True
if num == '1':
    while flag:
        account_name = input('请输入账户名称：')
        if account_name in accounts:
            print('此账号已被注册，请重新输入!')
        else:
            flag = False
            accounts.append(account_name)
            password = input('请输入密码：')
            passwords.append(password)
            print('注册成功')
            """
            1. 多个字符串拼接成一个
            2. 把字符串构成列表
            3. 
            """
            accounts = " ".join(accounts)
            passwords = " ".join(passwords)
            # print(passwords)
            # print(accounts)
            new_account_info = [accounts + '\n', passwords]
            # print(new_acc_info)
            with open('account_code.txt', 'w') as f:
                f.writelines(new_account_info)
            break
# elif num == 2:

