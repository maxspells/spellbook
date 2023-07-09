import sys
import math
import msvcrt as m
sys.path.append('modules')
import inspect
import importlib
import os
import os.path
import requests
from modules.character import *
newbook = []
book = [[],[],[],[],[],[],[],[],[],[]]
prepared = []

def create_spellbook(lvl):
    list = requests.get(f"https://pfapi.whizkid.dev/api/Spell/Class/{chr.pc_class}?level={lvl}&page=1&limit=100").json()
    for i in list:
        query = False
        if lvl == 0 and chr.pc_class == "Wizard":
            newbook.append(i)
        else:
            while query == False:
                art()
                print(f"Do you want to add {i['name']} to your spellbook?")
                prompt = input("y/n or d for description:")
                if prompt == "y":
                    newbook.append(i)
                    query = True
                elif prompt == "d":
                    print(i["description"])
                    wait()
                    continue
                else:
                    query = True



# checks spellbook.py for classes. If it's a class, imports it and adds it to an array and returns array
def load_spells(module_name): 
    module = importlib.import_module(module_name)
    list = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            list.append(obj)
    return list
allspells = load_spells('modules.spellbook')
def storespell(i): #sorts spell into book array by spell level
    book[i.sp_lvl].append(i)

def modifier(stat): #calculates intelligence modifier for spells that use it
    mod = math.floor((stat-10)/2)
    return mod

def perday(char): #calculates how many spells per day can be prepared per spell level
    spd = []
    z = 0
    bonus = chr_spells.bonus
    core = chr_spells.spellsperday
    for i in range(len(core)):
        if(core[z]>0): # if you can't cast spells of this level, skips adding bonus
            spd.append(core[z]+bonus[z]) 
        else:
            spd.append(core[z])
        z+=1
    return spd

def writespells():
    w = open("preparedspells.txt","w")
    header = -1
    for i in prepared:
        if header < i.sp_lvl:
            w.write("Level " + str(i.sp_lvl) + " spells" + "\n" + "-----------------" + "\n")
            header = i.sp_lvl
        w.write("-" + i.name + "-" + "\n" + "\n")
        w.write(i.desc + "\n" + "\n")
        w.write("\n")
    w.close()

def prepare():
    dex = 0
    availableslots = perday(chr)
    dex2 = 0
    for ea in availableslots:
        if ea > 0:
            print(f"You can prepare {ea} level {dex2} spells.")
            dex2+=1
    wait()
    art()
    print(chr.name)
    while(availableslots[dex]>0):
        if (dex<=(len(book)-1)):
            for spell in book[dex]:
                if availableslots[dex]>0:
                    art()
                    print(chr.name)
                    print(f"preparing level {spell.sp_lvl} spells, {availableslots[dex]} remaining.")
                    if input(f"Do you want to prepare {spell.name}? y/n:") == "y":
                        availableslots[dex] -= 1
                        prepared.append(spell)
        dex+=1
        print(f"increase dex to {dex}")
        if availableslots[dex] == 0:
            continue
def art():
    os.system('cls')
    print("""
      ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\  
 //________.|.________\\ 
`----------`-'----------'
        Spellbook
https://github.com/maxspells""")
def wait():
    print("Press any key")
    m.getch()

def start():
    art()
    wait()
    art()
    if (os.path.isfile("modules/spellbook.py")==True):
        import modules.spellbook as spellbook
        for i in allspells:
            storespell(i)
        print("spellbook.py found")
    else:
        print("No spellbook.py file found in modules folder")
    if (os.path.isfile("modules/character.py")==True):
        print("character.py found")
    else:
        print("character.py not found")   
# start()
# prepare()
# writespells()
# os.system('cls')
create_spellbook(0)#spell level

def writespellbook():
    w = open("spells.txt","w")
    header = -1
    for i in newbook:
        if header < i["classLevels"][chr.pc_class]:
            w.write("Level " + str(i["classLevels"][chr.pc_class]) + " spells" + "\n" + "-----------------" + "\n")
            header = i["classLevels"][chr.pc_class]
        w.write("-" + i["name"] + "-" + "\n" + "\n")
        w.write(i["description"] + "\n" + "\n")
        w.write("\n")
    w.close()
writespellbook()
