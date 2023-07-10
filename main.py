import sys
import math
import msvcrt as m
sys.path.append('modules')
import inspect
import importlib
import os
import os.path
import requests
import json
from modules.character import *
newbook = []
book = [[],[],[],[],[],[],[],[],[],[]]
prepared = []


def query_spell(spell,splvl,spellsleft):
    x = spellsleft
    query = False
    if splvl == 0 and chr.pc_class == "Wizard":
        newbook.append(spell)
    elif x>0:
        while query == False:
            print(f"Do you want to add {spell['name']} to your spellbook?")
            prompt = input("y/n or d for description:")
            if prompt == "y":
                newbook.append(spell)
                x-=1
                query = True
            elif prompt == "d":
                art()
                print("\n")
                print(f"-{spell['name']}-")
                print("--------------------------------------")
                print(f"Casting time:{spell['castingTime']}")
                print(f"Target:{spell['targets']}")
                print(f"Duration:{spell['duration']}")
                print("--------------------------------------")
                print(spell['description'])
                wait()
                continue
            else:
                query = True
    return x

def create_spellbook():
    for lvl in range(10):
        spellsleft = chr.spellsknown[lvl]
        if spellsleft>0:
            list = requests.get(f"https://pfapi.whizkid.dev/api/Spell/Class/{chr.pc_class}?level={lvl}&page=1&limit=100").json()
            list2 = requests.get(f"https://pfapi.whizkid.dev/api/Spell/Class/{chr.pc_class}?level={lvl}&page=2&limit=100").json()
            list3 = requests.get(f"https://pfapi.whizkid.dev/api/Spell/Class/{chr.pc_class}?level={lvl}&page=3&limit=100").json()
            spellnumber = 1
            totalspellsonlist = (len(list)+len(list2)+len(list3))
            for i in list:
                if spellsleft > 0:
                    art()
                    print(f"You can pick {spellsleft} more level {lvl} spells. {spellnumber}/{totalspellsonlist}")
                    spellsleft = query_spell(i,lvl,spellsleft)
                    spellnumber+=1
            for i in list2:
                if spellsleft > 0:
                    art()
                    print(f"You can pick {spellsleft} more level {lvl} spells. {spellnumber}/{totalspellsonlist}")
                    spellsleft = query_spell(i,lvl,spellsleft)
                    spellnumber+=1
            for i in list3:
                if spellsleft > 0:
                    art()
                    print(f"You can pick {spellsleft} more level {lvl} spells. {spellnumber}/{totalspellsonlist}")
                    spellsleft = query_spell(i,lvl,spellsleft)
                    spellnumber+=1


def searchspell(spell,property):
    sp = spell.replace(" ", "%20")
    spell_obj = requests.get(f"https://pfapi.whizkid.dev/api/Spell/{sp}")
    obj = spell_obj.json()
    output = obj[f'{property}']
    return output


# OUTDATED checks spellbook.py for classes. If it's a class, imports it and adds it to an array and returns array
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

def perday(): #calculates how many spells per day can be prepared per spell level
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

#OUTDATED
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
        import modules.old_spellbook as old_spellbook
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
create_spellbook()

def writespellbook():  #REWORK THIS TO SAVE KNOWN SPELL ARRAY LIST
    w = open("spells.txt","w")
    header = -1
    for i in newbook:
        if header < i["classLevels"][chr.pc_class]:
            w.write("Level " + str(i["classLevels"][chr.pc_class]) + " spells" + "\n" + "-----------------" + "\n")
            header = i["classLevels"][chr.pc_class]
        w.write("-" + i["name"] + "-" + "\n" + "\n")
        w.write(f"Casting time:{i['castingTime']}" + "\n")
        w.write(f"Target:{i['targets']}" + "\n")
        w.write(f"Duration:{i['duration']}" + "\n")
        w.write("--------------------------------------" + "\n")
        w.write(i["description"] + "\n" + "\n")
        w.write("\n")
    w.close()

writespellbook()