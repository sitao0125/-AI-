n=int(input("请输入非负整数n:"))
total=1;
if n >0 :
    for i in range(n,0,-1):
        total*=i
    print(total)
else:
    n = input("请输入非负整数n:")



# 输入一个整数n
n = int(input("请输入一个整数："))

# 初始化一个变量num为1
num = 1

# 使用while循环，当n大于等于1时，执行以下操作：
while n >= 1:
  # 将num乘以n，并赋值给num
  num = num * n
  # 将n减去1，并赋值给n
  n = n - 1

# 循环结束后，打印num的值，即为阶乘n
print("阶乘为：", num)