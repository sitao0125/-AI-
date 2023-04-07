def is_prime(n):
    if n<2:return False
    i=2
    while i*i <=n:
        if n%i == 0:return False
        i += 1
    return True
#测试
for i in range(100):#判断，输入1~99中的素数
    if is_prime(i):print(i,end=' ')
