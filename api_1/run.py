# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 6:43
# @Author    : yu
# @Email     : 
# @File      : run.py

from class_6.class_0220.do_excel import DoExcel
from api_1.common.http_request import HttpRequest
from api_1.common.project_path import case_path

file_name = case_path
sheet_name = 'Sheet1'
test_data = DoExcel(file_name,sheet_name).read_data()
print(test_data)
for i in test_data:
    method=i['Method']  #获取请求方法
    url=i['URL']        #获取请求地址
    param=eval(i['Params'])  #获取请求参数

    print('---正在测试{}模块，第{}条测试用例，测试标题:{}---'.format(i['Module'],i['CaseId'],i['Title']))
    resp = HttpRequest().http_request(method, url, param)
    print('测试结果{}'.format(resp.json()))

    #判断测试结果
    if resp.json()==eval(i['ExpectedResult']):
        TestResult='Pass'
    else:
        TestResult = 'Fail'
    print('该条测试用例结果是{}'.format(TestResult))

    #写回测试实际结果
    t=DoExcel(file_name,sheet_name)
    t.write_back(i['CaseId']+1,8,resp.text)
    t.write_back(i['CaseId']+1,9,TestResult)

