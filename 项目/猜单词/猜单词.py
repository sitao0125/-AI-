import random
words=['mother','passion','peace','blossom''sunshine','sweetheart',
       'gorgeous','cherish','enthusiasm',
       'hope','grace','rainbow','blue','sunflower','twinkle']

print("欢迎参加猜单词游戏！\n请把乱序后的字母组成一个单词\n")
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
      
      
