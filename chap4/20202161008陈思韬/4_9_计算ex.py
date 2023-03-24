x = int(input("请输入任意实数："))

e = 1
i = 1
t = 1
a = 1
while(a >= 10e-6):
    t *= i
    a = pow(x,i)/t
    e += a
    i += 1

print(f"Pow(e,x)={e}")
