def gcd(p,q):#使用递归函数计算p和q的最大公约数
    if q==0:
        return p
    print(p,q)#如果q=0，返回p
    return gcd(q,p%q)# 否则递归
#测试代码
p=int(input()) # p=命令行第一个参数
q=int(input()) # q=命令行第二个参数

print(gcd(p,q))
