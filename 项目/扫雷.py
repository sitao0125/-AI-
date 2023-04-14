from random import randint as r
w = 9
h = 9
lei_num = 10
mine_map=[]
mine_number=[]
mine_sign=[]       #地雷显示
flag=0
on=1
def game_init():   #游戏初始化设置
    global w
    global h
    global lei_num
    level = int(input("请选择难度：1、简单（9*9）2、中等（16*16）3、困难（25*15）4、自定义难度："))
    if(level ==1):
        w = 9
        h = 9
        lei_num = 10
    elif(level ==2):
        w = 16
        h = 16
        lei_num = 40
    elif(level ==3):
        w = 25
        h = 15
        lei_num = 80
    elif(level ==4):
        w = int(input("请输入宽度："))
        h = int(input("请输入高度："))
        lei_num = int(input("请输入雷数："))

def mine_init(a): #地雷的初始化
    b = []
    for i in range(lei_num):
        b.append(1)
    for i in range(w * h - lei_num):
        b.append(0)
    for i in range(h):
        a.append([])
        for j in range(w):
            t = r(0,len(b) - 1)
            t = b.pop(t)
            a[i].append(t)
def mine_sign_init(a):
    for i in range(h):
        a.append([])
        for j in range(w):
            a[i].append('█')
            
def inmap(i,j):
    if(i<0 or j<0 or i>w-1 or j>h-1):
        return False
    return True

def mine_count(a):
    for i in range(h):
        a.append([])
        for j in range(w):
            c=0
            q=i-1
            for k in range(j-1,j+2):
                if(inmap(q,k)):
                    if(mine_map[q][k]==1):
                        c+=1
            q=i
            for k in range(j-1,j+2,2):
                if(inmap(q,k)):
                    if(mine_map[q][k]==1):
                        c+=1
            q=i+1
            for k in range(j-1,j+2):
                if(inmap(q,k)):
                    if(mine_map[q][k]==1):
                        c+=1
            a[i].append(c)
def show_lei():  #显示地雷
    print("  ",end = " ")
    for j in range(w):
        print("%2d"%(j+1),end = " ")
    print()
    for i in range(h):
        print("%2d"%(i+1),end = " ")
        for j in range(w):
            if(mine_map[i][j] ==1):
                print("●",end=" ")
            else:
                print("█",end=" ")
        print()

def show():
    print("  ",end = " ")
    for j in range(w):
        print("%2d"%(j+1),end = " ")
    print()
    for i in range(h):
        print("%2d"%(i+1),end = " ")
        for j in range(w):
            print("%2c"%mine_sign[i][j],end=' ')
        print()

def sweep():
    global on
    global mine_sign
    global flag
    i = int(input("请输入行数："))-1
    j = int(input("请输入列数："))-1
    while(i<0 or j<0 or i>w-1 or j>h-1):
        print("输入错误")
        i = int(input("请输入行数："))-1
        j = int(input("请输入列数："))-1
    xz = int(input("1、翻开 2、插旗"))
    if(xz ==1):
        if(mine_map[i][j]==1):
            print("失败")
            show_lei()
            on=0
    elif(xz==2):
        mine_sign[i][j]="▲"
        flag +=1
        if(flag == lei_num):
            for i in range(h):
                for j in range(w):
                    if((mine_map[i][j]==0 and mine_sign[i][j] =="▲")or(mine_map[i][j]==i and mine_sign[i][j] !="▲")):
                        print("标记错误，游戏结束")
                    else:
                        print("你赢了，游戏结束")
        
        
    
game_init()#游戏初始化
mine_init(mine_map)#地雷初始化
mine_count(mine_number)#数地雷
mine_sign_init(mine_sign)#地雷显示初始化
while(on):
    show()
    sweep()
