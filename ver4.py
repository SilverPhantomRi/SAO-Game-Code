import time
import random


def cardinal_start():
    player_health_point_present =player_health_point_max = random.randint(40, 50)
    player_health_point = [player_health_point_present,player_health_point_max]
    player_attack = random.randint(5, 7)
    player_floor_present = 1
    player_floor_max = 1
    player_floor = [player_floor_present,player_floor_max]
    player_name = "no"
    player_surrounding = "city"
    present_level = 1
    present_exp = 0
    exp = [present_exp,present_level*50]
    player_level = [present_level,exp]
    col = 0
    monster_health_point = 0
    monster_attack = 0
    monster_origin_health_point = 0
    player_statue = [player_health_point,player_attack,player_floor,player_surrounding,player_name,player_level,col]
    monster_statue = [monster_health_point,monster_attack,monster_origin_health_point]
    cardinal_list = [player_statue,monster_statue]
#    print("Link start")
#    time.sleep(0.35)
#    print("Touch")
#    time.sleep(0.35)
#    print("OK")
#    time.sleep(0.35)
#    print("sight")
#    time.sleep(0.35)
#    print("OK")
#    time.sleep(0.35)
#    print("Hearing")
#    time.sleep(0.35)
#    print("OK")
#    time.sleep(0.35)
#    print("Taste")
#    time.sleep(0.35)
#    print("OK")
#    time.sleep(0.35)
#    print("Smell")
#    time.sleep(0.35)
#    print("OK")
#    time.sleep(0.35)
#    input("ID:")
#    input("Password:")
    cardinal_list[0][4] = input("Playername:")
    print("Welcome to Sword Art Online!")
    print("Novice teaching start!")
    print(f"Your HP is {cardinal_list[0][0][0]} .")
    print(f"Your basic attack is {cardinal_list[0][1]} .")
    print("Press I to attack and press P to defend")
    print("Here comes a rabbit, try to press I.")
    cardinal_novice_teaching(cardinal_list)

def cardinal_novice_teaching(cardinal_list):
    print("Novice teaching start.")
    print("Monster comes.")
    cardinal_list[1][0] = cardinal_list[1][2] = random.randint(35*cardinal_list[0][2][0]-10, 35*cardinal_list[0][2][0]+10)
    cardinal_list[1][1] = random.randint(4*cardinal_list[0][2][0]-2, 4*cardinal_list[0][2][0]+2)
    print(f"Monster has {cardinal_list[1][0]}HP.")
    cardinal_reactcycle(cardinal_list)
    print("Novice teaching finish.")
    cardinal_floor(cardinal_list)

def cardinal_monster_produce(cardinal_list):
    cardinal_probability = random.randint(0,3)
    if cardinal_probability >= 1:
        print("Monster comes.")
        cardinal_list[1][0] = cardinal_list[1][2] = random.randint(35*cardinal_list[0][2][0]-10, 35*cardinal_list[0][2][0]+10)
        cardinal_list[1][1] = random.randint(4*cardinal_list[0][2][0]-2, 4*cardinal_list[0][2][0]+2)
        print(f"Monster has {cardinal_list[1][0]}HP")
        cardinal_reactcycle(cardinal_list)
    else:
        print("Nothing found.")
        cardinal_floor(cardinal_list)

def cardinal_reactcycle(cardinal_list):
    if cardinal_list[1][0] > 0:
        cardinal_act = input("Press key.")
        if " i " in (" " + cardinal_act.lower() + " "):
            cardinal_attack(cardinal_list)
            cardinal_reactcycle(cardinal_list)
        elif " p " in (" " + cardinal_act.lower()+ " "):
            print("de")
            cardinal_reactcycle(cardinal_list)
        else:
            print("Monster attck")
            cardinal_reactcycle(cardinal_list)
    else:
        print("Congratulation.")
        print(f"Your HP become {cardinal_list[0][0][0]}/{cardinal_list[0][0][1]} .")
        print(f"EXP:{cardinal_list[0][5][1][0]}+{round(cardinal_list [1][2]*0.1)}/{cardinal_list[0][5][1][1]} ")
        cardinal_list[0][5][1][0] = cardinal_list[0][5][1][0] + round(cardinal_list [1][2]*0.1)
        if cardinal_list[0][5][1][0] >=cardinal_list[0][5][1][1]:
            cardinal_list[0][5][1][0] = cardinal_list[0][5][1][0] -cardinal_list[0][5][1][1]
            cardinal_list[0][5][0] = cardinal_list[0][5][0] + 1
            cardinal_list[0][5][1][1] = cardinal_list[0][5][0]*50
            print(f"Upgrade to LV{cardinal_list[0][5][0]}")
        print(f"You get {cardinal_list [1][2]}col.")
        cardinal_list[0][6] = cardinal_list[0][6] + cardinal_list [1][2]
        cardinal_floor(cardinal_list)
    return cardinal_list

