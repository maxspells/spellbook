# class blueprint:
#     sp_lvl = 
#     name = ""
#     desc = """ """
#     range = ""
#     vComp = 
#     sComp = 
#     mComp = 
#     damage = 

class detect_magic:
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

Aura Strength: An aura's power depends on a spell's functioning spell level or an 
item's caster level; see the accompanying table. If an aura falls into more than one 
category, detect magic indicates the stronger of the two."""
    range = "60 ft cone"
    vComp = True
    sComp = True
    mComp = False
    
class light:
    sp_lvl = 0
    name = "Light"
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
    mComp = True

class magic_missile:
    sp_lvl = 1
    name = "Magic Missile"
    desc = """A missile of magical energy darts forth from your fingertip and strikes 
its target, dealing 1d4+1 points of force damage.

The missile strikes unerringly, even if the target is in melee combat, so long as it 
has less than total cover or total concealment. Specific parts of a creature can't be 
singled out. Objects are not damaged by the spell.

For every two caster levels beyond 1st, you gain an additional missile - two at 3rd level,
three at 5th, four at 7th, and the maximum of five missiles at 9th level or higher. If 
you shoot multiple missiles, you can have them strike a single creature or several creatures. 
A single missile can strike only one creature. You must designate targets before you check 
for spell resistance or roll damage."""
    range = "100 ft. + 10 ft./level"
    vComp = True
    sComp = True
    mComp = False
    damage = "1d4+1"

class mage_hand:
    sp_lvl = 0
    name = "Mage Hand"
    desc = """You point your finger at an object and can lift it and move it at will 
from a distance. As a move action, you can propel the object as far as 15 feet in any 
direction, though the spell ends if the distance between you and the object ever exceeds 
the spell's range."""
    range = "close (25 ft. + 5 ft./2 levels)"
    vComp = True
    sComp = True
    mComp = False

class ghost_sound:
    sp_lvl = 0
    name = "Ghost Sound"
    desc = """Ghost sound allows you to create a volume of sound that rises, recedes, approaches,
or remains at a fixed place. You choose what type of sound ghost sound creates when casting
it and cannot thereafter change the sound's basic character.

The volume of sound created depends on your level. You can produce as much noise as four normal 
humans per caster level (maximum 40 humans). Thus, talking, singing, shouting, walking, marching, 
or running sounds can be created. The noise a ghost sound spell produces can be virtually any 
type of sound within the volume limit. A horde of rats running and squeaking is about the same 
volume as eight humans running and shouting. A roaring lion is equal to the noise from 16 humans, 
while a roaring dragon is equal to the noise from 32 humans. Anyone who hears a ghost sound 
receives a Will save to disbelieve.

Ghost sound can enhance the effectiveness of a silent image spell.

Ghost sound can be made permanent with a permanency spell."""
    range = "close (25 ft. + 5 ft./2 levels)"
    vComp = True
    sComp = True
    mComp = True

class prestidigitation:
    sp_lvl = 0
    name = "Prestidigitation"
    desc = """Prestidigitations are minor tricks that novice spellcasters use for practice. 
Once cast, a prestidigitation spell enables you to perform simple magical effects for 1 hour. 
The effects are minor and have severe limitations. A prestidigitation can slowly lift 1 pound 
of material. It can color, clean, or soil items in a 1-foot cube each round. It can chill, warm, 
or flavor 1 pound of nonliving material. It cannot deal damage or affect the concentration 
of spellcasters. Prestidigitation can create small objects, but they look crude and artificial. 
The materials created by a prestidigitation spell are extremely fragile, and they cannot be 
used as tools, weapons, or spell components. Finally, prestidigitation lacks the power to 
duplicate any other spell effects. Any actual change to an object (beyond just moving, cleaning, 
or soiling it) persists only 1 hour."""
    range = "10 feet"
    vComp = False
    sComp = False
    mComp = False

class open_close:
    sp_lvl = 0
    name = "Open/Close"
    desc = """You can open or close (your choice) a door, chest, box, window, bag, pouch, bottle, 
barrel, or other container. If anything resists this activity (such as a bar on a door or a 
lock on a chest), the spell fails. In addition, the spell can only open and close things 
weighing 30 pounds or less. Thus, doors, chests, and similar objects sized for enormous 
creatures may be beyond this spell's ability to affect."""
    range = "close (25 ft. + 5 ft./2 levels)"
    vComp = True
    sComp = True
    mComp = True

