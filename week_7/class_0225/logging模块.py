# -*- codiing: utf-8 -*-
# @time      : 2019/3/23 0023 下午 6:19
# @Author    : yu
# @Email     : 
# @File      : logging模块.py

#什么是日志
#日志的作用
#日志的等级  debug info warning error critical/fatal（致命的）

import logging

#日志搜集器logger   root logger
#日志输出渠道dandlers 控制台console file txt test.log


#1.定义一个日志搜集器并命名  并且设置级别  getLogger

my_logger=logging.getLogger('python')
my_logger.setLevel('DEBUG')

#2.指定输出去渠道StreamHandler FileHandler
formatter=logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息]：%(message)s')
ch=logging.StreamHandler()
ch.setLevel('INFO')
ch.setFormatter(formatter)  #设置输出格式

fh=logging.FileHandler('test.log',encoding='utf-8')
fh.setLevel('INFO')
fh.setFormatter(formatter)


#3.对接收集器和输出渠道  z最终输出信息是两者的交集
my_logger.addHandler(ch)
my_logger.addHandler(fh)


my_logger.debug('this is a debug')
my_logger.info('this is a info')
my_logger.warning('this is a warning')
my_logger.error('this is a error')
my_logger.critical('this is a cretical')

my_logger.removeHandler(fh)
my_logger.removeHandler(ch)  #记得移除