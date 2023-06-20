import sys
sys.path.append('modules')
import inspect
import importlib

import modules.spellbook as spellbook
from modules.spellbook import *

def load_spells(module_name):
    module = importlib.import_module(module_name)
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

def storespell(i):
    book[i.sp_lvl].append(i)

def createspell(i,x):
    x = spell(i.sp_lvl,i.name,i.desc,i.range,i.vComp,i.sComp,i.mComp,i.damage)
    storespell(x)

# createspell(spellbook.detect_magic,spellbook.detect_magic.name)
# createspell(spellbook.light,spellbook.light.name)
# createspell(spellbook.magic_missile,spellbook.magic_missile.name)

def printout(z):
    for x in book[z]:
        print(x.name)
        print(x.desc)
        print("_________________________________________________")

allspells = load_spells('modules.spellbook')
for i in allspells:
    print(i.name)