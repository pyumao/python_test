# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 3:43
# @Author    : yu
# @Email     : 
# @File      : learn_request.py

import requests


#注册
url='http://test.lemonban.com/futureloan/mvc/api/member/register'  #接口地址
param={'mobilephone':'18307217225','pwd':'123456','regname':'mao'} #字典形式存储数据
headers={'user-agent': 'Mozilla/5.0'}#模拟从Firefox浏览器发送出去的
resp_1=requests.get(url,params=param,headers=headers)
print(resp_1.text)

#登录
url='http://test.lemonban.com/futureloan/mvc/api/member/login'  #接口地址
param={'mobilephone':'18307217225','pwd':'123456'} #字典形式存储数据
resp_2=requests.post(url,data=param)
print(resp_2.json())

print('响应头：',resp_2.headers)
print('cookies',resp_2.cookies)
print('请求头',resp_2.request.headers)
print('状态码',resp_2.status_code)

#充值
url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'  #接口地址
param={'mobilephone':'18307217225','amount':'1234'} #字典形式存储数据
resp_3=requests.get(url,params=param,cookies=resp_2.cookies)
print(resp_3.json())

