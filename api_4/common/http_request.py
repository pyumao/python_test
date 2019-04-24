# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 4:47
# @Author    : yu
# @Email     : 
# @File      : http_request.py

import requests

class HttpRequest:
    # '''该类完成http的get或post请求'''

    def http_request(self,method,url,param,cookies):
        # '''根究请求方法发起get或post请求
        #     url：请求地址
        #     param：以字典格式存储请求参数
        #     method：请求方法 get post
        #     rtype：有返回值，返回结果是响应报文
        # '''
        global resp
        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,cookies=cookies)
            except Exception as e:
                print('错误是{}'.format(e))
                raise e
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,cookies=cookies)
            except Exception as e:
                print('错误是{}'.format(e))
                raise e
        else:
            resp=None
        return resp


if __name__ == '__main__':
    method = 'GET'
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'  # 接口地址
    param = {'mobilephone': '18307217225', 'pwd': '123456'}  # 字典形式存储数据

    resp=HttpRequest().http_request(method,url,param)
    print(resp)