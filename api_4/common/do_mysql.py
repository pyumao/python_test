# -*- codiing: utf-8 -*-
# @time      : 2019/4/20 0020 上午 11:34
# @Author    : yu
# @Email     : 
# @File      : do_mysql.py

from pymysql import connect
from api_4.common.read_config import ReadConfig


class DoMySql:
    '''读取数据库的数据 进行匹配校验'''


    def do_mysql(self,query,flag=1):
        '''query:sql语句
            flag：标志  1 获取一条数据  2 获取多条数据'''
        sql = eval(ReadConfig().get('SQL', 'mysql'))
        # db_config = {'host': 'test.lemonban.com',
        #              'user': 'test',
        #              'password': 'test',
        #              'port': 3306,
        #              'database': 'future',}
        # print(sql)
        #建立数据库的连接
        cnn=connect(**sql)

        #获取数据库的操作权限
        cursor=cnn.cursor()

        #操作数据库
        cursor.execute(query)

        #获取查询结果并打印
        if flag==1:
            res=cursor.fetchone()  #返回元组
        else:
            res=cursor.fetchall()  #返回列表嵌套元组
        return res

if __name__ == '__main__':
    query = 'select LeaveAmount from member where MobilePhone=18688775656'
    res=DoMySql().do_mysql(query,1)
    print(type(res))
    print('数据库查询结果是{}'.format(res))
    print(res[0])
    print(type(res[0]))