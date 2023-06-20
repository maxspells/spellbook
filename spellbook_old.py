import random

class PlayerCharacter:
    charName = ""
    charClass = ""
    charStats = []


#rolls 4d6, takes out lowest adds the other 3
def statRoll():
    rollSum = 0
    rollArray = []
    
    for _ in range(4):
        rollArray.append(random.randint(1, 6))
    
    minroll = min(rollArray)
    
    for roll in rollArray:
        if roll != minroll:
            rollSum += roll
    
    return rollSum

#creates 6 stats
def getStats():
    statArray = []
    x = len(statArray)
    while(x < 6):
        stat = statRoll()
        statArray.append(stat)
        x = len(statArray)
    return statArray

newchar = PlayerCharacter
newchar.charName = input("Enter character name:")
newchar.charClass = input("Enter character class:")
newchar.charStats = getStats()

def create_statFile(filename, stats):
    with open(filename, 'w') as file:
        for stat in stats:
            file.write(str(stat) + '\n')

stats = getStats()
create_statFile("asha.txt",stats)
