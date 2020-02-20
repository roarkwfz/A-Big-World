import os, sys, time, random
from math import sqrt
from monster import *
from character import Player
from item import *

#Words that appear when the player is around boss or merchant
baroundwords = ['I remember a time when men were kind and they didn’t fight each other.But then everyone decided to choose the hard way of living. So, what about you? Do you dare to fight me?', 'Now, human, nothing against your race, the issue only lies between you and me. Let’s finish this right here!','I can almost smell it in you, the thirst of blood, the untamed wildness. Guess what, I’ll help you to discover your real SELF!', 'You make me think of a distant past, and I don’t like it. We need to settle this down. Take up your weapon.']
merchantwords = ['I have everything that you have and you don’t have.','I am the GUARDIAN OF FOREVER!!!','Guess what, you are now standing in front of the only merchant in town.','What can I get from you?','What can I get for you?']

#generates the heal potions that would be used
hPotion1 = healPotion("A Heal Potion", "A physician heals thyself, but you're not a physician anyway.", 1, 10, 10)
hPotion2 = healPotion("Another Heal Potion", "On your way of becoming a physician, huh?", 2, 20, 20)
hPotion3 = healPotion('A more powerful Heal Potion', 'A righteous human never cheats. Shame on you using potions.', 3, 30, 35)
hPotion4 = healPotion('The most powerful Heal Potion', 'Heal potions only give you an illusion of feeling better. In the end, you shall find yourself still on the path to failure.', 4, 40, 50)
hPotionls = [hPotion1, hPotion2, hPotion3, hPotion4]

#generates the magic potions that would be used
mPotion1 = magicPotion("A Magic Potion", "Don't you just wonder why you can't restore magic by yourself?", 1, 5, 10)
mPotion2 = magicPotion("Another Magic Potion", "That's because magic is never meant to be used.", 2, 10, 20)
mPotion3 = magicPotion('A more powerful Magic Potion', 'Have you ever wondered how magic became known to people like you and me?', 3, 15, 40)
mPotion4 = magicPotion('The most powerful Magic Potion', 'Thought you’ve not. This is a game, games ought to have magic. HAHA.', 4, 20, 50)
mPotionls = [mPotion1, mPotion2, mPotion3, mPotion4]

#generates the weapons
w_woodenStick = Weapon('A Wooden Stick', 'A stick made of wood, looks heavy', 5, 1.2, 40)
w_plasticDagger = Weapon('A Plastic Dagger', 'A dagger made of plastic. What is plastic to you? Light but sharp.', 1, 1.4, 80)
w_thinSword = Weapon('A Thin Sword', 'A sword made of metal you can’t tell', 4, 1.8, 120)
w_broadSword = Weapon('A Broad Sword', 'It looks so heavy.', 7, 2.7, 400)
w_toyKnife = Weapon('A Toy Knife', 'How can kids nowadays play with this? Shouldn’t their parents be worried?', 3, 2.3,300)
w_macbethDagger = Weapon('The dagger Lady Macbeth used', 'You can still see dry blood that once belonged to King Duncan on it’s blade. You wonder how the dagger came here.', 2, 3.8, 823)
weaponls = [w_woodenStick, w_plasticDagger, w_thinSword, w_broadSword, w_toyKnife, w_macbethDagger]

#generates the armors
a_woodenShield = Armor('A Wooden Shield', 'A shield made of wood, looks unbreakable', 5, 1.4, 40)
a_fancyHelmet = Armor('A Fancy Helmet', 'A shinny helmet with feather decorations', 2, 1.2, 35)
a_bandana = Armor('A Bandana', 'A red and black bandana. It keeps you warm in the chilling wind.', 3, 1.6, 80)
a_chainmail = Armor('A Chainmail', 'A chainmail that protects you from most physical attacks, but difficult to wear', 9, 3, 592)
a_woolCloak = Armor('A Black Wool Cloak', 'Despite it is draping  over your shoulders and seems to fall at any time, you feel yourself moving more swiftly with the cloak.', 6, 2.6, 300)
a_newClothes = Armor('The Emperor’s New Clothes', 'The power of imagination is infinite. Imagine yourself to never be defeated!', 0, 3.7, 948)
armorls = [a_woodenShield, a_chainmail,a_bandana, a_newClothes, a_woolCloak, a_fancyHelmet]

#keys
doorKey = DoorKey()
chestKey = ChestKey()

