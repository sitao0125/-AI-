print("20202161008 陈思韬")  # 打印学号和姓名
from random import randint as r  # 导入随机数模块

w = 9  # 设置默认宽度为9
h = 9  # 设置默认高度为9
lei_num = 10  # 设置默认雷数为10
mine_map = []  # 创建一个空列表，用来存储地雷的位置
mine_number = []  # 创建一个空列表，用来存储每个格子周围的地雷数
mine_sign = []  # 创建一个空列表，用来存储地雷的显示状态
flag = 0  # 设置一个标志变量，用来判断游戏是否结束
on = 1  # 设置一个开关变量，用来控制游戏的进行
t = 0  # 设置一个计时变量，用来记录游戏的时间


def game_init():  # 定义一个函数，用来初始化游戏的难度设置
    global w  # 声明全局变量w
    global h  # 声明全局变量h
    global lei_num  # 声明全局变量lei_num
    level = int(input("请选择难度：1、简单（9*9）2、中等（16*16）3、困难（25*15）4、自定义难度："))  # 让用户输入难度等级
    if (level == 1):  # 如果用户选择简单难度
        w = 9  # 宽度为9
        h = 9  # 高度为9
        lei_num = 10  # 雷数为10
    elif (level == 2):  # 如果用户选择中等难度
        w = 16  # 宽度为16
        h = 16  # 高度为16
        lei_num = 40  # 雷数为40
    elif (level == 3):  # 如果用户选择困难难度
        w = 25  # 宽度为25
        h = 15  # 高度为15
        lei_num = 80  # 雷数为80
    elif (level == 4):  # 如果用户选择自定义难度
        w = int(input("请输入宽度："))  # 让用户输入宽度
        h = int(input("请输入高度："))  # 让用户输入高度
        lei_num = int(input("请输入雷数："))  # 让用户输入雷数


def mine_init(a):  # 定义一个函数，用来初始化地雷的位置
    b = []  # 创建一个空列表，用来存储地雷和空白的标记
    for i in range(lei_num):
        b.append(1)  # 在b中添加lei_num个1，表示地雷的标记
    for i in range(w * h - lei_num):
        b.append(0)  # 在b中添加w*h-lei_num个0，表示空白的标记
    for i in range(h):
        a.append([])  # 在a中添加h个空列表，表示h行格子
        for j in range(w):
            t = r(0, len(b) - 1)  # 从b中随机选取一个下标t
            t = b.pop(t)  # 从b中弹出下标为t的元素，并赋值给t，这样可以保证不重复选取元素
            a[i].append(t)  # 把t添加到a的第i行第j列，表示该格子是否有地雷


def mine_sign_init(a):  # 定义一个函数，用来初始化地雷的显示状态
    for i in range(h):
        a.append([])  # 在a中添加h个空列表，表示h行格子
        for j in range(w):
            a[i].append('█')  # 把'█'添加到a的第i行第j列，表示该格子未被点击


def inmap(i, j):  # 定义一个函数，用来判断一个坐标是否在地图范围内
    if (i < 0 or j < 0 or i > w - 1 or j > h - 1):
        return False  # 返回False，表示不在地图范围内
    return True  # 返回True，表示在地图范围内


def mine_count(a):  # 定义一个函数，用来计算每个格子周围的地雷数
    for i in range(h):
        a.append([])  # 在a中添加h个空列表，表示h行格子
        for j in range(w):
            c = 0  # 设置一个计数变量，用来记录周围的地雷数
            q = i - 1  # 设置一个临时变量，表示当前格子的上一行
            for k in range(j - 1, j + 2):  # 遍历当前格子的左上、上、右上三个格子
                if (inmap(q, k)):  # 如果这三个格子在地图范围内
                    try:
                        if (mine_map[q][k] == 1):  # 如果这三个格子有地雷
                            c += 1  # 计数变量加一
                    except:
                        pass
            q = i  # 设置临时变量为当前行
            for k in range(j - 1, j + 2, 2):  # 遍历当前格子的左、右两个格子
                if (inmap(q, k)):  # 如果这两个格子在地图范围内
                    try:
                        if (mine_map[q][k] == 1):  # 如果这两个格子有地雷
                            c += 1  # 计数变量加一
                    except:
                        pass
            q = i + 1  # 设置临时变量为当前格子的下一行
            for k in range(j - 1, j + 2):  # 遍历当前格子的左下、下、右下三个格子
                if (inmap(q, k)):  # 如果这三个格子在地图范围内
                    try:
                        if (mine_map[q][k] == 1):  # 如果这三个格子有地雷
                            c += 1  # 计数变量加一
                    except:
                        pass
            a[i].append(c)  # 把计数变量添加到a的第i行第j列，表示该格子周围的地雷数