def cardinal_floor(cardinal_list):
    if  " city " in (" " + cardinal_list[0][3] + " "):
        t1 = time.monotonic()
        print(f"You are in {cardinal_list[0][3]} floor {cardinal_list[0][2][0]}.")
        print("What would you like to do next?")
        cardinal_act = input("Go to maze? Go to another floor? Open statue?")
        if " maze " in (" " + cardinal_act.lower() + " "):
            cardinal_list[0][3] = "maze"
            t2 = time.monotonic()
            tt = t2-t1
            if cardinal_list[0][0][0]+tt < cardinal_list[0][0][1]:
                cardinal_list[0][0][0] = cardinal_list[0][0][0]+round(tt)
            else:
                cardinal_list[0][0][0]=cardinal_list[0][0][1]
            cardinal_floor(cardinal_list)
        elif " another " in (" " + cardinal_act.lower() + " ") or" floor " in (" " + cardinal_act.lower() + " "):
            cardinal_act_floor = input("Which floor?")
            if cardinal_act_floor.isdigit():
                cardinal_act_floor = int(cardinal_act_floor)
                if cardinal_list[0][2][1] >= cardinal_act_floor and cardinal_act_floor > 0:
                    cardinal_list[0][2][0] = cardinal_act_floor
                    print(f"Go to floor {cardinal_list[0][2][0]}.")
                    cardinal_floor(cardinal_list)
                elif cardinal_act_floor < 0:
                    print("Error.")
                    cardinal_floor(cardinal_list)
                else:
                    print("The floor hasn't open.")
                    cardinal_floor(cardinal_list)
            else:
                print("Error.")
                cardinal_floor(cardinal_list)
        elif " open " in (" " + cardinal_act.lower() + " ") or" statue " in (" " + cardinal_act.lower() + " "):
            cardinal_list = cardinal_playerstatue_open(cardinal_list)
            cardinal_floor(cardinal_list)
        else:
            cardinal_floor(cardinal_list)
    elif  " maze " in (" " + cardinal_list[
        0][3] + " "):
        print(f"You are in {cardinal_list[0][3]} floor {cardinal_list[0][2][0]}.")
        print("What would you like to do next?")
        cardinal_act = input("Explore? Go back to city? Open statue?")
        if " explore " in (" " + cardinal_act.lower()+ " "):
            cardinal_monster_produce(cardinal_list)
        elif "city" in (" " + cardinal_act.lower()+ " "):
            cardinal_list[0][3] = "city"
            cardinal_floor(cardinal_list)
        elif " open " in (" " + cardinal_act.lower() + " ") or" statue " in (" " + cardinal_act.lower() + " "):
            cardinal_list = cardinal_playerstatue_open(cardinal_list)
            cardinal_floor(cardinal_list)
        else:
            cardinal_floor(cardinal_list)
    else:
        cardinal_floor(cardinal_list)
    return cardinal_list

def cardinal_attack(cardinal_list):
    cardinal_p1= random.uniform(0,100)
    if cardinal_p1>=20:
        cardinal_p2 = random.uniform(0,100)
        if cardinal_p2 > 99:
            cardinal_list[1][0] = cardinal_list[1][0] - cardinal_list[0][1]*3
            print(f"Monster -{cardinal_list[0][1]*3} HP.")
            if cardinal_list[1][0] > 0:
                print(f"Monster left {cardinal_list[1][0]} HP.")
            else:
                print("Monster died.")
        else:
            cardinal_list[1][0] = cardinal_list[1][0] - cardinal_list[0][1]
            print(f"Monster -{cardinal_list[0][1]} HP.")
            if cardinal_list[1][0] > 0:
                print(f"Monster left {cardinal_list[1][0]} HP.")
            else:
                print("Monster died.")
    else:
        print("Monster dodge.")
    p3 = random.uniform(0,100)
    if p3 >= 70:
        cardinal_list[0][0][0] = cardinal_list[0][0][0] - cardinal_list[1][1]
        print(f"Monster give you {cardinal_list[1][1]}HP hurt")
        print(f"Your HP:{cardinal_list[0][0][0]}/{cardinal_list[0][0][1]}")
    else:
        print("You dodge monster's attack.")
    return cardinal_list

def cardinal_playerstatue_open(cardinal_list):
    print(f"LV:{cardinal_list[0][5][0]}")
    print(f"HP:{cardinal_list[0][0][0]}/{cardinal_list[0][0][1]}")
    print(f"Basic attack:{cardinal_list[0][1]}")
    print(f"EXP:{cardinal_list[0][5][1][0]}/{cardinal_list[0][5][1][1]} ")
    print(f"Col:{cardinal_list[0][6]}")
    input()
    return cardinal_list

cardinal_start()
print("Game Over.")
