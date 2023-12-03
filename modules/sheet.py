import os
import json
import ast
from random import randint
from character import *

class handler:

    @staticmethod
    def check_for_sheet():
        if os.path.isfile('sheet.txt') == False:
            print('sheet.txt not found, creating new sheet...')
            return handler.pc_creator()
            
        else:
            print("sheet.txt found...")
            return handler.load_sheet()
            

    @staticmethod
    def load_sheet():
        char = []
        with open('sheet.txt','r') as sheet:
            for line in sheet.readlines():    
                char.append(line.replace("\n",""))
        new_pc = character(char[0],char[1],char[2],ast.literal_eval(char[3]))
        return new_pc

    @staticmethod
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

    @staticmethod
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
    
    @staticmethod
    def random_roll(): #rolls 4d6, drops lowest adds the other 3, does this 6 times to make a stat array
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
    
print(handler.check_for_sheet().ability_modifiers)