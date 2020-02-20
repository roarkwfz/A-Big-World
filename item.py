import os, sys, time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, typename, name, description, size, price):
        self.type = typename
        self.name = name
        self.desc = description
        self.size = size
        self.price = price


class Container(Item):
    def __init__(self, name, description, sizeboost, price, size=0):
        Item.__init__(self, 'container', name, description, size, price)
        self.sizeboost = sizeboost
    def use(self, player):
        player.invmax += self.sizeboost
        player.drop(self)
    def describe(self):
        print('    This container increases inventory size by', str(self.sizeboost))

class Material(Item):
    def __init__(self, name, description, size, price):
        Item.__init__(self, 'material', name, description, size, price)
    def describe(self):
        pass
    def use(self):
        pass

class ChestKey(Item):
    def __init__(self, name="Key-Chest", description="opens locked chests", size=0.5):
        Item.__init__(self, "chestKey", name, description, size, price=1000)
    def describe(self):
        print('    This item can open chest')

class Chest(Item):
    def __init__(self, itemsls, name="Chest", description="a chest that may have items you want", size=0):
        Item.__init__(self, "chest", name, description, size, price=None)
        self.items = itemsls

class DoorKey(Item):
    def __init__(self, name="Key-Door", description="opens locked doors", size=0.5):
        Item.__init__(self, "doorKey", name, description, size, price=None)
    def describe(self):
        print("    THE KEY TO NEXT LEVEL")

class Weapon(Item):
    def __init__(self, name, description, size, atkboost, price):
        Item.__init__(self, "weapon", name, description, size, price)
        self.atkboost = atkboost
    def describe(self):
        print("    attack increase by", str(self.atkboost))
    def use(self, player):
        if player.weapon:
            w = player.weapon
            player.na()
            player.weapon = self
            player.drop(self)
            player.additem(w)
        else:
            player.weapon = self
            player.nd()
            player.drop(self)


class Armor(Item):
    def __init__(self, name, description, size, defboost, price):
        Item.__init__(self, "armor", name, description, size, price)
        self.defboost = defboost
    def describe(self):
        print("    defense increase by", str(self.defboost))
    def use(self, player):
        if player.armor:
            a = player.armor
            player.nd()
            player.armor = self
            player.drop(self)
            player.additem(a)
        else:
            player.armor = self
            player.nd()
            player.drop(self)

class healPotion(Item):
    def __init__(self, name, description, size, hpRestore, price):
        Item.__init__(self, "healPotion", name, description, size, price)
        self.hpRestore = hpRestore
    def describe(self):
        print("    This potion can restore health by", str(self.hpRestore))
    def use(self, player):
        if player.health<player.maxhealth:
            if player.health+self.hpRestore >= player.maxhealth:
                player.health = player.maxhealth
            else:
                player.health += self.hpRestore
            player.drop(self)
        else:
            print('    Sorry, U R Already In Max Health')
            time.sleep(1.5)

class magicPotion(Item):
    def __init__(self, name, description, size, magicRestore, price):
        Item.__init__(self, "magicPotion", name, description, size, price)
        self.magicRestore = magicRestore
    def describe(self):
        print("    This potion can restore magic by", str(self.magicRestore))
    def use(self, player):
        player.magic += self.magicRestore
        player.drop(self)









