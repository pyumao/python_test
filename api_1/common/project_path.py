# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 8:37
# @Author    : yu
# @Email     : 
# @File      : project_path.py

import os

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例的路径
case_path=os.path.join(project_path,'test_case','jiekouceshi.xlsx')
conf_path=os.path.join(project_path,'test_result','test_log','test_case.conf')

if __name__ == '__main__':

    print(project_path)
    print(case_path)
