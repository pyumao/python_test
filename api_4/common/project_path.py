# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 8:37
# @Author    : yu
# @Email     : 
# @File      : project_path.py

import os

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#文件路径
case_path=os.path.join(project_path,'test_case','api_test.xlsx')

#配置文件路径
conf_path=os.path.join(project_path,'conf','case.conf')

#报告路径
report_path=os.path.join(project_path,'test_result','test_result','report.html')

#日志路径
log_path=os.path.join(project_path,'test_result','test_log','test.log')

if __name__ == '__main__':
    print(conf_path)
    print(project_path)
    print(case_path)
    print(report_path)
