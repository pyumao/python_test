# -*- codiing: utf-8 -*-
# @time      : 2019/3/17 0017 下午 2:40
# @Author    : yu
# @Email     : 
# @File      : wechat.py

class WeChat:
    '''微信类'''
    company='腾讯'
    year='2011'
    PM='张小龙'

    def send_msg(self):
        print('发送消息')

    def add_friend(self):
        print('添加好友')

f=WeChat()
f.send_msg()#调用函数
print(f.year)#调用属性