#generates materials that can be used to make useful items
m_breathOfLife = Material('Breath of Life', 'Just what the name says', 0, 276)
m_pileOfEarth = Material('An Innocent Pile of Earth', 'You can get this everywhere.', 1, 40)
m_bottle = Material('A Bottle', 'You feel like you can always recycle the bottle once you drank the potion inside. But NO.', 1, 20)
m_rock = Material('A Piece of Rock', 'The whole thing looks strange. The rock doesn\'t belong here.', 1, 80)
m_hotChocolate = Material('A Cup of Hot Chocolate with Cinnamon Roll', 'Nothing tastes better if you add this to your heal potion recipe.', 2, 302)
m_air = Material('A Bag of Trembling Emotions', 'Can you name all the different species?', 5, 641)
m_plastic = Material('A Thin Slice of Plastic', 'Cheerful color, sharp edge. It keeps you happy, makes you even happier when you find a handle to hold it.', 2, 319)
materialls = [m_breathOfLife, m_pileOfEarth, m_bottle, m_rock, m_hotChocolate, m_air, m_plastic]

#generates containers that can increase your inventory size
c_smallBag = Container('A Small Bag', 'A really small bag', 5, 150)
c_largerBag = Container('A Larger Bag', 'Somehow holds more items than you would have expected', 15, 450)
c_woodenBox = Container('A Wooden Box', 'It\'s really heavy to carry around!', 20, 550)
c_case = Container('A Traveler\'s Suitcase', 'You can carry it effortlessly by pulling it.', 30, 700)
containerls = [c_smallBag, c_largerBag, c_woodenBox, c_case]

allitem = hPotionls + mPotionls + weaponls + armorls + materialls + containerls
allitem.append(chestKey)


#The recipe for crafting items
recipe = {}
recipe['lists'] = [hPotion1, hPotion2, hPotion3, hPotion4, mPotion1, mPotion2, mPotion3, mPotion4, w_plasticDagger]
recipe[hPotion1.name] = {m_breathOfLife:1, m_bottle:1}
recipe[hPotion2.name] = {m_breathOfLife:2, m_bottle:1}
recipe[hPotion3.name] = {m_breathOfLife:3, m_bottle:1, m_pileOfEarth:2}
recipe[hPotion4.name] = {m_breathOfLife:3, m_bottle:1, m_pileOfEarth:1, m_hotChocolate:1}
recipe[mPotion1.name] = {m_rock:2, m_bottle:1}
recipe[mPotion2.name] = {m_rock:1, m_bottle:1, m_pileOfEarth:1}
recipe[mPotion3.name] = {m_rock:3, m_bottle:1, m_pileOfEarth:1}
recipe[mPotion4.name] = {m_rock:3, m_bottle:1, m_pileOfEarth:1, m_air:1}
recipe[w_plasticDagger.name] = {m_plastic:2, m_pileOfEarth:2, m_rock:1}

#generates the list monster can drop
common_material = [m_breathOfLife, m_pileOfEarth, m_pileOfEarth, m_pileOfEarth, m_bottle, m_rock, m_plastic, m_bottle, m_bottle, m_bottle]
common_weapon = [w_woodenStick, w_plasticDagger, w_woodenStick, w_plasticDagger, w_thinSword, w_woodenStick]
common_armor = [a_woodenShield, a_woolCloak, a_woodenShield, a_woolCloak, a_bandana, a_woodenShield]
common_container = [c_smallBag, c_largerBag, c_woodenBox, c_smallBag, c_smallBag, c_smallBag]
common_potion = [mPotion1, mPotion2, hPotion1, hPotion2, mPotion1, hPotion1, mPotion1, mPotion2, hPotion1, hPotion2, mPotion1, hPotion1, hPotion3, mPotion3]
rare = [w_macbethDagger, a_newClothes, m_hotChocolate, m_air, c_case, mPotion4, hPotion4]
monsterdropl = common_material + common_weapon + common_armor + common_container + common_material + common_potion + common_potion
random.seed()


#The part that enables the game to run with single keyboard commands
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
get = _GetchUnix()

#prints the map on terminal
def showmap(player):
    for line in player.level:
        print(line.rstrip('\r\n'))

