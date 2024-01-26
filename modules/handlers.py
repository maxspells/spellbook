import os
import ast
from random import randint
from pfapi import api
from character import *
from spell import spell
import msvcrt as m
from main import art
class handler:

    @staticmethod
    def check_for_sheet():
        art()
        if os.path.isfile('sheet.data') == False:
            print('character not found, creating new character...')
            return handler.pc_creator()
        else:
            return handler.load_sheet()
            

    @staticmethod #loads sheet.txt and turns it into a character object and returns the object
    def load_sheet():
        char = []
        with open('sheet.data','r') as sheet:
            for line in sheet.readlines():    
                char.append(line.replace("\n",""))
        new_pc = character(char[0],char[1],char[2],ast.literal_eval(char[3]))
        return new_pc

    @staticmethod #creates a character object and saves it as sheet.txt
    def pc_creator(): 
        name = input("Input your character name: ")
        pc_class = input("Input character class: ").capitalize()
        pc_level = int(input("What level is the character: "))
        stat_array = handler.array_selector()
        new_pc = newcharacter(name,pc_class,pc_level,stat_array)
        with open('sheet.data','w') as sheet:
            sheet.write(f"{new_pc.name}\n")
            sheet.write(f"{new_pc.pc_class}\n")
            sheet.write(f"{new_pc.level}\n")
            sheet.write(str(f"{new_pc.ability_scores}"))
        return new_pc

    @staticmethod #returns an array of 6 stats depending on preference for use in pc_creator()
    def array_selector():
        in_loop = True
        while in_loop:
            array_standard = [16, 15, 14, 13, 10, 10]
            array_heroic = [18, 16, 14, 12, 10, 10]
            art()
            print("Which array would you like to use for your stats?")
            print(f"Standard array: {array_standard}")
            print(f"Heroic array: {array_heroic}")
            print("You can also input your own stats or you can roll for your stats \n")
            query = input("Heroic = h, Standard = s, Input stats = i, Random = r: ")
            match query:
                case "h":
                    in_loop == False
                    return array_heroic
                case "s":
                    in_loop == False
                    return array_standard
                case "i":
                    input_array = []
                    for dex in range(6):
                        stat = input(f"Input stat {dex+1}: ")
                        input_array.append(stat)
                    in_loop == False
                    return input_array
                case "r":
                    random_loop = True
                    while random_loop == True:
                        random_array = handler.random_roll()
                        print(random_array)
                        random_query = input("Do you want to keep this array? y/n: ")
                        if random_query == "y":
                            random_loop = False
                            in_loop == False
                            return random_array
                        else:
                            continue
                case _:
                    print("invalid input")
                    continue
    
    @staticmethod #rolls 4d6, drops lowest adds the other 3, does this 6 times to make a stat array.
    def random_roll(): 
        stat_array = []
        for _ in range(6):
            roll_array = []
            for _ in range(4):
                roll_array.append(randint(1,6))
            roll_array.sort()
            roll_array.pop(0)
            stat_to_append = 0
            for roll in roll_array:
                stat_to_append += roll
            stat_array.append(stat_to_append)
        return stat_array

