#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'chengcha'
__mtime__ = '2017/9/13'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓    ┏┓
            ┏┛┻━━━┛┻┓
            ┃    ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃   ┻     ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃  神兽保佑 ┣┓
              ┃　永无BUG！ ┏┛
               ┗┓┓┏━┳ ┏┛
                ┃┫┫ ┃┫┫
                ┗┻┛ ┗┻┛
"""

names = ["aaa","bbb","ccc","ddd","eee","fff"]
names.append("ggg")  #添加一个值
names.insert(2,"hhh") #在第二个值后面插入一个值
names[2] = "iii"  #将第三个值bbb改成iii
names.remove("bbb") #删除一个值，或 del names[2] 或 names.pop(2)

print(names)
print(names[0],names[1])
print(names[1:3])   #切片
print(names[-1])   #取最后一个值
print(names[-2:]) #取最后2个值
print(names[:3])  #取前三个值
print(names.index("aaa"))  #查找aaa在第几个位置
print(names[names.index("aaa")])  #查找aaa并打印
print(names.count("aaa")) #查找aaa有多少个






