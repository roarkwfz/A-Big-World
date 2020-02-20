import random
class Monster:
    def __init__(self, name, attackType, health, attack, defense, drop):
        self.name = name
        self.attackType = attackType
        self.health = health
        self.maxhealth = health
        self.attack = attack
        self.defense = defense
        self.dropls = drop

    def notdead(self):
        return self.health > 0

    def status(self):
        print(self.name + ": " + self.attackType)
        print('Health: '+str(self.health)+' / '+str(self.maxhealth)+' '+'Attack: '+str(self.attack))

    def decide(self, opp, roundnum):
        if self.health <= self.maxhealth * 0.2:
            return 'd'
        else:
            return 'a'

class AggresiveMonster(Monster):
    def __init__(self, name, health, attack, defense, drop):
        Monster.__init__(self, name, 'aggresive', health, attack, defense, drop)
    
    def decide(self, opp, roundnum):
        return 'a'

class DefensiveMonster(Monster):
    def __init__(self, name, health, attack, defense, drop):
        Monster.__init__(self, name, 'defensive', health, attack, defense, drop)

    def decide(self, opp, roundnum):
        if roundnum % 4 == 0:
            return 'a'
        else:
            return 'd'

class CleverMonster(Monster):
    def __init__(self, name, health, attack, defense, drop, choices=['a', 'a', 'd', 'd', 'a', 'a']):
        Monster.__init__(self, name, 'clever', health, attack, defense, drop)
        self.choice = choices

    def decide(self, opp, roundnum):
        if self.health <= self.maxhealth * 0.1:
            return 'd'
        elif opp.health <= opp.maxhealth * 0.2:
            return 'a'
        else:
            c = random.choice(self.choice)
            if c == 'd':
                if random.random() > 0.5:
                    c = 'a'
            return c




#class Boss(Monster):