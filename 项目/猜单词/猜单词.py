import random

#游戏初始化
def gameinit():
    global life
    if (level == 1):
        life=10
        words=[]
    elif(level ==3):
        life=8
        words=[]
    elif(level == 3):
        life=5
        words=[]
    return words
 
#菜单
def menu(): #将单词难度分类
    print("********************************************************************")
    print("                      ******欢迎参加猜单词游戏******                ")
    print("                       把乱序后的字母组成一个单词                   ")
    print("                                开始游戏                            ") 
    choice=input("请输入你要选择的游戏难度   1、简单   2、 困难   3、地狱")
    if choice == 1:
            return 1
    elif choice == 2:
            return 2
    elif choice == 3:
            return 3
    else:
            print("你输入的格式不正确，请输入1,2,3中的数字来选择难度")


def game_start(words):
    ch=int(input("请选择难度(1、简单，2、普通，3、困难):")
           while (ch < 1 or ch > 3):
           print("输入错误！")
           ch=menu()
    words=game_init()

def show_rank():
           print("***********************************************")
           print("*               世界排名                      *")


#猜单词
def guess_word():
    global life
    global words
    word = random.choice(words)
    words.remove(word)
    answer=word
    jumble = ""
    for i in word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + " "+word [(position + 1):]
    print("你有%d条命"%life)
    print("乱序后的单词：",jumble)
    guess = input("请输入你的猜测结果:")
    i=5
    while(i>0):
        if (guess !=  answer):
            print("结果错误，你还有%d次机会：",%i)
            guess = input()
            i -= 1
        else:
            print("恭喜您，猜对了！")
           break
           
    if(i>0):
        score =+ 1
    else:
        life -=1
        print("机会耗尽，正确单词是%s"%answer)


    #else:
    #    isContinue = input("是否继续（Y/N）?")
    #while isContinue in ("Y","y"):
     #   guess_word()

choice = menu()
if (choice==1):
        game_start()
        while(life > 0):
           guess_word()
        print("生命耗尽，下次加油！")
elif(ch1 == 2):
           show_rank()
elif(ch1 == 3):
    print("欢迎再次进入游戏！")


        
isContinue = "Y"
while isContinue in("Y","y"):
      #随机挑选一个单词
      word=random.choice(words)
      answer = word #保存答案
      jumble=""
      for i in word:
          #随机抽取一个位置的字符放入乱序jumble中，并删除元字符中这个字符
          position =random.randrange(len(word))
          jumble +=word[position]
          word=word[:position] + word[(position+1):]
      #输出乱序后的单词
      print("乱序后的单词：",jumble)
      #接受玩家猜的单词
      guess=input("请输入你的猜测结果:")
      while guess !=answer: 
          guess=input("结果错误，请重新猜测: ")
      print("恭喜你，猜对了！")
      isContinue = input("是否继续（Y/N）？")
print("谢谢参与，欢迎下次再玩！")
      
      