#combat between player and monster
#the function returns a list of three elements, the first indicates the result: 0-the player wins, 1-the player loses, 2-the player flees
#the second and the third are experience and money the player earns correspondingly 
def combat(player, monster):

    #visual effects of attacking and being attacked
    def attackPrint(kind):
        if kind == 'm':
            a = list('@ 💥💥💥💥💥💥💥 $')
        if kind == 'a':
            a = list('@ 🔥🔥🔥🔥🔥🔥🔥 $')
        if kind == 'b':
            a = list('$ 🔥🔥🔥🔥🔥🔥🔥 @')
        for i in a:
            time.sleep(0.05)
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
        print()

    #main combat loop
    count = 0
    notFled = True
    expected_count = monster.health // player.nattack
    while player.notdead() and monster.notdead() and notFled:
        clear()
        print("Round:", count)
        player.status()
        monster.status()
        print()

        #get's the player's decision and the monster's for this round
        print("What do you want to do this round?")
        print('m: Use magic')
        print('a: Attack')
        print('d: Defend')
        print('p: Use Potion')
        print('f: Flee')
        p = get().lower()
        m = monster.decide(player, count)
        Already = True
        while p!='a' and p!='m' and p!='d' and p!='f' and p!='p':
            if Already:
                print('Not a valid command, try again')
                Already = False
            p = get().lower()

        #compares the two desicions
        clear()
        print("Round:", count)
        player.status()
        print()
        monster.status()
        print()
        if p == 'f':
            notFled = False
            print('You have fled from the combat.')
            print('Press c to continue')
            key = get().lower()
            if key == 'c':
                return [2,0,0]
        elif p == 'p':
            player.usepotion()
            if m == 'a':
                attackPrint('a')
                player.health -= monster.attack
            else:
                print('The monster decided to defend itself. Nothing happends.')
                time.sleep(1)
        elif p == 'a':
            if m == 'a':
                attackPrint('a')
                attackPrint('b')
                monster.health -= player.nattack
                player.health -= monster.attack
            else:
                attackPrint('a')
                monster.health -= player.nattack
        elif p == 'd':
            if m == 'd':
                print('Both you and your opponent decided to defend themselves. Nothing happened this round.')
                time.sleep(1)
            else:
                attackPrint('b')
                player.health -= int(monster.attack / player.ndefense + 0.5)
        elif p == 'm':
            if player.magic == 0:
                print('You don\'t have magic for this.')
                time.sleep(1)
            elif m == 'a':
                attackPrint('m')
                attackPrint('b')
                monster.health -= int(player.nattack * 1.5)
                player.health -= monster.attack
                player.magic -= 1
            else:
                attackPrint('m')
                monster.health -= int(player.nattack / monster.defense + 0.5)
                player.magic -= 1

        count += 1

    #calculates the reward for this combat
    if notFled and player.notdead():
        exp = 30 + int(expected_count / count * 5)
        money = 5 + int(expected_count / count * 2)
        return [0, exp, money]
    else:
        exp = 15 + int(expected_count / count * 3)
        money = 2 + int(expected_count / count)
        return [1, exp, money]


#generates the monster of this level
#the number of monsters in each level is fixed, and the monster's strength is slightly lower than the player's
#the monsters are random by their name, type, and drop list
def generateMonster(player):
    monsterls = []
    r = []
    for i in range(player.levelnum * 3 + 5):
        r += random.choice(['a', 'd', 'c'])
    for item in r:
        name = str(int(random.random() * 1000))
        drop = [random.choice(monsterdropl), random.choice(monsterdropl), random.choice(monsterdropl), random.choice(monsterdropl)]
        if item == 'a':
            monsterls.append(AggresiveMonster(name, int(player.health * random.uniform(0.6,1.0)), int(player.nattack * random.uniform(0.6,1.0)), int(player.ndefense * random.uniform(0.6,1.0)), [random.choice(drop), random.choice(drop)]))
        elif item == 'd':
            monsterls.append(DefensiveMonster(name, int(player.health * random.uniform(0.6,1.0)), int(player.nattack * random.uniform(0.6,1.0)), int(player.ndefense * random.uniform(0.6,1.0)), [random.choice(drop)]))
        else:
            choices = []
            for i in range(random.randint(8,15)):
                choices += random.choice(['a', 'd'])
            monsterls.append(CleverMonster(name, int(player.health * random.uniform(0.6,1.0)), int(player.nattack * random.uniform(0.6,1.0)), int(player.ndefense * random.uniform(0.6,1.0)), [random.choice(drop), random.choice(drop)], choices))
    if random.random() < 0.05:
        Felix = random.choice(monsterls)
        Felix.dropls.append(random.choice(rare))
    random.choice(monsterls).dropls.append(chestKey)
    random.shuffle(monsterls)
    return monsterls

#generates a random list of when the monster will appear
def generateMonsterls(monsterls):
    monsterappear = []
    for i in range(len(monsterls)):
        monsterappear.append(random.randint(5,28))
    return monsterappear

