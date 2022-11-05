import time
import random

def act_lv1_try(p_statue):
    print("Monster comes.")
    m_hp = round(random.uniform(30, 40),3)
    m_at = round(random.uniform(3, 6),3)
    print(f"Monster has {m_hp}HP")
    m_hp_o = m_hp
    level_1(reactcycle(m_hp,m_hp_o,p_statue))

def act_lv1(p_statue):
    p1 = round(random.uniform(0,1),0)
    if p1 == 1:
        print("Monster comes.")
        m_hp = round(random.uniform(30, 40),3)
        m_at = round(random.uniform(3, 6),3)
        print(f"Monster has {m_hp}HP")
        m_hp_o = m_hp
        
        level_1(reactcycle(m_hp,m_hp_o,p_statue))
    elif p1 == 0:
        print("Nothing found.")
        level_1(p_statue)

def act_lv2(p_statue):
    p1 = round(random.uniform(0,1),0)
    if p1 == 1:
        print("Monster comes.")
        m_hp = round(random.uniform(70, 80),3)
        m_at = round(random.uniform(10,12),3)
        print(f"Monster has {m_hp}HP")
        m_hp_o = m_hp
        
        level_2(reactcycle(m_hp,m_hp_o,p_statue))
    elif p1 == 0:
        print("Nothing found.")
        level_2(p_statue)

def attack(m_hp,p_statue):
    p = round(random.uniform(0,100),3)
    p_statue_at_o = round(p_statue[1],3)
    p_statue[1] = round(p_statue[1],3) + round(random.uniform(-1, 1),3)
    if p>=20:
        p2 = random.uniform(0,100)
        if p2 > 99:
            m_hp = m_hp - p_statue[1]*3
            print(f"Monster -{p_statue[1]*3} HP.")
            if m_hp > 0:
                print(f"Monster left {m_hp} HP.")
            else:
                print(f"Monster -{p_statue[1]} HP.")
                print("Monster died.")
        else:
            m_hp = m_hp - p_statue[1]
            if m_hp > 0:
                print(f"Monster left {m_hp} HP.")
            else:
                print("Monster died.")
    else:
        print("Monster escape.") 
    p_statue[1] = p_statue_at_o
    return m_hp,p_statue

def reactcycle(m_hp,m_hp_o,p_statue):
    if m_hp > 0:
        act1 = input("Press key.")
        if " i " in (" " + act1 + " ".lower()):
            m = attack(m_hp,p_statue)
            n = reactcycle(m[0],m_hp_o,p_statue)
            p_statue[0] = n[0]
            return p_statue
        elif " p " in (" " + act1 + " ".lower()):
            print("de") 
            return p_statue
        else:
            print("monster attck")
            return p_statue
    else:
        print("Congratulation.")
        p_statue[0] = round(p_statue[0] + 0.1*m_hp_o,3)
        print(f"Your HP become {p_statue[0]} .")
        return p_statue

def level_1(p_statue):
    print("What would you like to do next?")
    level_1_next = input("Go to level two?  Discover Level one? Leave? Open statue?")
    if " one " in (" " + level_1_next + " ".lower())  or " 1 " in (" " + level_1_next + " "):
        act_lv1(p_statue)
    elif " two " in (" " + level_1_next + " ".lower()) or " 2 " in (" " + level_1_next + " "):
        print("Walking.")
        time.sleep(0.5)
        print("Walking..")
        time.sleep(0.5)
        print("Walking...")
        time.sleep(0.5)
        level_2_start(p_statue)
    elif" leave " in (" " + level_1_next + " ".lower()):
        print("Walking.")
        time.sleep(0.5)
        print("Walking..")
        time.sleep(0.5)
        print("Walking...")
        time.sleep(0.5)
        new_place(p_statue)
    elif "statue" in (" " + level_1_next + " ".lower()):
        print(f"HP:{p_statue[0]}")
        print(f"Basic attack:{p_statue[1]}")
        input()
        level_1(p_statue)
    else:
        level_1(p_statue)

def level_2(p_statue):
    print("What would you like to do next?")
    level_2_next = input("Go to level one? Go to level three?  Discover Level two? Open statue?")
    if " one " in (" " + level_2_next + " ".lower())  or " 1 " in (" " + level_2_next + " "):
        level_1_start(p_statue)
    elif " two " in (" " + level_2_next + " ".lower()) or " 2 " in (" " + level_2_next + " "):
        act_lv2(p_statue)
    elif " three " in (" " + level_2_next + " ".lower()) or " 3 " in (" " + level_2_next + " "):
        print("Walking.")
        time.sleep(0.5)
        print("Walking..")
        time.sleep(0.5)
        print("Walking...")
        time.sleep(0.5)
        #level3
    elif "statue" in (" " + level_2_next + " ".lower()):
        print(f"HP:{p_statue[0]}")
        print(f"Basic attack:{p_statue[1]}")
        input()
        level_2(p_statue)
    else:
        level_2(p_statue)

def level_1_start(p_statue):
    print("Welcome to level 1.")
    level_1(p_statue)

def level_2_start(p_statue):
    print("Welcome to level 2.")
    level_2(p_statue)

def start():
    p_hp = round(random.uniform(40, 50),3)
    p_at = round(random.uniform(4, 6),3)
    p_statue = [p_hp,p_at]
    playername = input("What's your name?")
    print(f"Welcome to the world {playername}.")
    place_1 = input("Where would you like to go?")
    print(f"Let's go to {place_1}.")
    print("Walking.")
    time.sleep(0.5)
    print("Walking..")
    time.sleep(0.5)
    print("Walking...")
    time.sleep(0.5)
    print(f"{place_1.title()} arrived!")
    print("Novice teaching start!")
    print(f"Your HP is {p_statue[0]} .")
    print(f"Your basic attack is {p_statue[1]} .")
    print("Press I to attack and press P to defend")
    print("Here comes a rabbit, try to press I.")
    act_lv1_try(p_statue)
    
def new_place(p_statue):
    place_1 = input("Where would you like to go?")
    print(f"Let's go to {place_1}.")
    print("Walking.")
    time.sleep(0.5)
    print("Walking..")
    time.sleep(0.5)
    print("Walking...")
    time.sleep(0.5)
    print(f"{place_1.title()} arrived!")
    level_1(p_statue)
      
start()
print("Game Over.")
