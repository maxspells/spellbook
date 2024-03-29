from math import floor
class character:
    def __init__(self, name, pc_class, level, stat_dict):
        self.name = name
        self.pc_class = pc_class
        self.level = level
        self.ability_scores = stat_dict
        self.ability_modifiers = character.get_modifier_dict(self.ability_scores)
        self.spells_known = [4,15,5,4,0,0,0,0,0,0] #TODO THIS IS A PLACEHOLDER, NEED TO MAKE FUNCTION TO CALCULATE THIS

    def check_primary_stat(pc_class):
        match pc_class: #checks primary casting stat used for bonus spells per day in spell_handlers.bonusspells
            case "Wizard":
                return "Intelligence"
            case "Cleric":
                return "Wisdom"
            case "Ranger":
                return "Wisdom"
            case "Druid":
                return "Wisdom"
            case "Sorcerer":
                return "Charisma"
            case _:#nothing matched #TODO implement this exception
                return False
            
    def query_stat(stat):
            ability_array = ["Strength",'Dexterity',"Constitution","Wisdom","Intelligence","Charisma"]
            print(f"Where do you want to put your {stat}?:")
            query = input(f"{ability_array[0]}:a {ability_array[1]}:d {ability_array[2]}:c {ability_array[3]}:w {ability_array[4]}:i {ability_array[5]}:r")
            match query:
                case "a":
                    return ability_array.pop(0)
                case "d":
                    return ability_array.pop(1)
                case "c":
                    return ability_array.pop(2)
                case "w":
                    return ability_array.pop(3)
                case "i":
                    return ability_array.pop(4)
                case "r":
                    return ability_array.pop(5)
                case _ :                    
                    return False #TODO implement this exception

    def get_modifier_dict(stat_dict):
        mod_dict = {"Strength":[],"Dexterity":[],"Constitution":[],"Wisdom":[],"Intelligence":[],"Charisma":[]}
        for x in stat_dict:
            mod_dict[x].append(character.get_modifier(stat_dict[x][0]))
        return mod_dict

    def get_modifier(stat):
        return floor((stat-10)/2)

class newcharacter(character):
    def __init__(self, name, pc_class, level, stat_array):
        self.name = name
        self.pc_class = pc_class
        self.level = level
        self.ability_scores = newcharacter.get_ability_dict(stat_array)
        self.ability_modifiers = character.get_modifier_dict(self.ability_scores)
        self.spells_known = [4,15,5,4,0,0,0,0,0,0] #TODO THIS IS A PLACEHOLDER, NEED TO MAKE FUNCTION TO CALCULATE THIS

    def get_ability_dict(stat_array):
        print(f"checking stat list {stat_array}...")
        if len(stat_array) == 6:
            print(f"preparing to assign values to ability scores")
            stat_dict = {"Strength":[],"Dexterity":[],"Constitution":[],"Wisdom":[],"Intelligence":[],"Charisma":[]}
            stat_array.sort(reverse=True)
            for stat in stat_array:
                stat_dict[character.query_stat(stat)].append(stat)
        else:
            return False
        return stat_dict