class enlarge_person:
    sp_lvl = 1
    name = "Enlarge Person"
    desc = """Range close (25 ft. + 5 ft./2 levels)
Target one humanoid creature
Duration 1 min./level (D)
Saving Throw Fortitude negates; Spell Resistance yes

DESCRIPTION

This spell causes instant growth of a humanoid creature, doubling its height and multiplying 
its weight by 8. This increase changes the creature's size category to the next larger one. 
The target gains a +2 size bonus to Strength, a -2 size penalty to Dexterity (to a minimum of 1)
, and a -1 penalty on attack rolls and AC due to its increased size.

A humanoid creature whose size increases to Large has a space of 10 feet and a natural reach 
of 10 feet. This spell does not change the target's speed.

If insufficient room is available for the desired growth, the creature attains the maximum 
possible size and may make a Strength check (using its increased Strength) to burst any 
enclosures in the process. If it fails, it is constrained without harm by the materials enclosing 
it–the spell cannot be used to crush a creature by increasing its size.

All equipment worn or carried by a creature is similarly enlarged by the spell. Melee weapons 
affected by this spell deal more damage (see Table: Medium/Large Weapon Damage). Other magical 
properties are not affected by this spell. Any enlarged item that leaves an enlarged creature’s 
possession (including a projectile or thrown weapon) instantly returns to its normal size. This 
means that thrown and projectile weapons deal their normal damage. Magical properties of enlarged 
items are not increased by this spell.

Multiple magical effects that increase size do not stack.
Enlarge person counters and dispels reduce person .
Enlarge person can be made permanent with a permanency spell."""

class protection_from_evil:
    sp_lvl = 1
    name = "Protection from Evil"
    desc = """Casting Time 1 standard action
Components V, S, M/DF

EFFECT

Range touch
Target creature touched
Duration 1 min./level (D)
Saving Throw Will negates (harmless); Spell Resistance no; see text

DESCRIPTION

This spell wards a creature from attacks by evil creatures, from mental control, 
and from summoned creatures. It creates a magical barrier around the subject at a 
distance of 1 foot. The barrier moves with the subject and has three major effects.

First, the subject gains a +2 deflection bonus to AC and a +2 resistance bonus on 
saves. Both these bonuses apply against attacks made or effects created by evil creatures.

Second, the subject immediately receives another saving throw (if one was allowed 
to begin with) against any spells or effects that possess or exercise mental control 
over the creature (including enchantment [charm] effects and enchantment [compulsion] 
effects, such as charm person, command, and dominate person). This saving throw is made 
with a +2 morale bonus, using the same DC as the original effect. If successful, such 
effects are suppressed for the duration of this spell. The effects resume when the 
duration of this spell expires. While under the effects of this spell, the target is 
immune to any new attempts to possess or exercise mental control over the target. This 
spell does not expel a controlling life force (such as a ghost or spellcaster using 
magic jar), but it does prevent them from controlling the target. This second effect 
only functions against spells and effects created by evil creatures or objects, 
subject to GM discretion.

Third, the spell prevents bodily contact by evil summoned creatures. This causes the 
natural weapon attacks of such creatures to fail and the creatures to recoil if such 
attacks require touching the warded creature. Summoned creatures that are not evil 
are immune to this effect. The protection against contact by summoned creatures ends 
if the warded creature makes an attack against or tries to force the barrier against 
the blocked creature. Spell Resistance can allow a creature to overcome this protection 
and touch the warded creature."""

class Shield:
    sp_lvl = 1
    name = "Shield"
    desc = """CASTING

Casting Time 1 standard action
Components V, S

EFFECT

Range personal
Target you
Duration 1 min./level (D)

DESCRIPTION

Shield creates an invisible shield of force that hovers in front of you. It negates 
magic missile attacks directed at you. The disk also provides a +4 shield bonus to 
AC. This bonus applies against incorporeal touch attacks, since it is a force effect. 
The shield has no armor check penalty or arcane spell failure chance."""

class mage_armor:
    sp_lvl = 1
    name = "Mage Armor"
    desc = """Casting Time 1 standard action
Components V, S, F (a piece of cured leather)

EFFECT

Range touch
Target creature touched
Duration 1 hour/level (D)
Saving Throw Will negates (harmless); Spell Resistance no

DESCRIPTION

An invisible but tangible field of force surrounds the subject of a mage armor spell, 
providing a +4 armor bonus to AC.

Unlike mundane armor, mage armor entails no armor check penalty, arcane spell failure 
chance, or speed reduction. Since mage armor is made of force, incorporeal creatures 
can't bypass it the way they do normal armor."""

