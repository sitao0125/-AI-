from random import  randint as r
a=r(0,100)
b=r(0,100)
c=r(0,100)

#1
print("排序方法一")
print(str.format("原始：{0}，{1}，{2}", a, b, c))
a1=a
b1=b
c1=c
if(a1 > b1): a1,b1 = b1,a1
if(a1 > c1): a1,c1 = c1,a1
if(b1 > c1): b1,c1 = c1,b1

print(str.format("从小到大排序：{0}，{1}，{2}", a1, b1, c1))

print()

#2
print("排序方法二")
print(str.format("原始：{0}，{1}，{2}", a, b, c))
max1=max(a,b,c)
min1=min(a,b,c)
mid=a+b+c -max1 - min1

print(str.format("从小到大排序：{0}，{1}，{2}", min1, mid, max1))

#3
print("排序方法三")
print(str.format("原始：{0}，{1}，{2}", a, b, c))
e=sorted([a,b,c])
print(f"从小到大排序：{e}")
