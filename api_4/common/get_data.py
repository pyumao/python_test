# -*- codiing: utf-8 -*-
# @time      : 2019/4/19 0019 下午 7:48
# @Author    : yu
# @Email     : 
# @File      : get_data.py

class GetData:
    '''可以动态的获取  更改  删除类的属性值'''
    cookies=None
    loan_id=None
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
    print(delattr(GetData,'cookies'))  #第一个参数是类名 第二个参数是属性的参数名
    print(getattr(GetData,'cookies'))
    print(setattr(GetData,'cookies','1'))
