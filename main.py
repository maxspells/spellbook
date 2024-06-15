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

def main():
    while True:
        global charactersheet
        global book
        charactersheet = handler.check_for_sheet() #loads/creates sheet.txt and turns into class obj
        book = spellbook.check_for_spellbook()
        art()
        header(charactersheet,book)
        if book == False:
            print("Create a spellbook 'b'")
        else:
            print("Create spellbook.txt file = 'b'")
        print("Search a spell = 's'")
        print("Create a new character = 'c'")
        print("Quit = 'q")
        prompt = input(':')
        if prompt == "b" and book == False:
            spellbook.parse_all_spells(charactersheet.pc_class,charactersheet.spells_known)
        elif prompt == "b":
            spellbook.write_spellbook_txt(book,charactersheet)
            print("Spellbook written to 'spellbook.txt'")
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


def art():
    os.system('cls')
    time.sleep(.05)
    print("""s
          
      ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\  
 //________.|.________\\ 
`----------`-'----------'
        Spellbook
https://github.com/maxspells""")
    
def header(sheet,book):
    print(f"{sheet.name}, level {sheet.level} {sheet.pc_class}.")
    if book != False:
        print("Spellbook data loaded.\n")
    else:
        print('\n')

def wait():
    print("Press any key")
    m.getch()


def search_func():
    while True:
        art()
        header(charactersheet,book)
        print("Type q to return to menu")
        prompt = input("Search a spell:")
        if prompt == "q":
            break
        else:
            newspell = spell(api.search_spell(prompt))
            art()
            newspell.spell_description()
            wait()


if __name__ == "__main__":
    main()

