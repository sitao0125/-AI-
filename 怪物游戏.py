from random import randint as r
class gw:  #定义怪物
    count = 0#静态属性
    def  __init__(self,i):
        self.num = i#num是对象的属性
        self.blood = r(1,5)
        gw.count += 1
        
    def kill(self,name,i):
        self.count -=1
        if(self.blood <1):
            print("%d号怪物被%s打死了"%(self.num,name))
            gw.count -= 1
class wj:
    def __init__(self,name):
        self.blood=100
        self.fl=800
        self.name=name

#gw1 = gw(1)
def czgw(n,g):
    for i in range(n):
        g.append(gw(i+1))

def hz(n,g):
    print("你可以打的怪物:",end="")
    for i in range(n):
        if(g[i].blood > 0):  #怪物还活着
            print(g[i].num,end= "")
    print()

def gj(g):
    i=int(input("你想打几号怪物")) - 1
    g[i].kill(name,5)


name=input("请输入玩家姓名")
wj1 = []
wj1.append(wj(name))

level=int(input("请选择难度:1、新手，2、普通，3、困难"))
if(level==1):
    n=5
elif(level==2):
    n=10
else:
    n=30

gw1=[]          # 创造怪物
czgw(n,gw1)

while(gw.count > 0):
    hz(n,gw1)
    gj(gw1)

