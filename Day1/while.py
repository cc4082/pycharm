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


age_of_cc = 30

count = 0
while count < 3:
    guess_age = int(input("猜年龄："))

    if guess_age == age_of_cc :
        print("恭喜你，猜对了！")
        break
    elif guess_age > age_of_cc:
        print("往小处想...")
    else:
        print("往大处想...")
    count +=1
    if count == 3:
       continue_confirm = input("你想继续吗？")
        if continue_confirm != 'n':  #如果输入的key不等于n，则将count置为0，继续猜年龄；
            count = 0
else:
    print("你试了太多次！")
















