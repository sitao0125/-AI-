import math

a = float(input("输入系数a: "))
b = float(input("输入系数b: "))
c = float(input("输入系数c: "))

if a==0 and b== 0:
    print(f"此方程无解！")
elif a ==  0 and b!=0:
    print(f"此方程的解为：{round(-c/b,1)}")
elif b**2 - 4 * a *c == 0:
    print(f"此方程有两个相等的实根: {round(-b/(2*a),1)}")
elif b**2 - 4 * a *c >0:
    print((f"此方程有两个不等实根 {round( (-b/2*a) + math.sqrt(b**2 - 4 * a * c) / (2 * a),1 )}  "
           f" 和  {round((-b/2*a) - math.sqrt(b**2 - 4 * a * c) / (2 * a),1)}"
           ))
elif b ** 2 - 4 * a * c < 0:
    print((f"此方程有两个不等虚根 {  round(-b/2*a,1)  }+i*{round(math.sqrt( 4 * a * c - b**2) / (2 * a),1)}  "
           f"和{round(-b/2*a,1)} -i * {round(math.sqrt(4 * a * c - b**2) / (2 * a),1)} "))


