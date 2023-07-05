import sys
import math
import msvcrt as m
sys.path.append('modules')
import inspect
import importlib
import os
import os.path
#import modules.spellbook as spellbook
import modules.character as character
from modules.character import chr
#from modules.spellbook import *

book = [],[]
prepared = [],[]

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

def printout(z): #debug printing function
    for x in book[z]:
        print(x.name)
        print(x.range)
        print(x.desc)
        print("_________________________________________________")

def modifier(stat): #calculates intelligence modifier for spells that use it
    mod = math.floor((stat-10)/2)
    return mod

def bonusspells(char): #calculates bonus spells based on intelligence stat
    bonus = [0,0,0,0,0,0,0,0,0,0]
    match char.int:
        case 12 | 13:
            bonus = [0,1,0,0,0,0,0,0,0,0]
        case 14 | 15:
            bonus = [0,1,1,0,0,0,0,0,0,0]
        case 16 | 17:
            bonus = [0,1,1,1,0,0,0,0,0,0]
        case 18 | 19:
            bonus = [0,1,1,1,1,0,0,0,0,0]
        case 20 | 21:
            bonus = [0,2,1,1,1,1,0,0,0,0]
        case 22 | 23:
            bonus = [0,2,2,1,1,1,0,0,0,0]
        case 24 | 25:
            bonus = [0,2,2,2,1,1,1,1,0,0]
    return bonus

def perday(char): #calculates how many spells per day can be prepared per spell level
    spd = []
    z = 0
    bonus = bonusspells(char)
    core = char.spellsperday
    for i in range(len(core)):
        if(core[z]>0): # if you can't cast spells of this level, skips adding bonus
            spd.append(core[z]+bonus[z]) 
        else:
            spd.append(core[z])
        z+=1
    return spd




#[4, 4, 2, 1, 1, 1, 0, 0, 0, 0]
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
    while(availableslots[dex]>0):
        if (dex<=(len(book)-1)):
            for spell in book[dex]:
                print(f"preparing level {spell.sp_lvl} spells")
                if availableslots[dex]>0:
                    if input(f"Do you want to prepare {spell.name}?") == "y":
                        print(f"preparing {spell.name}")
                        availableslots[dex] -= 1
                        prepared[dex].append(spell)
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
        Spellbook v0.1⠀""")
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
        print("spellbook.py found, spells imported")
    else:
        print("No spellbook.py file found in modules folder")
    if (os.path.isfile("modules/character.py")==True):
        print("character.py found")
        import modules.character as chr
    else:
        print("character.py not found")   
start()
prepare()