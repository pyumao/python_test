# -*- codiing: utf-8 -*-
# @time      : 2019/3/17 0017 下午 3:13
# @Author    : yu
# @Email     : 
# @File      : zuoye_0218.py

# import requests
#
# class HttpRequest:
#     '''完成http请求'''
#     def __init__(self,url):
#         self.url=url
#
#     def get(self):
#         return requests.get('{}'.format(self.url))
#
#     def post(self):
#         return requests.post('{}'.format(self.url))
#
# t=HttpRequest('https://www.ketangpai.com/Main/index.html')
#
# a=input('请输入数字1：get请求，2.post请求：')
# if a.isdigit():
#     if int(a)==1:
#         print(t.get().text)
#     elif int(a)==2:
#         print(t.post().text)
#     else:
#         print('输入有误，')
# else:
#     print('请输入数字')



import random
class GuessingGame:
    sum = 0
    count = 0
    c = 0

    def __init__(self, name=None):
        self.name = name


    def choice_characte(self):
        '''选择角色'''
        while True:

            option = input('请输入要选择的角色：1：曹操，2：张飞，3：刘备：')
            if option.isdigit():
                if int(option)==1:
                    self.name='曹操'
                    break
                elif int(option)==2:
                    self.name='张飞'
                    break
                elif int(option)==3:
                    self.name='刘备'
                    break
                else:
                    print('输入有误')


    def guessing_player(self):
        '''玩家出拳'''

        while True:
            print('请出拳')
            a = input('1：剪刀，2：石头，3：布:')
            if a.isdigit():
                if int(a)==1:
                    print('{}出石头'.format(self.name))
                    break
                elif int(a)==2:
                    print('{}出剪刀'.format(self.name))
                    break
                elif int(a)==3:
                    print('{}出布'.format(self.name))
                    break
                else:
                    print('输入有误')
        return int(a)

    def guessing_robot(self):
        '''robot出拳'''
        b=random.randint(1,3)
        if int(b) == 1:
            print('robot石头')
        elif int(b) == 2:
            print('robot剪刀')
        elif int(b) == 3:
            print('robot布')
        else:
            print('输入有误')
        return b


    def game(self):
        '''开始游戏'''
        while True:
            self.choice_characte()
            p=self.guessing_player()
            r=self.guessing_robot()

            if p==r:
                self.sum+=1
                print('该局平局')

            elif (p==1 and r==3) or (p==2 and r==1 ) or (p==3 and r==1):
                self.count+=1
                print('该局{}胜'.format(self.name))

            else:
                self.c+=1
                print('该局robot胜')
            f = input('是否继续？y/n:')
            if f == 'n':
                break
        self.result()
        print("游戏结束")


    def result(self):
        print('robot赢{}局'.format(self.c))
        print('{}赢{}'.format(self.name,self.count))
        print('平局{}次'.format(self.sum))
        if self.count > self.c:
            print('玩家胜')
        elif self.count <self.c:
            print('robot胜')
        else:
            print('平手')

if __name__=='__main__':
    res=GuessingGame()
    res.game()

