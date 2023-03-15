# 导入random模块
import random

# 生成两个0~100之间的随机整数a和b
a = random.randint(0, 100)
b = random.randint(0, 100)

# 打印a和b
print("整数1 =", a)
print("整数2 =", b)

# 如果a和b相等，则重新生成并打印它们
while a == b:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print("重新生成：")
    print("整数1 =", a)
    print("整数2 =", b)

# 让m为较大的数，n为较小的数
if a > b:
    m = a
    n = b
else:
    m = b
    n = a

# 使用辗转相除法求最大公约数
r = m % n
while r != 0:
    m = n
    n = r
    r = m % n

# 计算最小公倍数（注意使用整除运算符）
minnum = (a * b) // m

# 打印最大公约数和最小公倍数
print("最大公约数 =", m)
print("最小公倍数 =", minnum)