import sys
import math
import msvcrt as m
sys.path.append('modules')
import os
import os.path
from modules.pfapi import api
from modules.character import *
newbook = []
book = [[],[],[],[],[],[],[],[],[],[]]
prepared = []


def sp_desc(spell):#print description of spell when called
    art()
    print("\n")
    print(f"-{spell['name']}-")
    print(f"{spell['classLevels']}")
    print("--------------------------------------")
    print(f"Casting time:{spell['castingTime']}")
    print(f"Target:{spell['targets']}")
    print(f"Range:{spell['range']}")
    print(f"Duration:{spell['duration']}")
    print("--------------------------------------")
    print(spell['description'])
    wait()
    os.system('cls')

def query_spell(spell,splvl,spellsleft):
    x = spellsleft
    query = False
    if splvl == 0 and chr.pc_class == "Wizard": #Wizards start will all lvl 0 spells in spellbook
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
                sp_desc(spell)
                continue
            else:
                query = True
    return x

def create_spellbook():
    for lvl in range(10):
        spellsleft = chr.spellsknown[lvl]
        if spellsleft>0:
            totalspellsonlist = api.get_number_spells_perlvl(chr.pc_class,lvl)
            spellnumber = 1
            for page in range(5):
                splist = api.splist_get(chr.pc_class,lvl,(page+1))
                for i in splist:
                    if spellsleft > 0:
                        art()
                        print(f"You can pick {spellsleft} more level {lvl} spells. {spellnumber}/{totalspellsonlist}")
                        spellsleft = query_spell(i,lvl,spellsleft)
                        spellnumber+=1

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
https://github.com/maxspells
""")

def wait():
    print("Press any key")
    m.getch()

def writespellbook():  #REWORK THIS TO SAVE KNOWN SPELL ARRAY LIST
    w = open("spellbook.txt","w")
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

def search_func():
    while True:
        art()
        print("Type q to return to menu")
        prompt = input("Search a spell:")
        search = api.search_spell(prompt)
        if prompt == "q":
            break
        else:
            sp_desc(search)
def main():
    while True:
        art()
        print("Create a spellbook 'b'")
        print("Search a spell = 's'")
        print("Quit = 'q")
        prompt = input(':')
        if prompt == "b":
            create_spellbook()
            writespellbook()
        elif prompt == "s":
            search_func()
        elif prompt == "q":
            break
        else:
            continue
main()

search_func()
# create_spellbook()
# writespellbook()