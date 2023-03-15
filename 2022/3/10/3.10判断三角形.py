a = float(input("输入边A: "))
b = float(input("输入边B: "))
c = float(input("输入边C: "))

#检查是否为三角形
if (a + b > c) and (b + c > a) and (c + a > b):

        p = a + b + c

        s = p / 2

        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"三角形的三条边分别是: A:{round(a,1)} B:{round(b,1)} B:{round(c,1)}")
        print(f"三角形周长是： {round(p, 1)}")
        print(f"三角形面积是： {round(area, 1)}")
else:

        print("无法构成三角形")
