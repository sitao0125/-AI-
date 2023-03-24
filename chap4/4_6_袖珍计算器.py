a = float(input("请输入操作数x："))
b = float(input("请输入操作数y："))
operator = input("请输入操作符（+、-、*、/、%）：")

if(b == 0 and (operator == '/' or operator == '%')):
    print("分母为零，异常！")
else:
    if operator == '+': result = a+b
    elif operator == '-': result = a-b
    elif operator == '*': result = a*b
    elif operator == '/': result = a/b
    elif operator == '%': result = a%b
    print("{0} {1} {2}= {3}：".format(a,operator,b,result))