class spellbook:
    @staticmethod #returns True is spell is selected, or false if passed
    def query_spell(spell_dict):       
        inloop = True
        while inloop == True:
            print(f'Do you want to add {spell_dict['name']} to your spellbook?')
            query = input("y/n or 'd' for description")
            if query == "y":
                inloop = False
                return True
            elif query == "n":
                inloop = False
                return False
            elif query == "d":
                newspell = spell(spell_dict)
                newspell.spell_description()
                m.getch()
                os.system('cls')
            else:
                continue

    #return array of selected spell dictionaries
    def parse_all_spells(pc_class,spells_known_array):
        selected_spells = [] #list of spell dicts
        wizard_exception = False #checks if all level 0 spells need to be auto added later
        for lvl in range(10): #spells level 0-9
            if pc_class == 'Wizard' and lvl == 0:
                print("Wizards start with all level 0 spells, adding to spellbook...")
                wizard_exception = True
            list_current_level_spell_dicts = []
            spellsleft = spells_known_array[lvl]
            total_spells_perlvl = 0
            if spellsleft > 0:
                page_index = 1
                searching_for_spells = True
                while searching_for_spells == True: #checks until no results returned
                    page_array = api.splist_get(pc_class,lvl,page_index)
                    length = len(page_array)
                    if length > 0:
                        for spell_dict in page_array:
                            list_current_level_spell_dicts.append(spell_dict)
                        total_spells_perlvl+=length
                        print(f'{total_spells_perlvl} lvl {lvl} spells found')
                        page_index+=1
                    else:
                        searching_for_spells = False
            for spell in list_current_level_spell_dicts:
                if wizard_exception == True and lvl == 0:
                    selected_spells.append(spell)
                elif spellsleft > 0:
                    os.system('cls')
                    print(f"You can select {spellsleft} more level {lvl} spells {list_current_level_spell_dicts.index(spell)+1}/{total_spells_perlvl}")
                    if spellbook.query_spell(spell) == True:
                        selected_spells.append(spell)
                        spellsleft-=1
        spellbook.write_spellbook_data(selected_spells)
        return selected_spells

    @staticmethod #input spell dict list, writes to file
    def write_spellbook_data(spell_dict_list):
        with open('spellbook.data','w') as book:
            for spell_dict in spell_dict_list:
                book.write(str(spell_dict)+"\n")

    @staticmethod
    def write_spellbook_txt(spell_dict_list,sheet):
        with open('spellbook.txt','w') as w:
            header = -1
            for sp in spell_dict_list:
                newspell = spell(sp)
                if newspell.classLevels[f"{sheet.pc_class}"] > header:
                    w.write(f"-------Level {header+1} spells --------\n")
                    header+=1
                w.write("-" + newspell.name + "-" + "\n" + "\n")
                w.write(f"Casting time:{newspell.castingTime}" + "\n")
                w.write(f"Target:{newspell.targets}" + "\n")
                w.write(f"Duration:{newspell.duration}" + "\n")
                w.write("--------------------------------------" + "\n")
                w.write(newspell.description + "\n" + "\n")
                w.write("\n")

    @staticmethod
    def load_spellbook_data(): #loads file, returns array of dictionaries
        book_array = [] #full of dictionaries
        with open('spellbook.data','r') as book:
            for line in book.readlines():
                book_array.append(ast.literal_eval(line))
        return book_array
    
    @staticmethod
    def check_for_spellbook():
        if os.path.isfile('spellbook.data') == True:
            return spellbook.load_spellbook_data()
        else:
            return False
        
    @staticmethod
    def add_newspell_to_spellbook():
        pass
    
class spell_handler:
    @staticmethod #returns array of spells per level
    def core_spells(character_level):
        match character_level:
            case 1:
                charspells = [3,1,0,0,0,0,0,0,0,0]
            case 2:
                charspells = [4,2,0,0,0,0,0,0,0,0]
            case 3:
                charspells = [4,2,1,0,0,0,0,0,0,0]
            case 4:
                charspells = [4,3,2,0,0,0,0,0,0,0]
            case 5:
                charspells = [4,3,2,1,0,0,0,0,0,0]
            case 6:
                charspells = [4,3,3,2,0,0,0,0,0,0]
            case 7:
                charspells = [4,4,3,2,1,0,0,0,0,0]
            case 8:
                charspells = [4,4,3,3,2,0,0,0,0,0]
            case 9:
                charspells = [4,4,4,3,2,1,0,0,0,0]
            case 10:
                charspells = [4,4,4,3,3,2,0,0,0,0]
            case 11:
                charspells = [4,4,4,4,3,2,1,0,0,0]
            case 12:
                charspells = [4,4,4,4,3,3,2,0,0,0]
            case 13:
                charspells = [4,4,4,4,4,3,2,1,0,0]
            case 14:
                charspells = [4,4,4,4,4,3,3,2,0,0]
            case 15:
                charspells = [4,4,4,4,4,4,3,2,1,0]
            case 16:
                charspells = [4,4,4,4,4,4,3,3,2,0]
            case 17:
                charspells = [4,4,4,4,4,4,4,3,2,1]
            case 18:
                charspells = [4,4,4,4,4,4,4,3,3,2]
            case 19:
                charspells = [4,4,4,4,4,4,4,4,3,3]
            case 20:
                charspells = [4,4,4,4,4,4,4,4,4,4]
        return charspells
    
    @staticmethod
    def bonusspells(primary_stat): #calculates bonus spells per day based on primary casting stat
        match primary_stat:
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
    
    @staticmethod
    def spells_per_day(pc_class,pc_level): #calculates how many spells per day can be prepared per spell level
        spd = []
        z = 0
        bonus = spell_handler.bonusspells(character.check_primary_stat(pc_class))
        core = spell_handler.core_spells(pc_level)
        for i in range(len(core)):
            if(core[z]>0): # if you can't cast spells of this level, skips adding bonus
                spd.append(core[z]+bonus[z]) 
            else:
                spd.append(core[z])
            z+=1
        return spd
