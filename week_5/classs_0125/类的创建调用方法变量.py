# -*- codiing: utf-8 -*-
# @time      : 2019/3/12 0012 下午 2:32
# @Author    : yu
# @Email     : 
# @File      : 类的创建调用方法变量.py

#类的创建
#类的语法  关键字class
#class 类名：
    #类的说明
    #类体  属性 即变量  函数 即普通函数
#类名 标识符 驼峰命名法 WeChat  首字母大写区分每个词

# class WeChat:
#     '''微信类'''
#     company='腾讯'
#     year='2011'
#     PM='张小龙'
#     def send_msg(self):
#         print('发送消息')
#     def add_friend(self):
#         print('添加好友')
# f=WeChat()
# f.send_msg()#调用函数
# print(f.year)#调用属性

class BoyFrind:
    '''男友标准'''
    def __init__(self,age,height,name): #初始化函数属性
        self.age=age #给对象变量赋值
        self.height=height
        self.name=name
    def sport(self,*args):
        print(self.name+'爱运动{}'.format(args))
        self.coding()  #调用其他对象函数
        self.info()    #调用静态函数
        self.cook()

    def coding(self):
        print('会写代码')

    @classmethod
    def cook(cls):
        cls('','','胡歌').coding() #类函数调用对象函数  需要创建一个类
        print(cls('','','胡歌').name+'会下厨')

    @staticmethod  #写在类里面，但和类里面其他函数和属性 无调用关系（应用场景）
    def info():
        print('会打扫')

t=BoyFrind(30,175,'胡歌')
t.sport('跑步')
t.cook()
BoyFrind.info()
BoyFrind.cook()
#类里面的函数 分为3种 1.对象函数 2.类函数  3.静态函数
#对象函数：对象函数只能被对象调用
#类函数：可以被对象和类调用 @classmethod 只能标记一个函数
#静态函数：可以被 对象，类调用  @classmethod