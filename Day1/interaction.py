#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'chengcha'
__mtime__ = '2017/8/23'
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
name = input("name:")
age = int(input("age:"))
#print(username,password)
job = input("job:")
salary = input("salary:")

info = '''
--------------- info of %s -------------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name,name,age,job,salary)

info2 = '''
--------------- info2 of {_name} -------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
''' .format(_name=name,
            _age=age,
            _job=job,
            _salary =salary)

info3 = '''
--------------- info3 of {0} -------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
''' .format(name,age,job,salary)

print(info)
print(info2)
print(info3)
