import random
ch=10
a=int(input("请输入数字范围"))
t=random.randrange(0,a+1)
print("请输入一个0-",a,"的数字")
num=int(input())
ch=ch-1
while(num!=t and ch >0):
    if(num>t):
                   print("大了，请输入一个0-",a,"的数字：,你还剩",ch,"次机会")
                   num=int(input())
                   ch=ch-1
    else:
                   print("小了，请输入一个0-:",a,"的数字：，你还剩",ch,"次机会")
                   num=int(input())
                   ch=ch-1
if(num==t):
    print("恭喜答对了")
else:
    print("机会用尽，正确数字是：",t)
