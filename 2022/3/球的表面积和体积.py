import math
r=float(input("请输入球的半径："))
s=4*math.pi*r*r
v=(4/3)*math.pi*r*r*r
print(str.format("球的发表面积为:{0:2.2f},体积为：{1:2.2f}",s,v))
