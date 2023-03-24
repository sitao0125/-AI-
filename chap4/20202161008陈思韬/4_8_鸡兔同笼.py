h = int(input("请输入总头数："))
f = int(input("请输入总脚数(必须是偶数)："))

def fun1(h,f):
    tuzi = f/2-h
    ji = h-tuzi
    if(ji < 0 or tuzi  < 0): return '无解，请重新运行测试'
    return ji,tuzi

def fun2(h,f):
    for i in range(0,h+1):
        if(2*i + 4*(h-i) == f):return i,h-i
    return '无解'

if(h>0 and f>0 and f % 2 == 0):
    if fun1(h,f)=='无解，请重新运行测试':
        print("无解，请重新运行测试")
    else:
        print("方法一：鸡：{0}，兔：{1}".format(fun1(h,f)[0],fun1(h,f)[1]))
        print("方法二：鸡：{0}，兔：{1}".format(fun2(h,f)[0],fun2(h,f)[1]))
else:
    print('输入的数据无意义')
