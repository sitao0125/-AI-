from random import randint, choice


class Monster:
    count = 0

    def __init__(self, num):
        self.num = num
        self.blood = randint(1, 5)
        Monster.count += 1

    def attack(self, player):
        damage = randint(1, 3)
        print(f"怪物{self.num}攻击了你，造成了{damage}点伤害！")
        player.blood -= damage
        if player.blood <= 0:
            print("你被怪物打败了！")
            return False
        else:
            return True

    def be_killed(self, player):
        print(f"怪物{self.num}被你打死了！")
        if randint(0, 1):
            gold = randint(1, 3)
            player.gold += gold
            print(f"你获得了{gold}个金币！")
        player.exp += 1
        if player.exp >= player.level * 5:
            player.level += 1
            print(f"你升到了{player.level}级！")
        Monster.count -= 1


class Player:
    def __init__(self, name):
        self.name = name
        self.blood = 200
        self.level = 1
        self.exp = 0
        self.gold = 0

    def attack(self, monster):
        damage = randint(3, 6)
        monster.blood -= damage
        if monster.blood <= 0:
            monster.be_killed(self)
            return True
        else:
            return False


def create_monsters(n):
    monsters = []
    monster_nums = list(range(1, n + 1))
    for i in range(n):
        monsters.append(Monster(monster_nums[i]))
    return monsters


def show_monsters(monsters):
    print("目前你可以打的怪物：", end=" ")
    alive_monster_nums = [monster.num for monster in monsters if monster.blood > 0]
    sorted_alive_monster_nums = sorted(alive_monster_nums)
    for num in sorted_alive_monster_nums:
        print(num, end=" ")
    print()




def attack_monster(monsters, player):
    while True:
        try:
            num = int(input("你想打哪只怪物？")) - 1
            if num < 0 or num >= len(monsters):
                print("输入有误，请重新输入！")
                continue
            monster = monsters[num]
            if monster.blood <= 0:
                print("这只怪物已经死了，请选择其他怪物！")
                continue
            if player.attack(monster):
                monster.blood = 0
                return True
            else:
                return False
        except ValueError:
            print("输入有误，请重新输入！")
            continue
        else:  # 避免重复输出
            break




def play_game(player, monsters):
    while Monster.count > 0:
        show_monsters(monsters)
        if not attack_monster(monsters, player):
            break
        alive_monsters = [monster for monster in monsters if monster.blood > 0]
        if not alive_monsters:
            print("你赢了！")
            break
        for monster in alive_monsters:
            if not monster.attack(player):
                return False
        monsters = alive_monsters
    if player.blood <= 0:
        print("你死了！")
        return False
    else:
        print("游戏结束！")
        choice = input("是否重新开始游戏？(Y/N)").lower()
        if choice == "y":
            Monster.count = 0
            player.blood = 20
            player.level = 1
            player.exp = 0
            player.gold = 0
            return True
        else:
            return False



name = input("请输入玩家姓名：")
player = Player(name)

while True:
    play_game(player, create_monsters(5))
    if player.blood <= 0:
        print("您已死亡，游戏结束")

