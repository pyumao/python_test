# -*- codiing: utf-8 -*-
# @time      : 2019/4/19 0019 下午 10:53
# @Author    : yu
# @Email     : 
# @File      : lean_mysql.py

#操作mysql
#mysql

#pymsql mysql-connector-python
#pip install pymysql
#pip install mysql-connector-python

#navicat 界面工具 链接数据库 来做操作的
#数据库的链接信息：
#47.107.168.87  端口3306  用户名 python 密码 python666

from pymysql import connect
# from MySQLdb import connect

#第一步连接数据库
#提供数据库的信息
db_config={'host':'47.107.168.87',
        'user':'python',
        'password':'python666',
        'port':3306 ,
        'database':'future',
        }

cnn=connect(**db_config)  #建立一个连接


#第二获取游标  获取操作数据库的权限
cursor=cnn.cursor()

#第三步操作数据表
query='select Id, MobilePhone from member where Id<=23528'
cursor.execute(query)

#第四步获取查询结果并打印  readline  readlines
res_1=cursor.fetchone()  #获取一条数据  返回的是一个元组
res_2=cursor.fetchall()  #获取所有数据  返回的是一个列表嵌套元组
print('数据库的查询结果1{}'.format(res_1))
print('数据库的查询结果2{}'.format(res_2))




#增删改 update
# cursor.execute(query)
#cursor.execute('commit')#提交
