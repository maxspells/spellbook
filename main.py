class spell:
    def __init__(self,sp_lvl,name,desc,range,sComp,vComp,mComp,damage):
        self.sp_lvl = sp_lvl
        self.name = name
        self.desc = desc
        self.range = range
        self.sComp = sComp
        self.vComp = vComp
        self.mComp = mComp
        self.damage = damage

spellbook = [],[]

def storespell(i):
    spellbook[i.sp_lvl].append(i)

#light
sp_lvl = 0
name = "light"
desc = """This spell causes a touched object to glow like a torch, shedding normal 
light in a 20-foot radius from the point touched, and increasing the light level for 
an additional 20 feet by one step, up to normal light (darkness becomes dim light, 
and dim light becomes normal light). In an area of normal or bright light, this 
spell has no effect. The effect is immobile, but it can be cast on a movable object.

You can only have one light spell active at any one time. If you cast this spell 
while another casting is still in effect, the previous casting is dispelled. If you 
make this spell permanent (through permanency or a similar effect), it does not count 
against this limit. Light can be used to counter or dispel any darkness spell of equal 
or lower spell level."""
range = "touch"
vComp = True
sComp = False
mComp = "A firefly"
damage = "N/A"
sp_light = spell(sp_lvl,name,desc,range,vComp,sComp,mComp,damage) #creates light spell
storespell(sp_light) #stores light spell in array

#-------------------------------------------------------------------------------------#
#detect magic
sp_lvl = 0
name = "Detect Magic"
desc = """You detect magical auras. The amount of information revealed depends on how long you 
study a particular area or subject.

1st Round: Presence or absence of magical auras.

2nd Round: Number of different magical auras and the power of the most potent aura.

3rd Round: The strength and location of each aura. If the items or creatures bearing 
the auras are in line of sight, you can make Knowledge (arcana) skill checks to 
determine the school of magic involved in each. (Make one check per aura: DC 15 + 
spell level, or 15 + 1/2 caster level for a nonspell effect.) If the aura 
emanates from a magic item, you can attempt to identify its properties (see Spellcraft).

Magical areas, multiple types of magic, or strong local magical emanations may 
distort or conceal weaker auras.

Aura Strength: An aura’s power depends on a spell’s functioning spell level or an 
item’s caster level; see the accompanying table. If an aura falls into more than one 
category, detect magic indicates the stronger of the two."""
range = "60 ft cone"
vComp = True
sComp = True
mComp = "None"
damage = "N/A"

sp_detect = spell(sp_lvl,name,desc,range,vComp,sComp,mComp,damage) #same with detect magic spell
storespell(sp_detect)

#endspell

print(spellbook[0][0].name)
print(spellbook[0][0].desc)
print(spellbook[0][1].name)
print(spellbook[0][1].desc)# prints both spells names and description


