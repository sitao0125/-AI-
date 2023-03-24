n = int(input("请输入一个整数："))

# 创建一个空列表
a = []

for i in range(n):
    # 创建一个新行
    row = [1] * (i + 1)
    # 循环遍历前面的行以填充值
    for j in range(1, i):
        row[j] = a[i-1][j-1] + a[i-1][j]
    # 将新行添加到列表中
    a.append(row)

# 打印三角形
for row in a:
    print(' '.join([str(elem) for elem in row]).center(n*2))