import sys
sys.path.append('modules')
import inspect
import importlib

import modules.spellbook as spellbook
from modules.spellbook import *

def load_spells(module_name): # checks spellbook.py for classes. If it's a class, imports it and adds 
    module = importlib.import_module(module_name) # it to an array and returns array
    list = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            list.append(obj)
    return list

book = [],[]

def storespell(i): #sorts spell into book array by spell level
    book[i.sp_lvl].append(i)


def printout(z): #debug printing
    for x in book[z]:
        print(x.name)
        print(x.desc)
        print("_________________________________________________")

allspells = load_spells('modules.spellbook')
for i in allspells:
    storespell(i)
printout(0)
printout(1)