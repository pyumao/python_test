# -*- codiing: utf-8 -*-
# @time      : 2019/3/17 0017 下午 2:42
# @Author    : yu
# @Email     : 
# @File      : we_chat_1.1.py

from class_6.class_0218.wechat import WeChat
import random
class WeChat_1(WeChat):

    def send_red_bag(self,money,number,status): #发送红包
        '''money：发送的金额
            number:发送红包的个数'''

        if 0.01 <=money<=100:
            if number!=1:
                if status==1:
                    print('共计发送{}个红包，每个金额是{}'.format(number,money/number))
                else:
                    sum=0
                    c=random.random(money,number)
                    for item in c:
                        sum+=item
                        if sum==money:
                            print('共计发送{}个红包，金额分别是{}'.format(number,item))


            else:
                print('发送一个红包，金额是{}'.format(money))
        else:
            print('金额必须在0.01到200之间')
