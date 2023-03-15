# 定义一个函数来计算Sn
def calcSn(n):
  # 初始化Sn为0
  Sn = 0
  # 从1到n以2为步长循环
  for i in range(1,n+1,2):
    # 如果i是奇数，就加到Sn上
    if i % 4 == 1:
      Sn += i
    # 如果i是偶数，就从Sn中减去
    else:
      Sn -= i
  # 返回Sn
  return Sn

# 测试函数，令n=101
n = 101
print("Sn =", calcSn(n))