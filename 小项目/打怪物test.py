from random import randint as r
import keyboard

class gw:
    count = 0  # 静态属性，类的属性

    def __init__(self, i):
        self.num = i  # num是对象的属性
        self.blood = r(1, 5)
        gw.count += 1
        self.gold = r(1, 10)
        self.exp = r(1, 5)

    def kill(self, name, i, w):
        self.blood -= i
        if (self.blood < 1):
            print("%d号怪物被%s打死了，掉落了%d个金币和%d点经验值" % (self.num, name, self.gold, self.exp))
            gw.count -= 1
            w.exp += self.exp
            if (w.exp >= 10 * w.level):
                w.upgrade()
                print("%s升级了！当前等级为%d" % (w.name, w.level))


class shop:
    def __init__(self):
        self.items = {"无尽之刃": {"price": 20, "attack": 100},
                      "破败王者之刃": {"price": 10, "attack": 80},
                      "狂徒铠甲": {"price": 5, "hp": 500}}

    def show_items(self):
        print("欢迎来到商城！")
        for i, item in enumerate(self.items):
            print("%d. %s（价格：%d金币）" % (i + 1, item, self.items[item]["price"]))

    def buy_item(self, w):
        my_shop = shop()  # 创建一个shop类的实例
        while True:
            my_shop.show_items()  # 通过实例调用show_items()方法
            choice =input("请选择要购买的物品编号：")
            if choice.isdigit() and int(choice) in range(1, len(self.items) + 1):
                item = list(self.items.keys())[int(choice) - 1]
                if w.gold >= self.items[item]["price"]:
                    w.gold -= self.items[item]["price"]
                    if "attack" in self.items[item]:
                        w.gjl += self.items[item]["attack"]
                        print("恭喜你，你购买了%s，攻击力提升了%d点！" % (item, self.items[item]["attack"]))
                    if "hp" in self.items[item]:
                        w.blood += self.items[item]["hp"]
                        print("恭喜你，你购买了%s，生命值提升了%d点！" % (item, self.items[item]["hp"]))
                    choice = input("是否继续购买？（y/n）")
                    if choice.lower() == "n":
                        break
                else:
                    print("金币不足，无法购买！")
            elif choice == "esc":
                break
            else:
                print("输入有误，请重新输入！")


class wj:
    def __init__(self, name):
        self.blood = 100
        self.gjl = 800
        self.name = name
        self.level = 1
        self.gold = 0
        self.exp = 0
        self.items = []

    def kill(self, g):
        self.blood -= g.blood
        if (self.blood < 1):
            print("%s被%d号怪物打死了" % (self.name, g.num))

    def upgrade(self):
        self.level += 1
        self.blood = 100 * self.level
        self.gjl = 800 * self.level
        self.exp = 0

    def show_items(self):
        print("您的物品清单：")
        for item in self.items:
            print(item.name)


def czgw(n, g):  # 创造怪物
    for i in range(n):
        g.append(gw(i + 1))


def hz(n, g):
    print("目前你可以打的怪物:", end=" ")
    for i in range(n):
        if (gw1[i].blood > 0):  # 怪物还活着
            print(g[i].num, end=" ")
    print()


def gj(g, w):
    i = int(input("你想打几号怪物")) - 1
    g[i].kill(w.name, w.gjl, w)
    if (g[i].blood < 1):
        w.gold += g[i].gold
        choice = input("是否购买装备？（y/n）")
        if choice.lower() == "y":
            shop.buy_item(wj1[0],w)
    if (w.blood > 0):
        gj(g, w)



name = input("请输入玩家姓名：")
wj1 = []
wj1.append(wj(name))

level = int(input("请选择难度：1、新手，2、普通，3、困难"))
if (level == 1):
    n = 5
elif (level == 2):
    n = 10
else:
    n = 30

gw1 = []
czgw(n, gw1)

while (gw.count > 0 and wj1[0].blood > 0):
    hz(n, gw1)
    gj(gw1, wj1[0])
