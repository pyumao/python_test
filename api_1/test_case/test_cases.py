# -*- codiing: utf-8 -*-
# @time      : 2019/4/18 0018 下午 6:27
# @Author    : yu
# @Email     : 
# @File      : test_cases.py

import unittest
from ddt import ddt,data,unpack
from api_1.common.http_request import HttpRequest
from api_1.common.project_path import case_path
from class_6.class_0220.do_excel import DoExcel

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试前的准备
        self.t = DoExcel(case_path, 'Sheet1')  #
    def tearDown(self):
        pass

    test_data = DoExcel(case_path, 'Sheet1').read_data()
    @data(*test_data)
    def test_case(self,case):
        # test_data = DoExcel(case_path, 'Sheet1').read_data()
        method = case['Method']  # 获取请求方法
        url = case['URL']  # 获取请求地址
        param = eval(case['Params'])  # 获取请求参数

        print('---正在测试{}模块，第{}条测试用例，测试标题:{}---'.format(case['Module'], case['CaseId'], case['Title']))

        resp = HttpRequest().http_request(method, url, param)
        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult='Pass'
        except Exception as e:
            print('请求错误，错误是{}'.format(e))
            TestResult = 'Failed'
        finally:
            #写回结果
            # t = DoExcel(case_path, 'Sheet1')
            self.t.write_back(case['CaseId'] + 1, 8, resp.text)
            self.t.write_back(case['CaseId'] + 1, 9, TestResult)

        print('测试结果{}'.format(resp.json()))




