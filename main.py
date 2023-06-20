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

class spell:
    def __init__(self,sp_lvl,name,desc,range,sComp,vComp,mComp,damage):
        self.sp_lvl = sp_lvl
        self.name = name
        self.desc = desc
        self.range = range
        self.sComp = sComp
        self.vComp = vComp
        self.mComp = mComp
        self.damage = damage

book = [],[]

def storespell(i): #sorts spell into book array by spell level
    book[i.sp_lvl].append(i)

def createspell(i,x): #creates spell class object and stores it....this might be redundant
    x = spell(i.sp_lvl,i.name,i.desc,i.range,i.vComp,i.sComp,i.mComp,i.damage)
    storespell(x)

def printout(z): #debug printing
    for x in book[z]:
        print(x.name)
        print(x.desc)
        print("_________________________________________________")

allspells = load_spells('modules.spellbook')
for i in allspells:
    createspell(i,i.name)
printout(0)
printout(1)