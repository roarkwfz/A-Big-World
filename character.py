import os, sys, time, item, monster
from math import sqrt, log




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

#the symbol represetations of characters and items in game
hero = '@'
boss = '%'
merchant = '$'
door = '!'
chest = '&'

#readmap method helps to read the level.txt file and show them and transfer strings to self.levelmap (a list of strings)
#readmap change strings in each line to a list and return a list of lines lists
def readmap(filename, levelnum):
    mapFile = open(filename, 'r')
    content = mapFile.readlines() + ['\r\n']
    mapFile.close()
    start = 0
    end = 0
    l = levelnum % 6 + 1

    for i in range(len(content)):
        line = content[i].rstrip('\r\n')
        if ';'+str(l) in line:
            start = i
        if start and line == '':
            end = i
            break
    levelMap = content[start+1:end]
    return levelMap


class Player:
    def __init__(self):
        self.levelnum = 1
        self.level = readmap('levels.txt', self.levelnum)
        self.maxhealth = 50
        self.health = 50
        self.maxmagic = 30
        self.magic = 10
        self.weapon = None
        self.armor = None
        self.attack = 5
        self.maxattack = 20
        self.nattack = 5
        self.defense = 5
        self.maxdefense = 20
        self.ndefense = 5
        self.inventory = []
        self.invsize = 0
        self.invmax = 20
        self.money = 30
        self.exp = 0
        self.expmax = 50
        self.getLocation()
        self.recipe = None
    
    #change map to next level
    def moveToNext(self):
        self.levelnum += 1
        self.level = readmap('levels.txt', self.levelnum)

    #adds experience to the player
    def addexp(self,n):
        if self.exp + n >= self.expmax:
            self.exp = self.expmax - self.exp
            self.expmax = int(self.expmax * 1.5 + 0.5)
            self.levelnum += 1
            self.attack = int(self.attack * 1.2)
            self.na()
            self.magic = int(self.magic * 1.2)
            self.defense = int(self.defense * 1.2)
            self.nd()
            self.health = int(self.health * 1.1)
            print("You have leveled up!")
            time.sleep(1)
        else:
            self.exp += n

    #calculate the attack of player with weapon
    def na(self):
        if self.weapon == None:
            self.nattack = self.attack
        else:
            self.nattack = int(self.attack * (1 + sqrt(self.weapon.atkboost)))
        if self.nattack > self.maxattack:
            self.nattack = self.maxattack

    #calculate the defense of player with armor
    def nd(self):
        if self.armor == None:
            self.ndefense = self.defense
        else:
            self.ndefense = int(self.defense * (1 + sqrt(self.armor.defboost)))
        if self.ndefense > self.maxdefense:
            self.ndefense = self.maxdefense

    #the order number of the character symber in the list returned by readmap is self.y 
    #and the number of the string in that list is self.x
    #we treats the position of every character as coordinates.
    def move(self, direction):
        self.getLocation()
        right = True
        if direction == 'w':
            y1 = self.y -1
            x1 = self.x
        elif direction == 's':
            y1 = self.y +1
            x1 = self.x
        elif direction == 'a':
            x1 = self.x -1 
            y1 = self.y
        elif direction == 'd':
            x1 = self.x +1
            y1 = self.y
        if y1 in range(len(self.level)):
            if x1 in range(len(self.level[y1])):
                if self.level[y1][x1]==' ':
                    self.level[y1] = self.level[y1][:x1]+hero+self.level[y1][x1+1:]
                    self.level[self.y] = self.level[self.y][:self.x]+' '+self.level[self.y][self.x+1:]
        self.getLocation()
    
    def notdead(self):
        return self.health>0

    #refresh the location of character
    def getLocation(self):
        for i in range(len(self.level)):
            line = self.level[i].rstrip('\r\n')
            if hero in line:
                self.x = line.index(hero)
                self.y = i
                break

    #using coordinate to check if the player is around any other things like chest or boss.
    def around(self, c):
        bx = None
        for i in range(len(self.level)):
            line = self.level[i].rstrip('\r\n')
            if c in line:
                bx = line.index(c)
                by = i
        if bx == None:
            return False
        if self.x + 1 == bx or self.x - 1 == bx or self.x == bx:
            if self.y + 1 == by or self.y - 1 == by or self.y == by:
                return True

    #after the chest is used or the boss beaten, the symbol in the map needs to disappear
    def disappear(self, c):
        for i in range(len(self.level)):
            line = self.level[i].rstrip('\r\n')
            if c in line:
                bx = line.index(c)
                by = i
        if bx == None:
            return False
        self.level[by] = self.level[by][:bx]+' '+self.level[by][bx+1:]

    #get the status of the player
    def status(self):
        print('Health: '+str(self.health)+'/'+str(self.maxhealth))
        print('Attack: '+str(self.nattack)+'/'+str(self.maxattack))
        print('Magic:  '+str(self.magic)+'/'+str(self.maxmagic))
        print('Armor:  '+str(self.ndefense)+'/'+str(self.maxdefense))
        print('INV:    '+str(self.invsize)+'/'+ str(self.invmax))
        print('Money:  '+str(self.money))
        print('LV:     '+str(self.levelnum)+'  '+str(self.exp)+'/'+str(self.expmax))
        print()

    #Helps the player to inspect its inventory
    #apnum number is the appointed item the player currently choose in its inventory
    def inspect(self):
        still = True
        apnum = 0
        while still:
            namelist = []
            for item in self.inventory:
                if item not in namelist:
                    namelist.append(item)
            limit = len(namelist)
            if apnum >= limit:
                apnum = 0
            elif apnum < 0:
                apnum = limit-1

            if limit == 0:
                print('You have nothing in inventory.')
                print()
                print("Press c to continue")
                command = get()
                if command == 'c':
                    still = False
                else:
                    print('Not a valid command, try again')
            else:
                clear()
                inv = {}
                for item in self.inventory:
                    if item in inv:
                        inv[item] += 1
                    else:
                        inv[item] = 1
                self.status()
                print()
                print("Now you have: ")
                for item in namelist:
                    if item == namelist[apnum]:
                        print('>   ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                    else:
                        print('    ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                print()
                print()
                print('    ' + namelist[apnum].desc)
                namelist[apnum].describe()
                print()
                print()
                print('Press d to drop, u to use, c to craft, or x to leave')
                print()
                command = get()
                if command == 'w':
                    apnum -=1
                elif command == 's':
                    apnum +=1
                elif command == 'c':
                    self.craft(self.recipe)
                elif command == 'd':
                    print('Press y to Drop this Item or n to Cancel')
                    command = get()
                    if command == 'y':
                        self.drop(namelist[apnum])
                    elif command == 'n':
                        still == True
                elif command == 'u':
                    print('Press y to Use this Item or n to Cancel')
                    command = get()
                    if command == 'y':
                        namelist[apnum].use(self)
                    elif command == 'n':
                        still == True
                elif  command == 'x':
                    print('Press Y to Leave or N to Stay')
                    command = get()
                    if command == 'y':
                        still = False
                    elif command == 'n':
                        still == True
                else:
                    print('Not a valid Command, try again')

    #Similar to inspect, but shows the items monster drops and allows the player to pick up these items
    def monsterdrop(self, droplist):
        still = True
        apnum = 0
        while still:
            namelist = []
            for item in droplist:
                if item not in namelist:
                    namelist.append(item)
            limit = len(namelist)
            if apnum >= limit:
                apnum = 0
            elif apnum < 0:
                apnum = limit-1

            if limit == 0:
                clear()
                self.status()
                print()
                print('There is Nothing Else.')
                time.sleep(1)
                still = False
            else:
                clear()
                inv = {}
                for item in droplist:
                    if item in inv:
                        inv[item] += 1
                    else:
                        inv[item] = 1
                clear()
                self.status()
                print()
                print("Monster Drops: ")
                for item in namelist:
                    if item == namelist[apnum]:
                        print('>   ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                    else:
                        print('    ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                print()
                print()
                print()
                print('    ' + namelist[apnum].desc)
                namelist[apnum].describe()
                print()
                print()
                print('Press P to Pick, I to Check Inventory, or X to leave')
                print()
                command = get()
                if command == 'w':
                    apnum -=1
                elif command =='i':
                    self.inspect()
                elif command == 's':
                    apnum +=1
                elif command == 'p':
                    print('Press Y to Take this Item or N to Cancel')
                    command = get()
                    if command == 'y':
                        self.additem(namelist[apnum])
                        droplist.remove(namelist[apnum])
                    elif command == 'n':
                        still == True
                elif  command == 'x':
                    print('Press Y to Leave or N to Stay')
                    command = get()
                    if command == 'y':
                        still = False
                    elif command == 'n':
                        still == True

    #Similar to inspect. allows the player to pick up the items in chest
    def chestopen(self, chest):
        still = True
        apnum = 0
        while still:
            namelist = []
            for item in chest.items:
                if item not in namelist:
                    namelist.append(item)
            limit = len(namelist)
            if apnum >= limit:
                apnum = 0
            elif apnum < 0:
                apnum = limit-1

            if limit == 0:
                clear()
                self.status()
                print()
                print('There is Nothing Else.')
                time.sleep(2)
                still = False
            else:
                clear()
                inv = {}
                for item in chest.items:
                    if item in inv:
                        inv[item] += 1
                    else:
                        inv[item] = 1
                clear()
                self.status()
                print()
                print("Chest Has: ")
                for item in namelist:
                    if item == namelist[apnum]:
                        print('>   ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                    else:
                        print('    ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                print()
                print()
                print()
                print('    ' + namelist[apnum].desc)
                namelist[apnum].describe()
                print()
                print()
                print('Press P to Pick, I to inspect inventory, or X to Leave.')
                print()
                command = get()
                if command == 'w':
                    apnum -=1
                elif command =='i':
                    self.inspect()
                elif command == 's':
                    apnum +=1
                elif command == 'p':
                    print('Press Y to Take This Item or N to Cancel')
                    command = get()
                    if command == 'y':
                        self.additem(namelist[apnum])
                        chest.items.remove(namelist[apnum])
                    elif command == 'n':
                        still == True
                elif  command == 'x':
                    print('Press Y to Leave or N to Stay')
                    command = get()
                    if command == 'y':
                        still = False
                        self.disappear('&')
                    elif command == 'n':
                        still == True
                if not len(chest.items):
                    self.disappear('&')

    #Similar to inspect, but it's only used when using potions during combat
    def usepotion(self):
        still = True
        apnum = 0
        while still:
            namelist = []
            for item in self.inventory:
                if item.type == "healPotion" or item.type == "magicPotion":
                    if item not in namelist:
                        namelist.append(item)
            limit = len(namelist)
            if apnum >= limit:
                apnum = 0
            elif apnum < 0:
                apnum = limit-1

            if limit == 0:
                print('You have nothing in inventory.')
                still = False
            else:
                clear()
                inv = {}
                for item in self.inventory:
                    if item in inv:
                        inv[item] += 1
                    else:
                        inv[item] = 1
                clear()
                self.status()
                print()
                print("'You can use the following items in your bag:'")
                for item in namelist:
                    if item == namelist[apnum]:
                        print('>   ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                    else:
                        print('    ' + str(inv[item]) + "x " + str(item.name)+ ' s'+str(item.size))
                print()
                print()
                print('    ' + namelist[apnum].desc)
                namelist[apnum].describe()
                print()
                print()
                print('Press U to Use, X to Leave')
                print()
                command = get()
                if command == 'w':
                    apnum -=1
                elif command == 's':
                    apnum +=1
                elif command == 'u':
                    print('Press Y to Use this Item or N to Cancel')
                    command = get()
                    if command == 'y':
                        namelist[apnum].use(self)
                    elif command == 'n':
                        still == True
                elif  command == 'x':
                    print('Press Y to Leave or N to Stay')
                    command = get()
                    if command == 'y':
                        still = False
                    elif command == 'n':
                        still == True
    
    def additem(self, item):
        if self.invsize + item.size <= self.invmax:
            self.inventory.append(item)
            self.invsize +=item.size
        else:
            print('You don not have enough space in your inventory')

    def drop(self, item):
        self.inventory.remove(item)
        self.invsize -= item.size
    
    def buy(self, allitem):
        still = True
        apnum = 0
        warn = 0
        while still:
            limit = len(allitem)
            if apnum >= limit:
                apnum = 0
            elif apnum < 0:
                apnum = limit-1
            print('You have: ' + str(self.money))
            print()
            print("You Can Buy: ")
            for item in allitem:
                if len(str(item.price)) == 1:
                    sp = '   '
                else:
                    sp = '  '
                if item == allitem[apnum]:
                    print('>   $' + str(item.price) + sp + str(item.name))
                else:
                    print('    $' + str(item.price) + sp + str(item.name))
            print('    ' + allitem[apnum].desc)
            allitem[apnum].describe()
            print()
            print()
            print('Press B to buy or X to leave')
            if warn == 1:
                print('You Don\'t Have enough Money')
            elif warn ==2:
                print('Your Inventory Doesn\'t have enough Space')
            warn = 0
            command = get()
            if command == 'w':
                apnum -=1
            elif command == 's':
                apnum +=1
            elif command == 'b':
                print('Press Y to Buy this Item or N to Cancel')
                command = get()
                if command == 'y':
                    if self.money >= allitem[apnum].price:
                        if self.invsize + allitem[apnum].size <= self.invmax:
                            self.inventory.append(allitem[apnum])
                            self.invsize += allitem[apnum].size
                            self.money -= allitem[apnum].price
                        else:
                            warn = 2
                    else:
                        warn = 1
                elif command == 'n':
                    still == True
            elif  command == 'x':
                print('Press Y to Leave or N to Stay')
                command = get()
                if command == 'y':
                    still = False
                elif command == 'n':
                    still == True

    def sell(self):
        still = True
        apnum = 0
        while still:
            namelist = []
            for item in self.inventory:
                if item not in namelist:
                    namelist.append(item)
            limit = len(namelist)
            if apnum >= limit:
                apnum = 0
            elif apnum < 0:
                apnum = limit-1

            if limit == 0:
                print('You have nothing to sell.')
                still = False
            else:
                clear()
                inv = {}
                for item in self.inventory:
                    if item in inv:
                        inv[item] += 1
                    else:
                        inv[item] = 1
                clear()
                self.status()
                print()
                print("Now you have: ")
                for item in namelist:
                    if item == namelist[apnum]:
                        print('>   ' + str(inv[item]) + "x " + str(item.name))
                    else:
                        print('    ' + str(inv[item]) + "x " + str(item.name))
                print()
                print('    ' + namelist[apnum].desc)
                namelist[apnum].describe()
                command = get()
                if command == 'w':
                    apnum -=1
                elif command == 's':
                    apnum +=1
                elif command == 't':
                    print('Press y to sell this Item or n to Cancel. Press x to leave')
                    command = get()
                    if command == 'y':
                        self.removeitem(namelist[apnum])
                        self.money += int(namelist[apnum].price * 0.5)
                    elif command == 'n':
                        still == True
                elif  command == 'x':
                    print('Press y to Leave or n to Stay')
                    command = get()
                    if command == 'y':
                        still = False
                    elif command == 'n':
                        still == True

    #according the number of player moving to regenerate health
    def regeneration(self):
        if self.health<self.maxhealth:
                if self.health+1 >= self.maxhealth:
                    self.health = self.maxhealth
                else:
                    self.health += 1

    #It's for the player to craft useful items from materials
    def craft(self, recipe):
        #help to check possible items to make
        def select(inv, recipe):
            m = {}
            for item in inv:
                if item.type == 'material':
                    if item in m:
                        m[item] += 1
                    else:
                        m[item] = 1
            possible = []
            for product in recipe:
                make = True
                for ingredient in recipe[product]:
                    if not ingredient in m:
                        make = False
                    else:
                        if recipe[product][ingredient] > m[ingredient]:
                            make = False
                if make:
                    possible.append(product)
            return possible

        def shift(possible, ls):
            i=0
            while i < len(possible):
                for item in ls:
                    if possible[i] == item.name:
                        possible[i] = item
                i+=1
            return possible

        still = True
        apnum = 0
        while still:
            possible = select(self.inventory,recipe)
            possible = shift(possible, recipe['lists'])
            limit = len(possible)
            if apnum >= limit:
                apnum = 0
            elif apnum < 0:
                apnum = limit - 1
            if limit == 0:
                print('You can make nothing from what you have.')
                time.sleep(2)
                still = False
            else:
                clear()
                print()
                print("You can make: ")
                for item in possible:
                    if item == possible[apnum]:
                        print('>   ' + item.name)

                    else:
                        print('    ' + item.name)
                print()
                print()
                print('    ' + possible[apnum].desc)
                possible[apnum].describe()
                print()
                print()
                print('Press c to craft or x to leave')
                print()
                command = get()
                if command == 'w':
                    apnum -=1
                elif command == 's':
                    apnum +=1
                elif command == 'c':
                    print('Press y to Craft this Item or n to Cancel')
                    command = get()
                    if command == 'y':
                        ingredients = recipe[possible[apnum].name]
                        for item in ingredients:
                            while ingredients[item] > 0:
                                self.drop(item)
                                ingredients[item] -= 1
                        self.additem(possible[apnum])
                        possible.remove(possible[apnum])
                        print("Craft success!")
                        time.sleep(0.8)
                    else:
                        still = True
                elif command == 'x':
                    print('Press y to Leave or n to Stay')
                    command = get()
                    if command == 'y':
                        still = False
                    elif command == 'n':
                        still == True
                        
    #it's a talking system when you are around the merchant
    #it feels like real life
    def talkmerchant(self, allitem):
        boo = ["1. I want to buy something", "2. I want to sell things to get money", "3. Let's talk.", "4. I want to leave."]
        apnum = 0
        still = True

        def talk(self):
            apnum = 0
            still = True
            choices = ["1. Why I keep seeing you here?", "2. How can you move between levels?", "3. Who am I?", "4. Why I don't need to eat here?", "5. I want to leave"]
            while still:
                clear()
                print("'Sure, what do you want to talk about? I'm only a merchant who happens to be here. I like to talk to people.' The merchant smiled at you.")
                print()
                print()
                print("What do you want to say?")
                print("Press c to choose")
                print()
                if apnum == len(choices):
                    apnum = 0
                elif apnum < 0:
                    apnum = 1
                for item in choices:
                    if item == choices[apnum]:
                        print('>   ' + item)
                        x = item
                        number = int(item[0:1])
                    else:
                        print('    ' + item)
                print()
                print()
                command = get()
                if command == 'w':
                    apnum -=1
                elif command == 's':
                    apnum +=1
                elif command == 'c':
                    if number == 1:
                        print("'I'm part of the tower. I exist when the tower exists.'")
                        time.sleep(1.5)
                        choices.remove(x)
                    elif number == 2:
                        print("'The merchant has everything, you know.'")
                        time.sleep(1.5)
                        choices.remove(x)
                    elif number == 3:
                        print("'24601.' The merchant pointed to your striped shirt. Interesting, you never realized this.")
                        time.sleep(1.5)
                        choices.remove(x)
                    elif number == 4:
                        print("'This is simple magic.'")
                        time.sleep(1.5)
                        choices.remove(x)
                    else:
                        print("'Okay, see you around.' The merchant said this to you, waved and returned to the sleep.")
                        print()
                        time.sleep(1)
                        still = False

        while still:
            clear()
            print("The merchant was lying on the ground, yawning. Seeing you approaching, the merchant smiled.")
            print("'Ah it's you again! Still not giving up? I have some items for you. Do you want to BUY any? Or you prefer to SELL some of your things to me?'")
            print()
            print()
            print("What do you want to say?")
            print("Press c to choose")
            print()
            if apnum == len(boo):
                apnum = 0
            elif apnum < 0:
                apnum = 1
            for item in boo:
                if item == boo[apnum]:
                    print('>   ' + item)
                    number = int(item[0:1])
                else:
                    print('    ' + item)
            print()
            print()
            command = get()
            if command == 'w':
                apnum -=1
            elif command == 's':
                apnum +=1
            elif command == 'c':
                if number == 1:
                    clear()
                    self.buy(allitem)
                    still = False
                elif number == 2:
                    clear()
                    self.sell()
                    still = False
                elif number == 3:
                    talk(self)
                    still = False
                else:
                    print("'Okay, see you around.' The merchant said this to you, waved and returned to the sleep.")
                    time.sleep(1)
                    print()
                    still = False

