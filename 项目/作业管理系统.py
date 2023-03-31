def menu():
    print("==============================================")
    print("陈思韬")
    print("1、例1.7:hello world")
    print("2、例1.9:hello world")
    print("3、例1.2:hello world")
    print("==============================================")
    choice=int(input("请输入序号:"))
    while(choice < 0 or choice > 4):
        print("输入错误!")
        menu()
    return choice



def liti_7():
    print("例1.7、hello world:")
    print("hello world")

def liti8_4():
    def print_star():
        print("*")
    n=int(input())
    for i in range(1,2*n):
        print_star()
        
def sign():
    print("陈思韬")

while(1):
    ch=menu()
    if(ch==1):
        liti_7()
    elif(ch==3):
        liti8_4()
    elif(ch==0):
        print("程序结束，欢迎下次再来")
        break
    sign()