def show_lei():  # 定义一个函数，用来显示地雷的位置
    for i in range(h):
        print("  ", end=" ")  # 打印两个空格，用来对齐
        for j in range(w):
            if (mine_map[i][j] == 1):  # 如果该格子有地雷
                print("¤", end=" ")  # 打印地雷的符号
            else:
                print("█", end=" ")  # 打印空白的符号
        print()  # 换行


def str_change(a):  # 定义一个函数，用来把数字转换成对应的字符
    if (a == 1):  # 如果数字是1
        s = '①'  # 字符是①
    elif (a == 2):  # 如果数字是2
        s = '②'  # 字符是②
    elif (a == 3):  # 如果数字是3
        s = '③'  # 字符是③
    elif (a == 4):  # 如果数字是4
        s = '④'  # 字符是④
    elif (a == 5):  # 如果数字是5
        s = '⑤'  # 字符是⑤
    elif (a == 6):  # 如果数字是6
        s = '⑥'  # 字符是⑥
    elif (a == 7):  # 如果数字是7
        s = '⑦'  # 字符是⑦
    elif (a == 8):  # 如果数字是8
        s = '⑧'  # 字符是⑧
    else:  # 如果数字是0或其他值
        s = '□'  # 字符是□，表示空白格子
    return s  # 返回字符


def show():  # 定义一个函数，用来显示游戏界面
    print("  ", end=" ")  # 打印两个空格，用来对齐
    for j in range(w):
        print("%2d" % (j + 1), end=" ")  # 打印每一列的序号，占两个字符位，右对齐，中间有空格隔开
    print()  # 换行
    for i in range(h):
        print("%2d" % (i + 1), end=" ")  # 打印每一行的序号，占两个字符位，右对齐，中间有空格隔开
        for j in range(w):
            print("%2s" % mine_sign[i][j], end="")  # 打印每个格子的显示状态，占两个字符位，右对齐，没有空格隔开
        print()  # 换行


def sweep_8(i, j):  # 定义一个函数，用来翻开一个格子周围的八个格子（包括自己）
    mine_sign[i][j] = str_change(mine_number[i][j])  # 把当前格子的显示状态改为周围地雷数对应的字符
    q = i - 1  # 设置一个临时变量，表示当前格子的上一行
    for k in range(j - 1, j + 2):  # 遍历当前格子的左上、上、右上三个格子
        if (inmap(q, k)):  # 如果这三个格子在地图范围内
            mine_sign[q][k] = str_change(mine_number[q][k])  # 把这三个格子的显示状态改为周围地雷数对应的字符
    q = i  # 设置临时变量为当前行
    for k in range(j - 1, j + 2, 2):  # 遍历当前格子的左、右两个格子
        if (inmap(q, k)):  # 如果这两个格子在地图范围内
            mine_sign[q][k] = str_change(mine_number[q][k])  # 把这两个格子的显示状态改为周围地雷数对应的字符
    q = i + 1  # 设置临时变量为当前格子的下一行
    for k in range(j - 1, j + 2):  # 遍历当前格子的左下、下、右下三个格子
        if (inmap(q, k)):  # 如果这三个格子在地图范围内
            mine_sign[q][k] = str_change(mine_number[q][k])  # 把这三个格子的显示状态改为周围地雷数对应的字符


