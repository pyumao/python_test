# -*- codiing: utf-8 -*-
# @time      : 2019/3/23 0023 下午 5:23
# @Author    : yu
# @Email     : 
# @File      : 配置文件.py


# #什么是配置文件 .conf .ini .config .properties .xml
#
# #怎么写配置文件  ---[section] option  value
# # 2 怎么读取配置文件   configparser  目前用到的是Configparser类4
#
# from configparser import ConfigParser
#
# #创建对象
# cf=ConfigParser()
#
# #第一步打开文件
# cf.read('lemon.conf',encoding='utf-8')
#
# #第二步读取文件
# res=cf.get('StudentName','stu_4')
# # res=cf['StudentName']['stu_3']
# res=cf.getint('StudentName','stu_3')
# res=cf.getfloat('StudentName','stu_1')
# res=cf.getboolean('StudentName','stu_5')
# print(res) #获取的都是字符串类型
#
# print(type(eval(res)))  #还原原来的数据类型  字典列表字符串 元组只能用eval
