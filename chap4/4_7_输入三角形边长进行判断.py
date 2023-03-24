a = float(input("请输入三角形的边a："))
b = float(input("请输入三角形的边b："))
c = float(input("请输入三角形的边c："))

if(a > b): a,b = b,a
if(a > c): a,c = c,a
if(b > c): b,c = c,b


if(not(a>0 and b>0 and c>0 and a+b>c)):
    print("此三边无法构成三角形")
else:
    if a == b == c:
        print("该三角形是等边三角形")
    elif(a==b or a==c or b==c):
        print("该三角形是等腰三角形")
    elif(a*a+b*b == c*c):
        print("该三角形是直角三角形")


