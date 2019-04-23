# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 10:01
# @Author    : yu
# @Email     : 
# @File      : read_config.py

from configparser import ConfigParser
from api_5.common.project_path import conf_path
# file_name=conf_path

class ReadConfig:

    def __init__(self):
        self.cf=ConfigParser()
        self.cf.read(conf_path,encoding='utf-8')

    def get_int(self,section,option):
        '''从配置文件里面获取一个整数'''
        res=self.cf.getint(section,option)
        return res

    def get_float(self,section,option):
        '''从配置文件里面获取一个浮点数'''
        res=self.cf.getfloat(section,option)
        return res

    def get_boolean(self,section,option):
        '''从配置文件里面获取一个布尔值'''
        res=self.cf.getboolean(section,option)
        return res

    def get(self,section,option):
        '''从配置文件里面获取一个字符串'''
        res=self.cf.get(section,option)
        return res

    def get_data(self,section,option):
        '''从配置文件里面获取一个其他类型字典 元组 列表'''
        res=self.cf.get(section,option)
        return eval(res)

if __name__ == '__main__':
    print(conf_path)
    t=ReadConfig()
    # print(t.get('CASE','button'))
    print(t.get_int('CASE','year'))
    print(type(t.get_int('CASE','year')))
    print(t.get('CaseRegister','caseid'))
    print(t.get('CaseAll','caseid'))
    print(type(eval(t.get('CaseAll','caseid'))['register']))
    print(type(t.get_data('SQL','mysql')))