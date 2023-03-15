#单分支结构
import math
x=float(input("请输入x："))
if x > 0 and x == 0:
   y= ((x**2)-3*x)/(x+1) +(2*math.pi)+ math.sin(x)
if x < 0:
    y =math.log(-5 * x) + 6 * math.sqrt(abs(x) + math.e ** 4) - ( (x + 1) ** 3 )
print(f"方法一：x = {round(x, 1)}, y = {round(y, 14)}，")

#双分支结构

if x > 0 and x == 0:
   y= ((x**2)-3*x)/(x+1) +(2*math.pi)+ math.sin(x)
else:
    y =math.log(-5 * x) + 6 * math.sqrt(abs(x) + math.e ** 4) - ( (x + 1) ** 3 )
print(f"方法二：x = {round(x, 1)}, y = {round(y, 14)}，")

#条件运算符语句
# 根据x是否大于或等于0，选择不同的表达式计算y的值
y = ((x**2)-3*x)/(x+1) +(2*math.pi)+ math.sin(x) if x > 0 or x == 0 \
    else math.log(-5 * x) + 6 * math.sqrt(abs(x) + math.e ** 4) - ( (x + 1) ** 3 )
print(f"方法三：x = {round(x, 1)}, y = {round(y, 14)}，")
