# -*- codiing: utf-8 -*-
# @time      : 2019/3/11 0011 上午 9:44
# @Author    : yu
# @Email     : 
# @File      : 路径处理.py

# file=open('py14.txt',encoding='utf-8')
# print(file.read())
#
import os

# path_1=os.getcwd()#获取当前的工作目录（目录）
# path_2=os.path.realpath(__file__) # __file__表示当前文件（文件路径）
# path_3=os.path.basename(__file__)#(文件名）
# print(path_1)
# print(path_2)
# print(path_3)


# 路径的切割  os.path.split()
# path_2=os.path.realpath(__file__) # __file__表示当前文件（文件路径）
# print(os.path.split(path_2))
# print(os.path.split(path_2)[0])
# print(os.path.split(os.path.split(path_2)[0])[0])

#路径的拼接 os.path.join()
path_2=os.path.realpath(__file__)
path_4=os.path.split(os.path.split(path_2)[0])[0]
print(path_4)
path_5=os.path.join(path_4,'py14.txt')
print(path_5)
file=open(path_5,encoding='utf-8')
print(file.read())