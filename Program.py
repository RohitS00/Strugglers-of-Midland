from Methods import *

MonsterLevel = 0
Monster_list = ["Drunk Skull", "Blue Knight", "Zodd"]
MonsterStr = Monster_list[random.randint(0, 2)]
print(MonsterStr + " has appeared")
if MonsterStr == "Drunk Skull":
    MonsterLevel = Monster("Drunk Skull", random.randint(50, 100)).power()
elif MonsterStr == "Blue Knight":
    MonsterLevel = Monster("Blue Knight", random.randint(50, 100)).power()
elif MonsterStr == "Zodd":
    MonsterLevel = Monster("Zodd", random.randint(80, 100)).power()

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
m = MonsterLevel - fight(attack_index)
loopVar = 0
while loopVar <= 5:
    if m > 0:
        print("Failure")
        attack_index = int(input("enter 0, 1 or 2"))
        m = MonsterLevel - fight(attack_index)
        loopVar += 1
    else:
        print("Success")
        exit()