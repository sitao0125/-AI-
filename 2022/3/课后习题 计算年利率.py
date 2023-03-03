def getValue(b,r,n):  #分别代表本金，年利率，年数 ，v：最终受益
    v=b*((1+r/100)**n)
    return v


b=float(input("请输入本金"))
r=float(input("请输入年利率"))
n=int(input("请输入年数"))
total =getValue(b,r,n)
print(total)
print(str.format("本金利率和为:{0:2.2f}",total))
