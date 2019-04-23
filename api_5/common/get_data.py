# -*- codiing: utf-8 -*-
# @time      : 2019/4/19 0019 下午 7:48
# @Author    : yu
# @Email     : 
# @File      : get_data.py

import re
from api_5.common.read_config import ReadConfig
cf=ReadConfig()
class GetData:
    '''可以动态的获取  更改  删除类的属性值'''
    cookies=None
    # loan_id=None
    normal_user=cf.get('DATA','normal_user')
    normal_pwd=cf.get('DATA','normal_pwd')

def replace(target):
    p2='#(.*?)#'  #圆括号代表正则表达式里面组的概念  ?是限定符
    while re.search(p2,target):
        m=re.search(p2,target)
        key=m.group(1)
        value=getattr(GetData,key)
        target = re.sub(p2,value,target,count=1)
    return target

# t=replace("{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}")
# print(t)

# def re():

if __name__ == '__main__':

    # #类属性
    # print(GetData.cookies)
    # print(GetData().cookies)
    #
    # #类的反射可以动态的查看，增加，删除，更改类的属性值
    #
    # #利用反射方法拿值
    # print(getattr(GetData,'cookies'))  #第一个参数是类名 第二个参数是属性的参数名
    # #判断类的该属性是否存在
    # print(hasattr(GetData,'cookies')) #第一个参数是类名 第二个参数是属性的参数名  返回是布尔值
    # #更改类属性值
    # print(setattr(GetData,'cookies','1'))  #第一个参数是类名 第二个参数是属性的参数名 第三个参数是要设置的新值  无返回值
    # print(getattr(GetData,'cookies'))
    #删除类属性
    # print(delattr(GetData,'cookies'))  #第一个参数是类名 第二个参数是属性的参数名
    # print(getattr(GetData,'cookies'))
    print(setattr(GetData,'cookies','1'))
    print(getattr(GetData,'cookies'))
    print(setattr(GetData,'normal',2))
    print(getattr(GetData,'normal'))
