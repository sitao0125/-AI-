pi=3.141592653589793#全局变量
e=2.718281828459048#全局变量
def my_func():
    global pi#全局变量
    pi=3.14
    print('global pi = ',pi)#输出全局变量的值
    e=2.718
    print('local e = ',e)
#测试代码
print('module pi = ',pi)#输出全局变量的值
print('module e = ',e)
my_func()#调用函数
print('module pi = ',pi)#输出全局变量的值，该值在函数中已被更改
print('module e= ',e)#输出全局变量的值
