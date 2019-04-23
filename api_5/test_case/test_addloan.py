# -*- codiing: utf-8 -*-
# @time      : 2019/4/19 0019 下午 1:13
# @Author    : yu
# @Email     : 
# @File      : test_login.py


import unittest
from ddt import ddt,data,unpack
from api_5.common.http_request import HttpRequest
from api_5.common.project_path import case_path
from api_5.common.do_excel import DoExcel
from api_5.common.my_log import MyLog
from api_5.common.get_data import GetData
from api_5.common.do_mysql import DoMySql
from api_5.common import get_data

logger=MyLog()
@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试前的准备
        self.t = DoExcel(case_path, 'addloan')  #
    def tearDown(self):
        pass

    test_data = DoExcel(case_path, 'addloan').read_data('CaseAddloan')

    @data(*test_data)
    def test_case(self,case):
        global TestResult
        # test_data = DoExcel(case_path, 'Sheet1').read_data()
        method = case['Method']  # 获取请求方法
        url = case['URL']  # 获取请求地址

        #参数化项目id 判断请求参数中是否参数化项目id 存在则替换成前一条用例所得到的项目id
        # if case['Params'].find('loanid')!=-1:
        #     param=eval(case['Params'].replace('loanid',str(getattr(GetData,'loan_id'))))
        #     # print(param['id'])
        # else:
        #     param = eval(case['Params'])  # 获取请求参数

        #参数化  获取请求参数
        param=eval(get_data.replace(case['Params']))
        # print(param)
        if case['SQL']!=None:
            sql = get_data.replace(case['SQL'])
        # query = eval(sql)['sql']
        # print(query)
        # print(sql)
        # print(type(sql))
        logger.info('---正在测试{}模块，第{}条测试用例，测试标题:{}---'.format(case['Module'], case['CaseId'], case['Title']))
        logger.info('测试数据是{}'.format(case))

        resp = HttpRequest().http_request(method, url, param,cookies=getattr(GetData,'cookies')) #完成http请求

        if case['CaseId'] == 1:
            query = eval(sql)['sql']  # 获取sql语句
            id = DoMySql().do_mysql(query, 1)[0]  # 操作数据库 获取项目id值 获取的是个元组  取出元组元素
            setattr(GetData, 'normal_memberid', str(id))  # 动态获取项目id值
            print(id)
        if case['CaseId']==2:
            query=eval(sql)['sql']  #获取sql语句
            loan_id=DoMySql().do_mysql(query,1)[0]  #操作数据库 获取项目id值 获取的是个元组  取出元组元素
            setattr(GetData,'loanid',str(loan_id))  #动态获取项目id值
            print(loan_id)
        if resp.cookies:
            setattr(GetData,'cookies',resp.cookies)
        try:
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

