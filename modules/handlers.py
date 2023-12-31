import os
import ast
from random import randint
from character import *

class handler:

    @staticmethod
    def check_for_sheet():
        os.system('cls')
        if os.path.isfile('sheet.txt') == False:
            print('sheet.txt not found, creating new sheet...')
            return handler.pc_creator()
            
        else:
            return handler.load_sheet()
            

    @staticmethod #loads sheet.txt and turns it into a character object and returns the object
    def load_sheet():
        char = []
        with open('sheet.txt','r') as sheet:
            for line in sheet.readlines():    
                char.append(line.replace("\n",""))
        new_pc = character(char[0],char[1],char[2],ast.literal_eval(char[3]))
        return new_pc

    @staticmethod #creates a character object and saves it as sheet.txt
    def pc_creator(): 
        name = input("Input your character name: ")
        pc_class = input("Input character class: ").capitalize()
        pc_level = int(input("what level is the character: "))
        new_pc = newcharacter(name,pc_class,pc_level,handler.array_selector())
        with open('sheet.txt','w') as sheet:
            sheet.write(f"{new_pc.name}\n")
            sheet.write(f"{new_pc.pc_class}\n")
            sheet.write(f"{new_pc.level}\n")
            sheet.write(str(f"{new_pc.ability_scores}"))
        return new_pc

    @staticmethod #returns an array of 6 stats depending on preference for use in pc_creator()
    def array_selector():
        in_loop = True
        while in_loop == True:
            array_standard = [16, 15, 14, 13, 10, 10]
            array_heroic = [18, 16, 14, 12, 10, 10]
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
