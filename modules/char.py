from math import floor
class character:
    def __init__(self,name,stat_array,pc_class):
        self.name = name
        self.pc_class = pc_class    
        self.ability_scores = character.get_ability_dict(stat_array,pc_class)
        self.ability_modifiers = character.get_modifier_dict(self.ability_scores)

    def check_class(pc_class): #TODO assign spells known and spells per day to this function and implement with all classes /sigh
        match pc_class:
            case "Wizard":
                pass
            case "Cleric":
                pass
            case "Ranger":
                pass
            case "Druid":
                pass
            case "Sorcerer":
                pass
            case _:#nothing matched
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

    def get_ability_dict(stat_array,pc_class):
        print(f"checking stat list {stat_array}...")
        if len(stat_array) == 6:
            print(f"preparing to assign values to ability scores")
            stat_dict = {"Strength":[],"Dexterity":[],"Constitution":[],"Wisdom":[],"Intelligence":[],"Charisma":[]}
            stat_array.sort(reverse=True)
            character.check_class(pc_class)
            for stat in stat_array:
                stat_dict[character.query_stat(stat)].append(stat)
        else:
            return False
        return stat_dict
    

    def get_modifier_dict(stat_dict):
        mod_dict = {"Strength":[],"Dexterity":[],"Constitution":[],"Wisdom":[],"Intelligence":[],"Charisma":[]}
        for x in stat_dict:
            mod_dict[x].append(character.get_modifier(stat_dict[x][0]))
        return mod_dict

    def get_modifier(stat):
        return floor((stat-10)/2)


test_array = [10,12,14,16,18,20]
asha = character("Asha Greywynd",test_array,"Wizard")
print(asha.name)
print(asha.ability_scores)
print(asha.pc_class)
print(asha.ability_modifiers)


    