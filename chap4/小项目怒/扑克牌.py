from random import randint as rand

def show(a):
    if a == 54:
        pm = "JOKE"
    elif a == 53:
        pm = "joke"
    else:
        a = a - 1
        #a表示一副扑克牌中的一张牌，取值范围是1-54
        #在这个函数中，a 是一个表示扑克牌的整数，它的范围是 1 到 54。
        # 但是在判断花色和点数的时候，我们是将 a 除以 13 来判断花色，取余数来判断点数的。
        # 因为我们把 54 张扑克牌的编号从 0 到 53 进行了映射，所以在使用除法和取余数操作之前，需要将 a 减去 1，
        # 以便使其从 0 开始编号。因此，对于这个函数而言，a 需要减去 1 才能正确地进行花色和点数的判断。
        if int(a / 13) == 0:
            huase = "黑桃"
        elif int(a / 13) == 1:
            huase = "红心"
        elif int(a / 13) == 2:
            huase = "梅花"
        elif int(a / 13) == 3:
            huase = "方块"
        a = a + 1
        if a % 13 >= 1 and a % 13 <= 10:
            t = a % 13
            if t == 1:
                pm = huase + "A"
            else:
                pm = huase + str(t)
        elif a % 13 == 11:
            pm = huase + "J"
        elif a % 13 == 12:
            pm = huase + "Q"
        elif a % 13 == 0:
            pm = huase + "K"
    return pm

def sort(a):#将玩家手牌进行排序
    #在扑克牌程序中，sort函数的作用是将玩家手中的牌进行排序，以便更好地展示和管理。
    # 在游戏中，玩家手中的牌顺序可能是随机的，
    # 如果不对其进行排序，那么就很难区分哪些是同花顺、顺子、三条等等，而且也不方便展示给其他玩家观看。
    # 因此，sort函数可以帮助玩家快速、准确地排序手中的牌，方便后续的游戏操作。
    #在程序中，sort函数会接收一个列表作为参数，对其进行升序排序，并返回一个值。
    # 具体来说，它会通过多次比较和交换，把玩家手中的牌按照从小到大的顺序排列。
    # 然后，程序会输出玩家手中已经排好序的牌，便于游戏进行。
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

pk = []
for i in range(54):
    pk.append(i+1)

wj = []
wj.append([])
wj.append([])
wj.append([])

dp = []
for i in range(17):
    for j in range(3):
        t = rand(0, len(pk)-1)
        wj[j].append(pk.pop(t))
        #总的来说，这段代码的作用是实现扑克牌的洗牌和发牌操作。
        # 其中，17次循环保证了每个玩家能够获得17张牌，
        # 而循环内部的随机选择保证了每个玩家手中的牌是随机的。
        # 最终，剩下的三张牌会作为底牌存储在dp列表中。

for i in range(3):
    dp.append(pk.pop(0))

for i in range(3):
    print("玩家%2d:" % (i+1), end=" ")
    for j in range(17):
        print("%4s" % show(wj[i][j]), end=" ")
    print()

print("底牌: ", end="")
for i in range(3):
    print("%4s" % show(dp[i]), end=" ")

print()
print("理牌后：")
for i in range(3):
    wj[i] = sort(wj[i])

for i in range(3):
    print("玩家%d" % (i+1), end=" ")
    for j in range(17):
        print("%4s" % show(wj[i][j]), end=" ")
    print()

print("底牌:", end=" ")
for i in range(3):
    print("%4s" % show(dp[i]), end=" ")

