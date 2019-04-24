# -*- codiing: utf-8 -*-
# @time      : 2019/4/14 0014 下午 12:46
# @Author    : yu
# @Email     : 
# @File      : learn_suite.py

import unittest
import HTMLTestRunnerNew
from week_7.class_unittest_0301.class_unittest import TestAdd
from week_7.class_unittest_0301 import class_unittest
suite=unittest.TestSuite()  #测试套件 ————收集存储用例

#加载测试用例方法一
# suite.addTest(TestAdd('test_001'))#测试用例的实例
# suite.addTest(TestAdd('test_002'))#测试用例的实例

#方法二
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))

#方法三
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(class_unittest))

#执行用例 TestTextRunner 老版本
with open('test.txt','w',encoding='utf-8') as file:
    runner=unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    runner.run(suite)  #执行测试套件里面的用例

#执行用例生成报告
# with open('test.html','wb') as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                             verbosity=2,
#                                             title=None,
#                                             description=None,
#                                             tester=None)
#     runner.run(suite)

# .一个点表示一条用例通过
#E 表示一条用例报错
#F  表示测试用例未通过fail 期望不等于实际