# -*- codiing: utf-8 -*-
# @time      : 2019/4/18 0018 下午 7:42
# @Author    : yu
# @Email     : 
# @File      : run.py

import unittest
from api_3.test_case import test_register
from api_3.test_case import test_login
from api_3.test_case import test_recharge
import HTMLTestRunnerNew
from api_3.common.project_path import report_path

#新建一个测试集
suite=unittest.TestSuite()

#添加测试用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test_register.TestCases))
suite.addTest(loader.loadTestsFromTestCase(test_login.TestCases))
suite.addTest(loader.loadTestsFromTestCase(test_recharge.TestCases))

#执行测试 生成测试报告
with open(report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title=None,
                                            description=None,
                                            tester=None)

    runner.run(suite)
