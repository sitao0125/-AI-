#import random
from random import random as r
def randomarray(n):#生成由n个随机数构成的列表
    a=[]
    for i in range(n):
        a.append(r())#a.append(random.random())
    return a
#测试代码
b =randomarray(5)# 生成由五个随机数构成的列表
for i in b:print(i)#输出列表中每个元素
