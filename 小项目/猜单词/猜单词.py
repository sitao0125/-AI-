import random
import sys

isContinue = "Y"
life = 10
words = []
score = 0
record=[]#世界排名


# 游戏初始化
def game_init():
    global life
    global words
    if (level == 1):
        filename="1.txt"
    elif (level == 2):
        filename="2.txt"
        life = 8
    elif (level == 3):
        filename="3.txt"
        life = 5
    #with open(filename,'r',encoding='utf8') as f:
    #words = f.readline()
    #words=words.split()
    try:
        with open(filename,'r',encoding='utf8') as f:
            words=f.readline()
            words = words.split()
    except:
        print("单词库加载失败！")
    else:
        print("单词库加载成功，你可以玩游戏了")






# 菜单
def menu():
    print("-----------------------------------------------------")
    print("-            欢迎参加猜单词游戏！                   -")
    print("-        请把乱序后的字母组成一个单词               -")
    print("-        1、开始游戏                                -")
    print("-        2、查看游戏排名                            -")
    print("-        3、退出游戏                                -")
    print("-----------------------------------------------------")
    try:
        ch1 = int(input("请输入你的选择："))
        if (ch1 == 1):
            return 1
        elif (ch1 == 2):
            return 2
        elif (ch1 == 3):
            return 3
    except:
        pass


def game_start():
    global level
    level = int(input("请选择游戏难度(1、简单 2、一般 3、困难)："))
    while (level < 1 or level > 3):
        print("输入错误！")
        level = int(input("请选择游戏难度(1、简单 2、一般 3、困难)："))
    game_init()
    return "y"


def show_rank():
    print("------------------------------------------------")
    print("-                 游戏排名                     -")


# 猜单词
def guess_word():
    global life
    global words
    global score
    word = random.choice(words)
    words.remove(word)
    answer = word
    jumble = ""
    for i in word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("你有%d条命" % life)
    print("乱序后的单词：", jumble)
    guess = input("请输入你的猜测结果：")
    i = 5
    while (i > 0):
        if (guess != answer):
            print("结果错误，你还有%d次机会" % i)
            guess = input()
            i -= 1
        else:
            print("恭喜你，猜对了！")
            break
    if (i > 0):
        score += 1
    else:
        life -= 1
        print("机会用完，正确单词是%s" % answer)
#读取世界排名
def read_record():
    try:
        with open("record.txt",'r',encoding='utf8') as f:
            record = f.readlines()
            for i in range(len(record)):
                record[i]=record[i].strip()
                record[i]=record[i].split()
    except:
        pass
    return  record
        #print("世界排名读取失败")
#程序入口

record =read_record()

while(1):
    ch1 = menu()
    if (ch1 == 1):
        game_start()
        while (life > 0):
            guess_word()
        print("生命用完，继续加油！")







        
    elif (ch1 == 2):
        show_rank()
    elif (ch1 == 3):
        print("欢迎下次再玩")
sys.exit()

