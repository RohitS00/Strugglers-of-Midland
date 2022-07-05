import random

from Methods import *

Luck = random.randint(0, 50)

Struggler_health = 100

MonsterLevel = 0

Monster_list = ["Drunk Skull", "Blue Knight", "Zodd"]
MonsterStr = Monster_list[random.randint(0, 2)]
print(MonsterStr + " has appeared")

DrunkSkull = Monster("Drunk Skull", random.randint(500, 1000))
BlueKnight = Monster("Blue Knight", random.randint(1500, 2500))
Zodd = Monster("Zodd", random.randint(2000, 5000))

if MonsterStr == "Drunk Skull":
    MonsterLevel = DrunkSkull.health()
    MonsterAttack = DrunkSkull.attack_power()
elif MonsterStr == "Blue Knight":
    MonsterLevel = BlueKnight.health()
    MonsterAttack = BlueKnight.attack_power()
elif MonsterStr == "Zodd":
    MonsterLevel = Zodd.health()
    MonsterAttack = Zodd.attack_power()

AttackLevel = 0
Attack_list = ["Sword", "Magic", "Arrow"]
print("choose attack method Struggler!")


def fight(attack_index):
    try:
        AttackStr = Attack_list[attack_index]
    except:
        print("Failure")
        exit()
    print(f"you have choosen {AttackStr}")
    if AttackStr == "Sword":
        AttackLevel = Attack("Sword", random.randint(0, 100)).power()
    elif AttackStr == "Magic":
        AttackLevel = Attack("Magic", random.randint(0, 100)).power()
    elif AttackStr == "Arrow":
        AttackLevel = Attack("Arrow", random.randint(0, 100)).power()
    return AttackLevel


attack_index = int(input("enter 0, 1 or 2"))
m = MonsterLevel - fight(attack_index) + Luck
loopVar = 0
while loopVar <= 5:
    if m > 0:
        print("Failure")
        attack_index = int(input("enter 0, 1 or 2"))
        m = MonsterLevel - fight(attack_index)
        MonsterLevel = m
        Luck += 10
        loopVar += 1
    else:
        print("Success")
        exit()

print(f"{MonsterStr} is attacking!")
n = Struggler_health - MonsterAttack
fifty = 0
while fifty < 50:
    if n < 0:
        print("you died")
        exit()
    else:
        print("run away or attack")
        attackORrun = int(input("enter 0, 1, 2 or 5"))
        if attackORrun == 5:
            MonsterAttack += random.randint(0, 100)
            Struggler_health += 50
        else:
            n = Struggler_health + Luck - MonsterAttack
            if n < 0:
                print("you died")
                exit()
            else:
                m = MonsterLevel - fight(attack_index) + Luck
                if m < 0:
                    print("Success")
                    exit()
                MonsterLevel -= m
                Luck += 50
    fifty += 1

