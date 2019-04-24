# -*- codiing: utf-8 -*-
# @time      : 2019/4/14 0014 上午 11:41
# @Author    : yu
# @Email     : 
# @File      : class_unittest.py


#什么是单元测试 unit某部分 某个模块 某个类 去进行测试
#为什么要做单元测试



#unittest pytest


import unittest

#开始进行加法单元测试
class TestAdd(unittest.TestCase):
    def setUp(self): #在每一条用例执行之前执行
        print('开始执行') #准备测试环境
    def tearDown(self):#在每条测试用例执行之后执行
        print('执行结束') #清场工作/清除测试环境
    #写用例移动要用test_开头

    def test_001(self):#测试两个整数相加
        a=1
        b=2
        excepted=4
        c=a+b
        try:
            self.assertEqual(excepted,c)
        except AssertionError as e:
            print('001用例执行失败，错误时{}'.format(e))
            raise e
        finally:
            print('测试结果是{}'.format(c))

    def test_002(self):#测试两个负数相加
        a=-1
        b=-2
        excepted = -2
        c = a + b
        try:
            self.assertEqual(excepted, c)
        except AssertionError as e:
            print('002用例执行失败，错误时{}'.format(e))
            raise e

        print('测试结果是{}'.format(c))

    def test_003(self):#测试两个正 负数相加
        a=-1
        b=2
        excepted = 2
        c = a + b
        try:
            self.assertEqual(excepted, c)
        except AssertionError as e:
            print('003用例执行失败，错误时{}'.format(e))
            raise e
        print('测试结果是{}'.format(c))



#用例执行的时候是按照ASC编码执行的


# with open('text.log','w',encoding='utf-8') as file:
#     try:
#         print(a)
#     except Exception as e:
#         file.write(str(e))
#         raise e