class mount:
    sp_lvl = 1
    name = "Mount"
    desc = """Casting Time 1 round
Components V, S, M (a bit of horse hair)

EFFECT

Range close (25 ft. + 5 ft./2 levels)
Effect one mount
Duration 2 hours/level (D)
Saving Throw none; Spell Resistance no

DESCRIPTION

You summon a light horse or a pony (your choice) to serve you as a mount. 
The steed serves willingly and well. The mount comes with a bit and bridle 
and a riding saddle."""

class ear_piercing_scream:
    sp_lvl = 1
    name = "Ear Piercing Scream"
    desc = """Casting Time 1 standard action
Components V, S

EFFECT

Range close (25 ft. + 5 ft./2 levels)
Target one creature
Duration instantaneous; see text
Saving Throw Fortitude partial (see text); Spell Resistance yes

DESCRIPTION

You unleash a powerful scream, inaudible to all but a single target. The target is dazed for 
1 round and takes 1d6 points of sonic damage per two caster levels (maximum 5d6). A successful 
save negates the daze effect and halves the damage."""
class chill_touch:
    sp_lvl = 1
    name = "Chill Touch"
    desc = """Casting Time 1 standard action
Components V, S

EFFECT

Range close (25 ft. + 5 ft./2 levels)
Target one creature
Duration instantaneous; see text
Saving Throw Fortitude partial (see text); Spell Resistance yes

DESCRIPTION

You unleash a powerful scream, inaudible to all but a single target. The target is dazed for 
1 round and takes 1d6 points of sonic damage per two caster levels (maximum 5d6). A successful 
save negates the daze effect and halves the damage."""

class shocking_grasp:
    sp_lvl = 1
    name = "Shocking Grasp"
    desc = """Casting Time 1 standard action
Components V, S

EFFECT

Range touch
Target creature or object touched
Duration instantaneous
Saving Throw none; Spell Resistance yes

DESCRIPTION

Your successful melee touch attack deals 1d6 points of electricity damage per caster level 
(maximum 5d6). When delivering the jolt, you gain a +3 bonus on attack rolls if the opponent 
is wearing metal armor (or is carrying a metal weapon or is made of metal)."""

class magic_weapon:
    sp_lvl = 1
    name = "Magic Weapon"
    desc = """Casting Time 1 standard action
Components V, S, DF

EFFECT

Range touch
Target weapon touched
Duration 1 min./level
Saving Throw Will negates (harmless, object); Spell Resistance yes (harmless, object)

DESCRIPTION

Magic weapon gives a weapon a +1 enhancement bonus on attack and damage rolls. An enhancement 
bonus does not stack with a masterwork weapon's +1 bonus on attack rolls.

You can't cast this spell on a natural weapon, such as an unarmed strike (instead, see magic fang). 
A monk's unarmed strike is considered a weapon, and thus it can be enhanced by this spell."""

class touch_of_gracelessness:
    sp_lvl = 1
    name = "Touch of Gracelessness"
    desc = """Casting Time 1 standard action
Components V, S

EFFECT

Range touch
Targets creature touched
Duration 1 round/level
Saving Throw Fortitude partial; Spell Resistance yes

DESCRIPTION

With a single touch, you reduce a creature to a fumbling clown.

The target takes a penalty to its Dexterity equal to 1d6+1 per two caster levels (maximum 1d6+5). 
This penalty cannot drop the target's Dexterity score below 1.

In addition, if the subject moves more than half its speed, it falls prone. If the subject flies, 
its maneuverability is reduced by one step (perfect maneuverability becomes good, good becomes 
average, and so on).

A successful Fortitude save halves the penalty to Dexterity and negates the possibility of falling 
prone or the reduction to fly maneuverabilities."""

