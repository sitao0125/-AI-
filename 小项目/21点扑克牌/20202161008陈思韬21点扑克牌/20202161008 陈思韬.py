import random
import sys


def get_shuffled_deck():
    print("洗牌，初始化")
    suits = {'♧', '♡', '♢'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(suit + rank)
    random.shuffle(deck)
    print(deck)
    return deck


def deal_card(deck, player_card):
    temp_card = deck.pop()
    player_card.append(temp_card)
    return player_card


def count_total(player):
    print("计算点数")
    result = 0
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
              'Q': 10, 'K': 10, 'A': 11}
    for card in player:
        result += values[card[1:]]
    for card in player:
        if result > 21 and card[1:] == 'A':
            result -= 10
    print(result)
    return result


def show_card(player, name):
    print("%s的牌：" % name, end="")
    print(player)


def blackjack():
    print("21点游戏")
    deck = get_shuffled_deck()
    player = []
    house = []

    answer = input("是否继续发牌：输入0停止发牌")
    while answer != '0' and len(deck) >= 2:
        player = deal_card(deck, player)
        house = deal_card(deck, house)
        show_card(player, "玩家")
        show_card(house,"庄家")
        answer = input("是否继续发牌：输入0停止发牌")

    if count_total(house) > 21:
        print("庄家爆了，玩家赢了")
    elif count_total(player) > 21:
        print("玩家爆了，庄家赢了")
    elif count_total(player) > count_total(house):
        print("玩家赢了")
    elif count_total(player) < count_total(house):
        print("庄家赢了")
    else:
        print("平局")


if __name__ == '__main__':
    blackjack()
