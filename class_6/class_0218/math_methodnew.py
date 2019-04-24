# -*- codiing: utf-8 -*-
# @time      : 2019/3/17 0017 下午 2:03
# @Author    : yu
# @Email     : 
# @File      : math_methodnew.py

#继承 只有类与对象有
#我要有一个类，具有math_method里面的所有函数和属性值，除了div以外
#除此之外新增一个函数，完成多个参数相加并返回相加和

from class_6.class_0218.math_method import MathMethod

class MathMethodNew(MathMethod):
    def __init__(self,a,b):#重写

        self.a=10
        self.b=2

    def add(self):#重写的特点，与父类函数名一样的时候，重写以重写的为准  可以更改函数名以外的任意地方

        return self.a+self.b

    #拓展  父类里面没有 就是拓展
    def add_args(self,*args):
        sum=0
        for i in args:
            sum+=i
        return sum

if __name__=='__main__':
    t=MathMethodNew(5,4)
    res=t.add_args(1,2,3,4,5)
    print(res)
