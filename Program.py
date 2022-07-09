from Methods import *
Luck = random.randint(0, 50)

struggler_health = 100

monster_level = 0

Monster_list = ["Drunk Skull", "Blue Knight", "Zodd"]
monster_str = Monster_list[random.randint(0, 2)]
print(monster_str + " has appeared")

drunk_skull = Monster("Drunk Skull", random.randint(500, 1000))
blue_knight = Monster("Blue Knight", random.randint(1500, 2500))
Zodd = Monster("Zodd", random.randint(2000, 5000))

if monster_str == "Drunk Skull":
    monster_level = drunk_skull.health()
    monster_attack = drunk_skull.attack_power()

elif monster_str == "Blue Knight":
    monster_level = blue_knight.health()
    monster_attack = blue_knight.attack_power()

elif monster_str == "Zodd":
    monster_level = Zodd.health()
    monster_attack = Zodd.attack_power()
attack_level = 0
attack_list = ["Sword", "Magic", "Arrow"]
print("choose attack method Struggler!")


def fight(attack_index):
    try:
        attack_str = attack_list[attack_index]
    except:
        print("Failure")
        exit()
    print(f"you have choosen {attack_str}")
    if attack_str == "Sword":
        attack_level = Attack("Sword", random.randint(0, 100)).power()
    elif attack_str == "Magic":
        attack_level = Attack("Magic", random.randint(0, 100)).power()
    elif attack_str == "Arrow":
        attack_level = Attack("Arrow", random.randint(0, 100)).power()
    return attack_level


print("you got 5 chances")
attack_index = int(input("enter 0, 1 or 2"))
m = monster_level - fight(attack_index) + Luck
loopVar = 0
while loopVar <= 4:
    if m > 0:
        print("He's still alive! Try again...")
        attack_index = int(input("enter 0, 1 or 2"))
        m = monster_level - fight(attack_index)
        monster_level = m
        Luck += 10
        loopVar += 1
    else:
        print("You are now a Raider of Midland")
        exit()

print(f"{monster_str} is attacking!!!!")
n = struggler_health - monster_attack
fifty = 0
while fifty < 50:
    if n < 0:
        print("you died")
        exit()
    else:
        print("run away or attack, Struggle!")
        attackORrun = int(input("enter 0, 1, 2 or 5"))
        if attackORrun == 5:
            print("you can't keep running away...")
            monster_attack += random.randint(0, 100)
            struggler_health += 50
        else:
            print("you are bleeding")
            n = struggler_health + Luck - monster_attack
            if n < 0:
                print("you died")
                exit()
            else:
                m = monster_level - fight(attack_index) + Luck
                if m < 0:
                    print("You are now a Raider of Midland")
                    exit()
                print("He's still attacking!!!")
                monster_level = m
                Luck += 50
    fifty += 1
print("random philosophy")