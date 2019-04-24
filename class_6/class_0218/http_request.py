# -*- codiing: utf-8 -*-
# @time      : 2019/3/17 0017 下午 3:02
# @Author    : yu
# @Email     : 
# @File      : http_request.py

#request模块
#pip install requsets

#requsets 完成http请求 get post
#一级宝典， 基础使用 二级宝典

import requests

#get请求
res_1=requests.get('http://www.baidu.com')
print(res_1)  #获取http状态码
print(res_1.text)  #获取响应结果

#post请求
# res_2=requests.post('http//www.baidu.com')