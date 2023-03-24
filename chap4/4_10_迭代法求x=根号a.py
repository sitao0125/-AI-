import math

a = int(input("请输入任意实数a(>=0)："))

x = a / 2
y = (x + a/x) / 2

while(abs(y-x) >= pow(10,-6)):
    x = y
    y = (x + a/x) / 2

print(f"{a}的算术平方根={y}")
