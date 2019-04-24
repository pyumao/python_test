# -*- codiing: utf-8 -*-
# @time      : 2019/3/12 0012 上午 11:37
# @Author    : yu
# @Email     : 
# @File      : add_1.py

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def add_2(*args):
    sum=0
    for item in args:
        sum+=item
    return sum

if  __name__=='__main__': #程序执行入口，只有执行当前py文件的时候才会被执行
    print(add(1,2))

