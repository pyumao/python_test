# -*- codiing: utf-8 -*-
# @time      : 2019/4/15 0015 下午 3:24
# @Author    : yu
# @Email     : 
# @File      : learn_ddt.py

#ddt data drive test
#数据驱动测试
#安装 pip install ddt

import unittest
from ddt import ddt,data,unpack
test_data=((1,2,3),(2,3,4))
test_data_2=({'a':1,'b':2,'expected':3},{'a':2,'b':3,'expected':4})
@ddt # 装饰测试类
class TestMSG(unittest.TestCase):
    def setUp(self):
        print('执行测试')
    def tearDown(self):
        print('测试结束')
    @data(*test_data)
    @unpack
    def test_001(self,a,b,expected=None):
        c=a+b
        try:
            self.assertEqual(expected,c)
        except Exception as e:
            print('错误是{}'.format(e))
        finally:
            print('结束是{}'.format(c))

        # print('执行第{}条用例了'.format(a)

