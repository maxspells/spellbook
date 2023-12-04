import sys
import math
import msvcrt as m
sys.path.append('modules')
import os
import os.path
import time
from modules.pfapi import api
from modules.character import *
from modules.handlers import *
from modules.spell import spell

charactersheet = handler.check_for_sheet() #loads/creates sheet.txt and turns into class obj
newbook = []
book = [[],[],[],[],[],[],[],[],[],[]]
prepared = []

def query_spell(spell,splvl,spellsleft):
    x = spellsleft   
    if splvl == 0 and charactersheet.pc_class == "Wizard": #Wizards start will all lvl 0 spells in spellbook
        newbook.append(spell)
    elif x>0:
        query = False
        while query == False:
            print(f"Do you want to add {spell.name} to your spellbook?")
            prompt = input("y/n or d for description:")
            if prompt == "y":
                newbook.append(spell)
                x-=1
                query = True
            elif prompt == "d":
                art()
                spell.spell_description()
                print("\n")
            else:
                query = True
    return x

def create_spellbook():    
    wizard_exception = False
    for lvl in range(10): #spells levels 0-9
        spellsleft = charactersheet.spells_known[lvl]
        list_of_spell_obj = []    
        if spellsleft>0:
            totalspellsonlist = api.get_number_spells_perlvl(charactersheet.pc_class,lvl)
            spellnumber = 1
            print("Sorting spell list...")
            for page in range(5):
                sp_dict = api.splist_get(charactersheet.pc_class,lvl,(page+1))
                for item in sp_dict:
                    spell_obj = spell(item)
                    list_of_spell_obj.append(spell_obj)
            for sp_obj in list_of_spell_obj:                    
                if spellsleft > 0:
                    if lvl == 0  and charactersheet.pc_class == "Wizard": #this causes flashing if they are wizard, since wizards get all level 0 spells
                        if wizard_exception == False:
                            print("Adding all level 0 spells to spellbook")
                            wizard_exception = True    
                        spellsleft = query_spell(sp_obj,lvl,spellsleft)
                        spellnumber+=1
                    else:
                        art()
                        print(f"You can pick {spellsleft} more level {lvl} spells. {spellnumber}/{totalspellsonlist}")
                        spellsleft = query_spell(sp_obj,lvl,spellsleft)
                        spellnumber+=1 



def art():
    os.system('cls')
    time.sleep(.1)
    print("""
      ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\  
 //________.|.________\\ 
`----------`-'----------'
        Spellbook
https://github.com/maxspells""")
    print(f"{charactersheet.name}, level {charactersheet.level} {charactersheet.pc_class}.\n")

def wait():
    print("Press any key")
    m.getch()

def writespellbook():  #TODO REWORK THIS TO SAVE KNOWN SPELL ARRAY LIST
    w = open("spellbook.txt","w")
    header = -1
    for spell in newbook:
        if spell.classLevels[f"{charactersheet.pc_class}"] > header:
            w.write(f"-------Level {header+1} spells --------\n")
            header+=1
        w.write("-" + spell.name + "-" + "\n" + "\n")
        w.write(f"Casting time:{spell.castingTime}" + "\n")
        w.write(f"Target:{spell.targets}" + "\n")
        w.write(f"Duration:{spell.duration}" + "\n")
        w.write("--------------------------------------" + "\n")
        w.write(spell.description + "\n" + "\n")
        w.write("\n")
    w.close()

def search_func():
    while True:
        art()
        print("Type q to return to menu")
        prompt = input("Search a spell:")
        newspell = spell(api.search_spell(prompt))
        if prompt == "q":
            break
        else:
            art()
            newspell.spell_description()
            wait()

def main():
    while True:
        art()
        print("Create a spellbook 'b'")
        print("Search a spell = 's'")
        print("Create a new character = 'c'")
        print("Quit = 'q")
        prompt = input(':')
        if prompt == "b":
            create_spellbook()
            writespellbook()
        elif prompt == "s":
            search_func()
        elif prompt == "c":
            handler.pc_creator()
            print("you will need to reopen the program to continue")
            wait()
            break
        elif prompt == "q":
            break
        else:
            continue

main()

