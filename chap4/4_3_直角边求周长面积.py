import math
a=int(input("请输入三角形的一条直角边A(>0):"))
b=int(input("请输入三角形的一条直角边B(>0):"))
c=math.sqrt((a**2)+(b**2))
print(f"直角三角形的三边分别为：a={round(a,1)},b={round(b,1)},c={round(c,1)}")
print(f"三角形的周长={round(a+b+c,1)}，面积={round((a*b)/2,1)}")
sina = a/c
sinb = b/c

a_degree = round(math.asin(sina) * 180 / math.pi,0)
b_degree = round(math.asin(sinb) * 180 / math.pi,0)

print("三角形直角边a的度数：{0}，b的度数：{1}".format(a_degree,b_degree))
