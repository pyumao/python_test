# -*- codiing: utf-8 -*-
# @time      : 2019/4/15 0015 下午 7:43
# @Author    : yu
# @Email     : 
# @File      : request.py

import requests

#注册请求

# url='http://test.lemonban.com/futureloan/mvc/api/member/register'  #接口地址
# param={'mobilephone':'18307217222','pwd':'123456','regname':'maomao'} #字典形式存储数据
#发送一个get请求
#头部
# headers = {'user-agent': 'Mozilla/5.0'}#模拟从Firefox浏览器发送出去的

# file=open('text.txt','w',encoding='utf-8')
# resp=requests.get(url,params=param,headers=headers)
# print(resp.text)  #返回字符串类型
# print(resp.json())  #返回字典类型   #当返回数据类型是josn字符串的时候才能用这种方式获取响应报文

#发送一个post请求
# headers = {'user-agent': 'Mozilla/5.0'}#模拟从Firefox浏览器发送出去的

# file=open('text.txt','w',encoding='utf-8')
# resp=requests.post(url,data=param,headers=headers) #post请求要用data  不是params
# print(resp.text)  #返回字符串类型
# print(resp.json())  #返回字典类型
# print(type(resp.text))
# print(type(resp.json()))


#登录请求
url='http://test.lemonban.com/futureloan/mvc/api/member/login'  #接口地址
param={'mobilephone':'18307217222','pwd':'123456'} #字典形式存储数据
#发送一个get请求
#头部
headers = {'user-agent': 'Mozilla/5.0'}#模拟从Firefox浏览器发送出去的

# file=open('text.txt','w',encoding='utf-8')
# resp=requests.get(url,params=param,headers=headers)
# print(resp.text)  #返回字符串类型
# print(resp.json())  #返回字典类型

#发送一个post请求
headers = {'user-agent': 'Mozilla/5.0'}#模拟从Firefox浏览器发送出去的

file=open('text.txt','w',encoding='utf-8')
resp=requests.post(url,data=param,headers=headers)
print(resp.text)  #返回字符串类型
# print(resp.json())  #返回字典类型
# print(type(resp.text))
# print(type(resp.json()))

# {"status":1,"code":"10001","data":null,"msg":"登录成功"}
# {'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}
# s='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'  #python中不识别null
# s_1={'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}
# import json
# # value=json.loads(s) #将字符串转化成字典  key和value 都必须是双引号
# # print(value)
# # print(type(value))
#
# value_1={'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}
# value_1=json.dumps(s_1,ensure_ascii=False)  #将字典转化成josn格式的字符串  josn不识别None
# print(value_1)
# print(type(value_1))

# try:
#     resp=requests.get(url) #返回一个消息实体
#     print(resp.text)
# except Exception as e:
#     file.write(str(e))
#     raise e


# #响应结果：状态码 响应报文 响应头 cookies
print('状态码:',resp.status_code)
print('响应头:',resp.headers)
print('cookies:',resp.cookies)

print('请求头:',resp.request.headers)