#generates a boss with random name and drop list, its strength is about, or slightly higher than the player's
def generateBoss(player):
    choices = []
    name = '~~^' + str(int(random.random() * 10000000)) + '^~~'
    drop = [random.choice(monsterdropl), random.choice(monsterdropl), random.choice(monsterdropl), random.choice(rare)]
    for i in range(random.randint(8,15)):
        choices += random.choice(['a', 'd'])
    
    a = 0
    for i in choices:
        if i == 'd':
            a += 1
    if a > len(choices) // 3:
        for i in choices:
            p = random.random()
            if i == 'd' and p <= 0.5:
                i = 'a'

    Boss = CleverMonster(name, int(player.health * random.uniform(1.8,2.2)), int(player.nattack * random.uniform(1.8,2.2)), int(player.ndefense * random.uniform(1.8,2.2)), [random.choice(drop), random.choice(drop)], choices)
    Boss.dropls.append(doorKey)
    return Boss

#generates the drop list of chest chest in each level
def generateChest():
    itemls = []
    for i in range(random.randint(1,3)):
        itemls.append(random.choice(common_material))
        itemls.append(random.choice(common_container))
        itemls.append(random.choice(common_armor))
        itemls.append(random.choice(common_weapon))
        while len(itemls) > 1:
            random.shuffle(itemls)
            itemls.remove(itemls[0])
    if random.random() < 0.05:
        itemls.append(random.choice(rare))
    if random.random() < 0.3:
        random.shuffle(itemls)
        itemls.remove(itemls[0])
    return itemls



"""---------------------------------------------------------------------------------------"""
#This starts the game
hero = '@'
boss = '%'
merchant = '$'
door = '!'
chest = '&'

#initialzes player
player = Player()
player.recipe = recipe
player.additem(hPotion1)
player.additem(hPotion1)
player.additem(hPotion2)
player.additem(hPotion2)


#initialze monster, boss, and chest of level 1
monsterls = generateMonster(player)
monsterappear = generateMonsterls(monsterls)
Boss = generateBoss(player)
ch = Chest(generateChest())


#Some introduction of the game
playing = False
clear()
print()
entered = False
first = True
while first:
    clear()
    print("   You decided suddenly one day that you should follow the journey of all warriors.")
    time.sleep(0.6)
    print("   So you packed things that you need and entered the tower, in search for wealth and fame.")
    time.sleep(0.6)
    print("   Your goal is to defeat the boss of each level, get the door key from them, and move on.")
    time.sleep(0.6)
    print()
    print("Press c to continue.")
    command = get()
    if command != 'c':
        print("Press c to continue.")
    else:
        entered = True
        first = False
done = False
while entered:
    clear()
    print("   While you were walking aimlessly in the tower, someone called you by your name.")
    time.sleep(0.6)
    print("   This was strange, given that you hadn't had the chance to speak out your name in pride.")
    time.sleep(0.6)
    print("   You turned and moved towards the voice.")
    time.sleep(0.6)
    print("   'Hello, it's so nice to speak to people!' You saw a person sitting on the ground and leaning against the wall. There was a large bag next to this person.")
    time.sleep(0.6)
    print("   'I've seen people come all the time, but none of them succeeded. They told me that the tower is too high to climb. I am the merchant and aims to help you throughout your climb to the top of tower.'")
    time.sleep(0.6)
    print("   'Anyway, you can PRESS X TO LEAVE while you're seeing THE MAP.'")
    time.sleep(0.6)
    print("   'A useful tip: There are invisible monsters wandering here as well. You can earn money and level yourself up by not fleeing.'")
    time.sleep(0.6)
    print("   'Okay, I won't keep you long in this conversation. If you are determined enough to continue, I shall meet you again!'")
    time.sleep(0.6)
    print("   The merchant waved his hands at you. You nodded.")
    time.sleep(0.6)
    print()
    print("Press C to continue.")
    command = get()
    if command != 'c':
        print("Press C to continue.")
    else:
        done = True
        entered = False
while done:
    clear()
    print("Help:  This will NOT appear again.")
    print("     Make sure the caps lock is NOT on.")
    print("     Use 'w', 'a', 's', and 'd' to move upwards, leftwards, downwards, and rightwards.")
    print("     Use 'i' to check your inventory.")
    print("     '$': Merchant, from whom you can buy and sell items")
    print("     '&': Chest, can be opend with a chest key")
    print("     '%': Boss, defeat it to move on to next level")
    print("     And You will find other tips during the game.")
    print()
    print("Press C to continue.")
    command = get()
    if command != 'c':
        print("Press C to continue.")
    else:
        playing = True
        done = False

