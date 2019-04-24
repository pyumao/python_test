# -*- codiing: utf-8 -*-
# @time      : 2019/3/17 0017 下午 1:54
# @Author    : yu
# @Email     : 
# @File      : math_method.py

class MathMethod:
    '''这是一个数学类'''

    c=10
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        '''加法'''
        return self.a+self.b+self.c

    @classmethod
    def sub(cls):
        '''减法'''
        return cls.c+10

    @staticmethod
    def div():
        '''除法'''
        return 10

#测试代码
if __name__=='__main__':
    res=math_method(4,2)
    print(res.add())