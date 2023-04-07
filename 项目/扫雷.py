from random import randint as r
w=9
h=9
mine_num=10
mine_map=[]
def game_init():  #游戏的初始化设置
    global w
    global h
    global mine_num   
    level=int(input("请选择难度:1、简单(9*9),2、一般(16*16),3、高级(30*16),4、自定义"))
    if (level ==1):
        w=9
        h=9
        mine_num=10
    elif(level == 2):
        w=16
        h=16
        mine_num=40
    elif(level == 3):
        w=30
        h=16
        mine_num = 99
    elif(level ==4):
        w=int(input("请输入宽度"))
        h=int(input("请输入高度"))
        mine_num = int(input("请输入雷数"))


def mine_init(a):   #地雷的初始化
    b = []
    for i in range(mine_num):
        b.append(1)
    for i in range(w*h - mine_num):
        b.append(0)
    #print(b)
    for i in range(h):
        a.append([])
        for j in range(w):
            t=r(0,len(b) - 1)
            t=b.pop(t)
            a[i].append(t)

def show_mine():#显示地雷
    print(" ",end = " ")
    for j in range(w):
        print("%2d"%(j+1),end=" ")
    print()
    for i in range(h):
        print("%2d"%(i+1),end=" ")
        for j in range(w):
            if (mine_map[i][j]==1):
                print("雷",end=" ")
            else:
                print("□",end=" ")
        print()

def show():
    print(" ",end=" ")
    for j in range(w):
        print("%2d"%(j+1),end=" ")
        print()
        for i in range(h):
            print("%2d"%(i+1),end=" ")
            for j in range(w):
                print("□",end= " ")
            print()
game_init()
mine_init(mine_map)
show_mine()
