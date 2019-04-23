# -*- codiing: utf-8 -*-
# @time      : 2019/4/21 0021 下午 4:53
# @Author    : yu
# @Email     : 
# @File      : learn_re.py

import re
from api_5.common.get_data import GetData

'''
1.什么是正则表达式？编写一些规范查找需要的字符
2.正则表达式的要给组成 。原义字符   元字符
3.如何使用python来解析
4.正则使用场景
---参数化
---查找一些特殊字符：邮箱 手机号码 身份证号码
'''

#方式一使用原义字符查找
# target="{'mobilephone':'normal_user','pwd':'nurmal_pwd'}" #目标字符串
#
# p = 'normal_user'  #正则表达式
#
# m=re.search(p,target)  #在目标字符串里面根据正则表达式查找，有匹配字符就返回对象
#
# print(m)
# print(m.group())

#方式二使用元字符（通配符）来查找
# target="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}" #目标字符串
# p2='#(.*?)#'  #圆括号代表正则表达式里面组的概念  ?是限定符
# re.match(p2,target) #math从开头位置知道 开头没有就结束
# re.finditer(p2,target)  #返回一个包含所有匹配对象的迭代器
# m=re.search(p2,target)  #在目标字符串里面根据正则表达式查找，有匹配字符就返回对象  search从任意位置开始找，找到一个就返回 并放进一个组里面
#
# print(m)
# print(m.group())  #不传参的时候返回表达式和匹配的字符串一起
# print(m.group(1)) #传参就是只返回匹配的字符串，也就是当前组的匹配字符
# mm=re.findall(p2,target)  #找到所有匹配的字符，返回一个列表   findall找到全部返回列表
# print(mm)
#
# # re.sub()  #找到并替换
# target2=re.sub(p2,'1830',target,count=1)  #p2正则表达式 ，1830  需要替换的的字符串，target目标字符串，count=1替换次数
#
# print(target2)
# def replace():
target="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}" #目标字符串
p2='#(.*?)#'  #圆括号代表正则表达式里面组的概念  ?是限定符
while re.search(p2,target):
    m=re.search(p2,target)
    key=m.group(1)
    value=getattr(GetData,key)
    target = re.sub(p2,value,target,count=1)
#
print(target)


