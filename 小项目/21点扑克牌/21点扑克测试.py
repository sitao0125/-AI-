import random
import sys

# 定义牌
def get_shuffled_deck():
    print("洗牌，初始化")
    # 花色suit和序号
    suits = {'黑桃', '红桃', '方块', '❤'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(suit + rank)
    random.shuffle(deck)
    print(deck)
    return deck

def deal_card(deck, player_cards):
    print("发牌")
    temp_card = deck.pop()
    player_cards.append(temp_card)
    return player_cards

def count_total(cards):
    print("计算点数")
    values = 0
    num_ace = 0
    for card in cards:
        rank = card[1:]
        if rank.isdigit():
            values += int(rank)
        elif rank in ['J', 'Q', 'K']:
            values += 10
        elif rank == 'A':
            values += 11
            num_ace += 1
    while values > 21 and num_ace > 0:
        values -= 10
        num_ace -= 1
    return values

def blackjack():
    print("21点游戏")
    deck = get_shuffled_deck()
    player_cards = []
    house_cards = []
    
    # 初始发牌
    for _ in range(2):
        player_cards = deal_card(deck, player_cards)
        house_cards = deal_card(deck, house_cards)
        
    answer = input("是否继续发牌: 输入0停止发牌")
    while answer != '0':
        player_cards = deal_card(deck, player_cards)
        if count_total(player_cards) > 21:
            print("爆了，玩家输了")
            sys.exit()
        answer = input("是否继续发牌: 输入0停止发牌")
        
    while count_total(house_cards) < 17:
        house_cards = deal_card(deck, house_cards)
        if count_total(house_cards) > 21:
            print("爆了，庄家输了")
            sys.exit()
            
    if count_total(house_cards) < count_total(player_cards):
        print("玩家赢了")
    elif count_total(house_cards) > count_total(player_cards):
        print("庄家赢了")
    else:
        if count_total(player_cards) == 21:
            if len(player_cards) == 2:
                print("玩家赢了")
            elif len(house_cards) == 2 and len(player_cards) > 2:
                print("庄家赢了")
        else:
            print("平局")

# 调用主函数进行游戏
blackjack()
