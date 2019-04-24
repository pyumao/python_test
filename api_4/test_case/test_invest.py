# -*- codiing: utf-8 -*-
# @time      : 2019/4/19 0019 下午 1:13
# @Author    : yu
# @Email     : 
# @File      : test_login.py


import unittest
from ddt import ddt,data,unpack
from api_4.common.http_request import HttpRequest
from api_4.common.project_path import case_path
from api_4.common.do_excel import DoExcel
from api_4.common.my_log import MyLog
from api_4.common.get_data import GetData
from api_4.common.do_mysql import DoMySql

logger=MyLog()
@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试前的准备
        self.t = DoExcel(case_path, 'invest')  #
    def tearDown(self):
        pass

    test_data = DoExcel(case_path, 'invest').read_data('CaseInvest')

    @data(*test_data)
    def test_case(self,case):
        global TestResult
        # test_data = DoExcel(case_path, 'Sheet1').read_data()
        method = case['Method']  # 获取请求方法
        url = case['URL']  # 获取请求地址
        param = eval(case['Params'])  # 获取请求参数


        logger.info('---正在测试{}模块，第{}条测试用例，测试标题:{}---'.format(case['Module'], case['CaseId'], case['Title']))
        logger.info('测试数据是{}'.format(case))
        if case['SQL']!=None:
            query = eval(case['SQL'])['sql']  # 获取sql语句
            before_leaveamount = DoMySql().do_mysql(query, 1)[0]  # 操作数据库 获取项目id值 获取的是个元组  取出元组元素
            print(before_leaveamount)

        resp = HttpRequest().http_request(method, url, param,cookies=getattr(GetData,'cookies'))


        if resp.cookies:
            setattr(GetData,'cookies',resp.cookies)
        #
        # if case['SQL'] != None:
        #     query = eval(case['SQL'])['sql']
        #     after_leaveamount = DoMySql().do_mysql(query, 1)[0]
        #     print(after_leaveamount)

        try:
            if case['SQL'] != None:
                query = eval(case['SQL'])['sql']
                after_leaveamount = DoMySql().do_mysql(query, 1)[0]
                print(after_leaveamount)

                # print(type(after_leaveamount[0]))
                expect_leaveamount = before_leaveamount - int(param['amount'])
                print(expect_leaveamount)
                self.assertEqual(after_leaveamount,expect_leaveamount)
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult='Pass'
        except AssertionError as e:
            logger.error('请求错误，错误是{}'.format(e))
            TestResult = 'Failed'
            raise e
        finally:
            #写回结果
            # t = DoExcel(case_path, 'Sheet1')
            self.t.write_back(case['CaseId'] + 1, 9, resp.text)
            self.t.write_back(case['CaseId'] + 1, 10, TestResult)

        logger.info('测试结果{}'.format(resp.json()))