#the map shows from here
#step keeps track of how many steps the player has moved since last encouter with the monster
step = 0
while playing and player.notdead():
    timePass = False
    clear()
    print("Level:" + str(player.levelnum))
    player.status()
    showmap(player)

    #determines if the player can regenerate
    if step % 3 == 0:
        player.regeneration()

    #tells the player what they can do if they are around boss, merchant, door, or chest
    if player.around(boss):
        print('Boss: '+random.choice(baroundwords))
        print()
        print('Press y to FIGHT!!')
    elif player.around(merchant):
        print('Merchant: ' + random.choice(merchantwords))
        print()
        print('Press y to talk with Merchant.')
    elif player.around(door):
        print()
        if doorKey in player.inventory:
            print('Press y to Next Level or n to Stay')
        else:
            print('You Need to Defeat the Boss for Key')
    elif player.around(chest):
        print()
        if chestKey in player.inventory:
            print('Press y to open chest')
        else:
            print('You don\'t have the chest key.')

    #what the game would do when monster appears
    #The monster removes itself from monsterls once it is encountered
    if len(monsterls) and step == monsterappear[0]:
        if player.health < player.maxhealth * 0.2:
            u = 0
        else:
            print("You Are Attacked by a Monster!")
            time.sleep(1)
            step = 0
            result = combat(player, monsterls[0])
            if result[0] == 2:
                print('You fled, how shameful.')
                time.sleep(1)
                monsterls.remove(monsterls[0])
                monsterappear.remove(monsterappear[0])
            elif result[0] == 1:
                player.addexp(result[1])
                player.money += result[2]
                monsterls.remove(monsterls[0])
                monsterappear.remove(monsterappear[0])
                print('You lost the combat.')
                print('You gained: ' + str(result[1]) + " exp and " + str(result[2]) + " money.")
                player.health = int(0.1 * player.maxhealth)
                time.sleep(1)
            else:
                player.addexp(result[1])
                player.money += result[2]
                print('You won!')
                print('You gained: ' + str(result[1]) + " exp and " + str(result[2]) + " money.")
                time.sleep(1)
                player.monsterdrop(monsterls[0].dropls)
                monsterls.remove(monsterls[0])
                monsterappear.remove(monsterappear[0])
    
    #what the player can do if they are not encountered by a monster
    else:
        command = get().lower()
        if command == 'w':
            player.move('w')
        elif command == 'a':
            player.move('a')
        elif command == 's':
            player.move('s')
        elif command == 'd':
            player.move('d')
        elif command == 'i':
            if len(player.inventory) == 0:
                print('You have nothing in inventory.')
                time.sleep(1)
            else:
                player.inspect()
        elif command == 'x':
            print('Do you want to quit? Press Y to quit or N to stay')
            command = get()
            if command == 'y':
                playing = False
        elif command == 'y'and player.around(boss):
            result = combat(player, Boss)
            if result[0] == 2:
                print('You fled, how shameful.')
                time.sleep(1)
            elif result[0] == 1:
                player.addexp(result[1])
                player.money += result[2]
                print('You lost the combat.')
                print('You gained: ' + str(result[1]) + " exp and " + str(result[2]) + " money.")
                player.health = int(0.1 * player.maxhealth)
                time.sleep(1)
            else:
                player.addexp(int(result[1] * 1.5))
                player.money += result[2]
                print('You won!')
                print('You gained: ' + str(result[1]) + " exp and " + str(result[2]) + " money.")
                time.sleep(1)
                player.monsterdrop(Boss.dropls)
                player.disappear(boss)
        elif player.around(merchant) and command == 'y':
            player.talkmerchant(allitem)
        elif command =='y' and player.around(door):
            if doorKey in player.inventory:
                player.moveToNext()
                player.status()
                player.drop(doorKey)
                monsterls = generateMonster(player)
                monsterappear = generateMonsterls(monsterls)
                Boss = generateBoss(player)
                ch = Chest(generateChest())
            else:
                print("You don't have the key, defeat the boss to get one.")
                time.sleep(1)
        elif command == 'n' and player.around(door):
            if doorKey in player.inventory:
                print("Why not move up?")
            else:
                print("You don't have the key anyway, defeat the boss to get one.")
            time.sleep(1)
        elif command == 'y' and player.around(chest):
            if chestKey in player.inventory:
                player.chestopen(ch)
            else:
                print("You don't have the key, fight all monsters in this level to get one or buy from the merchant.")
                time.sleep(1)
        else:
            print('Not a valid command')
            time.sleep(0.952)
    if timePass == True:
        updater.updateAll()
    step += 1

