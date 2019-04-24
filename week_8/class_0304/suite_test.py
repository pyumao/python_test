# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 12:02
# @Author    : yu
# @Email     : 
# @File      : suite_test.py

import unittest
from week_8.class_0304.learn_ddt import TestMSG
import HTMLTestRunnerNew

suite=unittest.TestSuite()

loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMSG))

with open('text.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title=None,
                                            description=None,
                                            tester=None)
    runner.run(suite)
