from pfapi import api
import os
class spell:
    def __init__(self,spell_dict):
        self.name = spell_dict["name"]
        self.summary = spell_dict["summary"]
        self.description = spell_dict["description"]
        self.classLevels = spell_dict["classLevels"]#returns dictionary
        self.spellResistance = spell_dict["spellResistance"]
        self.savingThrow = spell_dict["savingThrow"]
        self.hasDivineFocusComponent = spell_dict["hasDivineFocusComponent"]
        self.hasFocusComponent = spell_dict["hasFocusComponent"]
        self.hasMaterialComponent = spell_dict["hasMaterialComponent"]
        self.hasSomaticComponent = spell_dict["hasSomaticComponent"]
        self.hasVerbalComponent = spell_dict["hasVerbalComponent"]
        self.hasCostlyComponents = spell_dict["hasCostlyComponents"]
        self.materialCosts = spell_dict["materialCosts"]
        self.isDismissable = spell_dict["isDismissable"]
        self.isShapeable = spell_dict["isShapeable"]
        self.isMythic = spell_dict["isMythic"]
        self.castingTime = spell_dict["castingTime"]
        self.duration = spell_dict["duration"]
        self.area = spell_dict["area"]
        self.effect = spell_dict["effect"]
        self.range = spell_dict["range"]
        self.targets = spell_dict["targets"]
        self.school = spell_dict["school"]
        self.source = spell_dict["source"]#returns dictionary
    
    def spell_description(self):
        print("\n")
        print(f"-{self.name}-")
        print(f"{self.classLevels}")
        print("--------------------------------------")
        print(f"Casting time:{self.castingTime}")
        print(f"Target:{self.targets}")
        print(f"Range:{self.range}")
        print(f"Duration:{self.duration}")
        print("--------------------------------------")
        print(self.description)
        