class invisibility:
    sp_lvl = 2
    name = "Invisibility"
    desc = """Casting Time 1 standard action
Components V, S, M/DF (an eyelash encased in gum arabic)

EFFECT

Range personal or touch
Target you or a creature or object weighing no more than 100 lbs./level
Duration 1 min./level (D)
Saving Throw Will negates (harmless) or Will negates (harmless, object); Spell Resistance yes (harmless) 
or yes (harmless, object)

DESCRIPTION

The creature or object touched becomes invisible. If the recipient is a creature carrying gear, that 
vanishes, too. If you cast the spell on someone else, neither you nor your allies can see the subject, 
unless you can normally see invisible things or you employ magic to do so.

Items dropped or put down by an invisible creature become visible; items picked up disappear if tucked 
into the clothing or pouches worn by the creature. Light, however, never becomes invisible, although a 
source of light can become so (thus, the effect is that of a light with no visible source). Any part of 
an item that the subject carries but that extends more than 10 feet from it becomes visible.

Of course, the subject is not magically silenced, and certain other conditions can render the recipient 
detectable (such as swimming in water or stepping in a puddle). If a check is required, a stationary 
invisible creature has a +40 bonus on its Stealth checks. This bonus is reduced to +20 if the creature 
is moving. The spell ends if the subject attacks any creature. For purposes of this spell, an attack 
includes any spell targeting a foe or whose area or effect includes a foe. Exactly who is a foe depends 
on the invisible character's perceptions. Actions directed at unattended objects do not break the spell. 
Causing harm indirectly is not an attack. Thus, an invisible being can open doors, talk, eat, climb stairs, 
summon monsters and have them attack, cut the ropes holding a rope bridge while enemies are on the bridge, 
remotely trigger traps, open a portcullis to release attack dogs, and so forth. If the subject attacks 
directly, however, it immediately becomes visible along with all its gear. Spells such as bless that 
specifically affect allies but not foes are not attacks for this purpose, even when they include foes 
in their area.

Invisibility can be made permanent (on objects only) with a permanency spell."""

class levitate:
    sp_lvl = 2
    name = "Levitate"
    desc = """Casting Time 1 standard action
Components V, S, F (a leather loop or golden wire bent into a cup shape)

EFFECT

Range personal or close (25 ft. + 5 ft./2 levels)
Target you or one willing creature or one object (total weight up to 100 lbs./level)
Duration 1 min./level (D)
Saving Throw none; Spell Resistance no

DESCRIPTION

Levitate allows you to move yourself, another creature, or an object up and down as you wish. 
A creature must be willing to be levitated, and an object must be unattended or possessed by a 
willing creature. You can mentally direct the recipient to move up or down as much as 20 feet 
each round; doing so is a move action. You cannot move the recipient horizontally, but the 
recipient could clamber along the face of a cliff, for example, or push against a ceiling to 
move laterally (generally at half its base land speed).

A levitating creature that attacks with a melee or ranged weapon finds itself increasingly 
unstable; the first attack has a -1 penalty on attack rolls, the second -2, and so on, to a 
maximum penalty of -5. A full round spent stabilizing allows the creature to begin again at -1."""

class owls_wisdom:
    sp_lvl = 2
    name = "Owl's Wisdom"
    desc = """Casting Time 1 standard action
Components V, S, M/DF (feathers or droppings from an owl)

EFFECT

Range touch
Target creature touched
Duration 1 min./level
Saving Throw Will negates (harmless); Spell Resistance yes

DESCRIPTION

The transmuted creature becomes wiser. The spell grants a +4 enhancement bonus to Wisdom, adding 
the usual benefit to Wisdom-related skills. Clerics, druids, and rangers (and other Wisdom-based 
spellcasters) who receive owl's wisdom do not gain any additional bonus spells for the increased 
Wisdom, but the save DCs for their spells increase."""

class cats_grace:
    sp_lvl = 2
    name = "Cat's Grace"
    desc = """Casting Time 1 standard action
Components V, S, M (pinch of cat fur)

EFFECT

Range touch
Target creature touched
Duration 1 min./level
Saving Throw Will negates (harmless); Spell Resistance yes

DESCRIPTION

The transmuted creature becomes more graceful, agile, and coordinated. The spell grants a +4 
enhancement bonus to Dexterity, adding the usual benefits to AC, Reflex saves, and other uses of 
the Dexterity modifier."""

class foxs_cunning:
    sp_lvl = 2
    name = "Fox's Cunning"
    desc = """Casting Time 1 standard action
Components V, S, M/DF (hairs or dung from a fox)

EFFECT

Range touch
Target creature touched
Duration 1 min./level
Saving Throw Will negates (harmless); Spell Resistance yes

DESCRIPTION

The target becomes smarter. The spell grants a +4 enhancement bonus to Intelligence, adding 
the usual benefits to Intelligence-based skill checks and other uses of the Intelligence modifier. 
Wizards (and other spellcasters who rely on Intelligence) affected by this spell do not gain any 
additional bonus spells for the increased Intelligence, but the save DCs for spells they cast 
while under this spell's effect do increase. This spell doesn't grant extra skill ranks."""