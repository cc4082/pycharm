#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'chengcha'
__mtime__ = '2017/9/1'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
'''
for i in range(10): # i为临时变量，循环10次，
    print("loop",i)

for i in range(1,10,2):  #从1开始，隔2个数字打印，一直到10
    print("loop",i)

for i in range(0,10):
    if i <3:
        print("loop",i)
    else :
        continue
    print("呵呵...")





age_of_cc = 30

for i in range(3):
    guess_age = int(input("猜年龄："))

    if guess_age == age_of_cc :
        print("恭喜你，猜对了！")
        break
    elif guess_age > age_of_cc:
        print("往小处想...")
    else:
        print("往大处想...")
    count +=1
else:
    print("你试了太多次！")
'''
for a in  range(10):
    print("-------------",a)
    for j in range(10):
        print(j)
        if j >5:
            break