def sweep():  # 定义一个函数，用来执行扫雷的操作
    global on  # 声明全局变量on，表示游戏是否进行中
    global mine_sign  # 声明全局变量mine_sign，表示地雷的显示状态
    global mine_map  # 声明全局变量mine_map，表示地雷的位置
    global mine_number  # 声明全局变量mine_number，表示每个格子周围的地雷数
    global flag  # 声明全局变量flag，表示游戏是否胜利
    global t  # 声明全局变量t，表示游戏是否开始
    i = int(input("请输入行数：")) - 1  # 让用户输入行数，并减一，因为列表的下标从0开始
    j = int(input("请输入列数：")) - 1  # 让用户输入列数，并减一，因为列表的下标从0开始
    while (i < 0 or j < 0 or i > w - 1 or j > h - 1):  # 如果用户输入的坐标不在地图范围内
        print("输入错误")  # 打印错误提示
        i = int(input("请输入行数：")) - 1  # 重新让用户输入行数，并减一，因为列表的下标从0开始
        j = int(input("请输入列数：")) - 1  # 重新让用户输入列数，并减一，因为列表的下标从0开始
    xz = int(input("1、翻开 2、插旗："))  # 让用户选择操作类型，1表示翻开格子，2表示插旗或取消插旗
    while (mine_map[i][j] == 1 and t == 0):  # 如果用户第一次点击的是地雷（t==0表示第一次点击）
        mine_map = []  # 清空地雷位置列表
        mine_number = []  # 清空每个格子周围的地雷数列表
        mine_sign = []  # 清空地雷显示状态列表
        mine_init(mine_map)  # 重新初始化地雷位置列表
        mine_count(mine_number)  # 重新计算每个格子周围的地雷数列表
        mine_sign_init(mine_sign)  # 重新初始化地雷显示状态列表
    t = 1  # 设置t为1，表示游戏已经开始，不再重新初始化列表
    if (xz == 1):  # 如果用户选择翻开格子
        if (mine_map[i][j] == 1):  # 如果该格子有地雷
            print("你踩雷了，游戏失败！")  # 打印失败提示
            show_lei()  # 显示所有地雷的位置
            on = 0  # 设置on为0，表示游戏结束
        else:  # 如果该格子没有地雷
            if (mine_number[i][j] == 0):  # 如果该格子周围没有地雷
                sweep_8(i, j)  # 翻开该格子周围的八个格子（包括自己）
            else:  # 如果该格子周围有地雷
                mine_sign[i][j] = str_change(mine_number[i][j])  # 把该格子的显示状态改为周围地雷数对应的字符
    elif (xz == 2):  # 如果用户选择插旗或取消插旗
        if (mine_sign[i][j] == '█'):  # 如果该格子未被点击
            mine_sign[i][j] = '▲'  # 把该格子的显示状态改为插旗的符号
        elif (mine_sign[i][j] == '▲'):  # 如果该格子已经插旗
            mine_sign[i][j] = '█'  # 把该格子的显示状态改为未被点击的符号
    flag = 0  # 设置flag为0，表示游戏是否胜利
    for i in range(h):
        for j in range(w):
            if (mine_map[i][j] == 1 and mine_sign[i][j] != '▲'):  # 如果有地雷没有被插旗
                flag = 1  # 设置flag为1，表示游戏没有胜利
    if (flag == 0):  # 如果flag为0，表示游戏胜利
        print("恭喜你，游戏胜利！")  # 打印胜利提示
        show_lei()  # 显示所有地雷的位置
        on = 0  # 设置on为0，表示游戏结束


game_init()  # 调用函数，初始化游戏难度设置
mine_init(mine_map)  # 调用函数，初始化地雷位置列表
mine_count(mine_number)  # 调用函数，计算每个格子周围的地雷数列表
mine_sign_init(mine_sign)  # 调用函数，初始化地雷显示状态列表

while (on):  # 当on为真时，表示游戏进行中，循环执行以下操作
    show()  # 调用函数，显示游戏界面
    sweep()  # 调用函数，执行扫雷操作
