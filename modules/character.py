class chr:
    pc_class = "Wizard"
    level = 4
    name = "Asha Greywynd"
    str = 10
    dex = 14
    con = 12
    int = 20
    wis = 16
    cha = 10
    spellsknown = [0,15,5,4,0,0,0,0,0,0] #if wizard


def charspells():
    match chr.level:
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

def bonusspells(): #calculates bonus spells based on intelligence stat
    match chr.int:
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

class chr_spells:
    spellsperday = charspells()
    bonus = bonusspells()

