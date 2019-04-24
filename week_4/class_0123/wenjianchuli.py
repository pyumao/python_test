# -*- codiing: utf-8 -*-
# @time      : 2019/3/11 0011 上午 11:48
# @Author    : yu
# @Email     : 
# @File      : wenjianchuli.py


file=open('py14.txt',encoding='utf-8') #r只读  r+读写  w清空之后写  w+清空之后读写   a  追加  a+追加  读写  py.txt文件名 没有就新建一个

# file.read(3)#读取指定元素个数，  不填就读取全部
# res=file.readline()#读取一行
# for i in range(1,5):
#     res=file.readline()
#     if i==3:
#         print(res)

res=file.readlines()#返回值的结果是列表，每一行作为列表的一个元素
print(res)

file.seek(0,0)#第一参数移动的多少个位置，第二个参数相对于谁去移动  0 头部  1当前位置  2末尾

# file.seek(0,0) #第一位