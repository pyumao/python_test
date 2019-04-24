# -*- codiing: utf-8 -*-
# @time      : 2019/3/12 0012 上午 11:36
# @Author    : yu
# @Email     : 
# @File      : 模块导入.py

#导入模块  import 导入  export 导出
#导入模块的时候  一层一层的定位  除开顶级目录

#第一种方法  import
# import week_5.class_0123.add_1  #导入指定模块的函数
#
# res=week_5.class_0123.add_1.add(1,3)
#
# print(res)

# #第二种方法 取别名 import ···as
# import week_5.class_0123.add_1 as s
#
# res=s.add(2,5)
# print(res)

#第三种方法 from  ····import

# from week_5.class_0123 import add_1 #具体到函数名|模块名
# res=add_1.add_2(5,33,2)
# print(res)

#调用模块的多个函数  和所有函数
# from week_5.class_0123.add_1 import add,add_2 #调用写出的两个函数
# from week_5.class_0123.add_1 import *           #调用所有函数
# res=add(5,3)
# res=add_2(4,2,3)

#第四种方式  from`````import ````as
from week_5.class_0123.add_1 import add_2 as d5
res=d5(1,3,4,56,6,2)
print(res)

i