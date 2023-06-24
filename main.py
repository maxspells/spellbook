import sys
sys.path.append('modules')
import inspect
import importlib
import modules.spellbook as spellbook
import modules.character as character
from modules.character import chr
from modules.spellbook import *

book = [],[]
prepared = [],[]

def load_spells(module_name): # checks spellbook.py for classes. If it's a class, imports it and adds 
    module = importlib.import_module(module_name) # it to an array and returns array
    list = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            list.append(obj)
    return list

def storespell(i): #sorts spell into book array by spell level
    book[i.sp_lvl].append(i)

def printout(z): #debug printing
    for x in book[z]:
        print(x.name)
        print(x.range)
        print(x.desc)
        print("_________________________________________________")

def modifier(char):
    mod = 0
    match char.int:
        case 6 | 7:
            mod = -2
        case 8 | 9:
            mod = -1
        case 10 | 11:
            mod = 0
        case 12 | 13:
            mod = 1
        case 14 | 15:
            mod = 2
        case 16 | 17:
            mod = 3
        case 18 | 19:
            mod = 4
        case 20 | 21:
            mod = 5
        case 22 | 23:
            mod = 6
        case 24 | 25:
            mod = 7
    return mod

def bonusspells(char):
    bonus = [0,0,0,0,0,0,0,0,0,0]
    match char.int:
        case 12 | 13:
            bonus = [0,1,0,0,0,0,0,0,0,0]
        case 14 | 15:
            bonus = [0,1,1,0,0,0,0,0,0,0]
        case 16 | 17:
            bonus = [0,1,1,1,0,0,0,0,0,0]
        case 18 | 19:
            bonus = [0,1,1,1,1,0,0,0,0]
        case 20 | 21:
            bonus = [0,2,1,1,1,1,0,0,0,0]
        case 22 | 23:
            bonus = [0,2,2,1,1,1,0,0,0,0]
        case 24 | 25:
            bonus = [0,2,2,2,1,1,1,1,0,0]
    return bonus

def perday(char):
    spd = []
    z = 0
    bonus = bonusspells(char)
    core = char.spellsperday
    for i in range(len(core)):
        spd.append(core[z]+bonus[z])
        z+=1
    return spd

sp_perday = perday(chr)

allspells = load_spells('modules.spellbook')
for i in allspells:
    storespell(i)

#[4, 4, 2, 1, 1, 1, 0, 0, 0, 0]
def prepare():
    dex = 0
    availableslots = perday(chr)
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
prepare()
