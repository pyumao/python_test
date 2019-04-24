# -*- codiing: utf-8 -*-
# @time      : 2019/4/17 0017 下午 9:24
# @Author    : yu
# @Email     : 
# @File      : my_log.py

import logging
from api_3.common.project_path import log_path
from api_3.common.read_config import ReadConfig

class MyLog():

    def my_logger(self,level,msg):

        my_logger=logging.getLogger(fn)
        my_logger.setLevel(ll)

        #2.指定输出去渠道StreamHandler FileHandler
        formatter=logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息]：%(message)s')
        ch=logging.StreamHandler()
        ch.setLevel(cl)
        ch.setFormatter(formatter)  #设置输出格式

        fh=logging.FileHandler(log_path,encoding='utf-8')
        fh.setLevel(fl)
        fh.setFormatter(formatter)


        #3.对接收集器和输出渠道  z最终输出信息是两者的交集
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)  #记得移除

    def debug(self,msg):
        self.my_logger('DEBUG',msg)
    def info(self,msg):
        self.my_logger('INFO',msg)
    def warning(self,msg):
        self.my_logger('WARNING',msg)
    def error(self,msg):
        self.my_logger('ERROR',msg)
    def caritical(self,msg):
        self.my_logger('aritical',msg)
#

t=ReadConfig()
fn=t.get('LOG','file')
ll=t.get('LOG','logger')
cl=t.get('LOG','ch')
fl=t.get('LOG','fh')

if __name__ == '__main__':
    logger=MyLog()
    logger.error('糟糕的结果')

