# -*- codiing: utf-8 -*-
# @time      : 2019/3/13 0013 下午 7:27
# @Author    : yu
# @Email     : 
# @File      : 0125zuoye.py



# #习题1
# class MathMethod:
#     '''数学类'''
#     def __init__(self,a,b):  #类属性初始化
#         self.a=a
#         self.b=b
#     def add(self):
#         '''加法对象函数'''
#         self.sub()  #对象函数调用类函数
#         self.Div()  #对象函数调用对象函数
#         self.info() #对象函数调用静态函数
#         sum=self.a+self.b
#         return sum
#
#     @classmethod
#     def sub(cls):
#         '''减法类函数'''
#         cls.info()  #类函数调用静态函数
#         cls(4,2).Div() #类函数调用对象函数
#         sum=cls(4,2).a-cls(4,2).b
#         print(sum)
#
#     @staticmethod
#     def info():
#         '''乘法静态函数'''
#         a=2
#         b=3
#         c=a*b
#         print(c)
#         return c
#
#     def Div(self):
#         '''除法对象函数'''
#         d=self.a/self.b
#         print(d)
#         return d
#
# t=MathMethod(6,3)  #实例化类
# print(t.add())
# print(t.sub())
# print(t.info())
# print(t.Div())


#习题2

class TestEngineer:
    '''测试工程师基础信息'''
    def __init__(self,name,age,sex,year):
        '''类属性初始化'''
        self.name=name

        self.age=age
        self.sex=sex
        self.year = year

    def basicinformation(self,*args):
        '''基础信息'''
        print('该工程师名叫{}，年龄{}，性别{},爱好{}'.format(self.name,self.age,self.sex,args))

    @classmethod
    def resume(cls):
        '''履历'''
        cls('yu','san','','')
        print('{}该工程师于2016年从事testengineer，至今从事该行业{}年'
              .format(cls('yu','','',3).name,cls('yu','','',3).year))
    @staticmethod
    def info():
        '''总结语'''
        print('该工程师基本符合岗位需求')

t=TestEngineer('yu',28,'nan',3)
print(t.basicinformation('爬山','阅读'))
print(t.resume())
print(t.info())