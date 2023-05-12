import random
import sys
#定义牌

def get_shuffled_deck():
    print("洗牌，初始化")
    #花色suit和序号
    suits={'黑桃','红桃','方块','❤'}
    ranks={'2','3','4,','5','6','7','8,','9,','10','J','Q','K','A'}
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(suit + ''+rank)
    random.shuffle(deck)
    print(deck)
    return deck


def deal_card(deck,player_card):
    print("发牌")
    temp_card = deck.pop()
    player_card.append(temp_card)
    return player_card
    
def count_total():
    print("计算点数")
    values = 0
    return values

def blackjack():#主函数
    print("21点游戏")
    deck  = get_shuffled_deck()
    player = []
    house = []
    for i in range(2):
        player=deal_card(deck,player)
        house = deal_card(deck,house)
    answer = input("是否继续发牌:输入0停止发牌")
    while(answer !='0'):
        deal_card("player")
        if(count_total() > 21):
            print("爆了，玩家输了")
            sys.exit()
        answer = input("是否继续发牌:输入0停止发牌")
    while(count_total(house)<17):
        deal_card("house")
        if(count_total() > 21):
            print("爆了，庄家输了")
            sys.exit()
    if(count_total(house) < count_total(player) ):
        print("玩家赢了")
    elif(count_total(house) > count_total(player) ):
        print("庄家赢了")
    else:
        if(conut_total(player) == 21):
            if(len(palyer) == 2):
                print("玩家赢了")
            elif(len(house) == 2 and len(player) > 2):
                print("庄家赢了")
        else:
            print("平局")
            
            

        

    #以上应该是玩家部分
    #庄家部分
        
        
'''
def total(player,house):#每次读取玩家和庄家的点数,发一次牌运行一次
    playp = 0 #玩家点数初始为0
    housep = 0#庄家点数初始为0
    playp = deal_card().    #这里应该要调用deal_card里面分配的点数吧？
    housep = deal_card()

    playp += playp
    houep += housep

    
    if playp > 21:
        print("玩家输牌")
'''


    
    
    
        



    

if __name__ == '__main__ ':
    blackjack()
    
get_shuffled_deck()

blackjack()
