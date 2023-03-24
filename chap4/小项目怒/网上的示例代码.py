#coding=utf-8
import random

class Card():
    #扑克牌类
    points = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♣️', '♦️', '♥️', '♠️'] #花色

    def __init__(self, point, suit):
        self.point = point
        self.suit = suit

    def __str__(self):
        return self.suit + self.point

class Poke():
    #一副牌类
    def __init__(self):
        self.cards = [Card(point, suit) for point in Card.points for suit in Card.suits]
        self.current = 0 #记录发到第几张牌

    def shuffle(self):
        #洗牌方法
        random.shuffle(self.cards)
        self.current = 0

    def deal(self):
        #发牌方法
        card = self.cards[self.current]
        self.current += 1
        return card

class Hand():
    #手牌类
    def __init__(self, name):
        self.name = name #玩家姓名
        self.cards = [] #手上的牌

    def add(self, card):
        #添加一张牌到手上
        self.cards.append(card)

    def sort(self):
        #对手上的牌进行排序
        self.cards.sort(key=lambda card: (Card.points.index(card.point), Card.suits.index(card.suit)))

    def show(self):
        #显示手上的所有牌
        print(self.name + ":", end=" ")
        for card in self.cards:
            print(card, end=" ")
        print()

#创建一副新牌并洗牌
poke = Poke()
poke.shuffle()

#创建四个玩家并发13张给每人
players = ["Tom", "Jerry", "Mike", "Lucy"]
hands = [Hand(name) for name in players]
for i in range(13):
    for hand in hands:
       hand.add(poke.deal())

#对每个玩家手中的扑克进行排序并显示出来
for hand in hands:
   hand.sort()
   hand.show()