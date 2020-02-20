The game is made by: Roark Wu, Livia Xu

1. How we divide work between ourselves:

    We first discussed about what we need to do for the game, then splitted the work up. We send our work to each other back and forth during the past month to debug, add new improvements, and add features to existing improvements.
    
    Below is an attempt to find out who contributes which part of the game. In fact we improve each other's code and it's sometimes hard to attribute the exact parts of codes to a certain person.:

        Roark Wu: levels.txt; main.py: showMap, combat, main game loop, class GetchUnix; character.py: readmap, class Player: __init__, addexp, na, nd, move, getLocation, around, disappear, status, inspect, monsterdrop, chestopen, usepotion, additem, drop, buy, sell, regeneration, talkmerchant

        Livia Xu: monster.py; item.py; main.py: generateMonster, generateMonsterls, generateBoss, generateChest, combat, list of all items, recipe to craft, main game loop; character.py: class Player: __init__, moveToNext, notdead, na, nd, craft, talkmerchant


2. Improvements: 57 points

-"drop" command  1 point
    in character.py, Player.drop()
    The player can drop items from their inventory

-"me" command  2 points
    in character.py, Player.status()
    The player can see their status of themselves. It is shown before the map.

-Bigger World  2 points
    in levels.txt
    There are six different maps in total, but theoretically the player can play as long as they want.

-Inventory maximum size  2 points
    in player.py, Player.__init__()
    Items are initialized with a parameter size, and player's inventory has a maximum size. When the player has items whose total size is larger than the maximum size of inventory, they need to drop items to make space.

-"inspect" command  2 points
    in character.py, Player.inspect()
    The command allows the player to see what they have in their bag. It can be called by pressing 'i' during the game. While inspecting, the player can see the description of the items and choose to use, drop, or craft items.

-Weapons  2 points
    in item.py, class Weapon
    in character.py, Player.na()
    There is a weapon class and different weapons. The weapons increase the player's attack by differnt factors and have different sizes so that the player can choose among them.
    weaponls = [w_woodenStick, w_plasticDagger, w_thinSword, w_broadSword, w_toyKnife, w_macbethDagger]

-Armors  2 points
    in item.py, class Armor
    in character.py, Player.nd()
    There is an armor class and different armors. The armors increase the player's attack by different factors and have different sizes so that the player can choose among them.
    armorls = [a_woodenShield, a_chainmail,a_bandana, a_newClothes, a_woolCloak, a_fancyHelmet]

-Auto-generating monsters  2 points
    in main.py, generateMonster(), generateMonsterls()
    There is a monster list that will be generated when the player enters a new level. Then the time that monsters appear is determined by a list of random numbers. The game keeps track of how many times the player has moved since last encounter with the boss and when the number is equal to a number in the list, the player will encounter a monster.

-Victory conditions  2 points
    in main.py, combat()
    The combat ends when the player flees, or when either of the participants has health less than 0. The player can earn experience and money unless they have fled. The amount of experience and money decreases when the player spend too much time in the combat. Less rewards are given, though, if the player loses. The player can pick up items that the monster dropped if the player wins. The player gains nothing if they have fled. 

-Healing objects  2 points
    in item.py, class HealPotion and class MagicPotion
    in character.py, Player.usePotion()
    The heal potions restore health, and the magic potions restore magic. Different potions restore different amount of health / magic. When the amount that potion would restore exceeds the amount that the player needs to reach max health / magic, the potion would only restore to max health / magic.
    hPotionls = [hPotion1, hPotion2, hPotion3, hPotion4]
    mPotionls = [mPotion1, mPotion2, mPotion3, mPotion4]

-Locked chests  2 points
    in item.py, class Chest and class ChestKey
    in main.py, generateChest()
    There is a chest in each level which can only be opened once with the chest key. The key can be bought from the merchant, or can be picked from a randomly chosen monster if the player defeats it. Items in the chest is chosen randomly from allitem.

-Locked doors  2 points
    in item.py, class DoorKey
    in main.py, generateBoss()
    The player needs a door key to enter the next level. The door key is in the drop list of the boss of each level and can be used only once.

-Containers  2 points
    in item.py, class Container
    The container itself does not have size, but can increase the maximum size of inventory once used.
    containerls = [c_smallBag, c_largerBag, c_woodenBox, c_case]

-Stacking items  2 points
    in character.py, Player.inspect()
    There is a dictionary containing the items as key and the numbers of them in the inventory as value. The dictionary is created each time when the player wants to inspect their bag.

-Regeneration  2 points
    in character.py, Player.regenerate()
    The player regenerates health every three moves during the game.

-Loot  3 points
    in monster.py, class Monster
    in main.py, generateMonster()
    The monster has a drop list generated by randomly picking items from all items.

-More monsters  3 points
    in monster.py, class AggressiveMonster, class DefensiveMonster, class CleverMonster
    in main.py, generateMonster()
    The three types of monster differ by how they behave during combat. Aggresive monster attacks all the time, defensive rarely attacks, and clever chooses its behavior among a list. 

-Player attributes  3 points
    in character.py, class Player
    The player has attributes of health, magic (which, when used during combat, causes a higher harm and cannot be defended), attack (and attack after using weapon), defense (and defense after using armor), experience and level, and money.

-Command abbreviation  3 points
    in main.py, movecommand() and the main game loop
    in character.py, Player.talkmerchant(), Player.inspect(), Player.craft()
    All commands can be done by pressing a single key

-Currency  4 points
    in character.py, class Player (Player.buy(), Player.sell())
    in main.py, combat()
    When in a combat and the player have not fled, the player can gain money. The player can also sell items in their inventory to merchant to gain money. The player can buy items from merchant with money.

-Leveling up  4 points
    in character.py, Player.addexp()
    in main.py, combat()
    When in a combat and the player have not fled, the player can gain experience. The player then will level up if they have enough experience. When leveling up, the player will have increase in health, magic, attack, and defense.

-Crafting  4 points
    in character.py, Player.craft()
    in item.py, class Materials
    The player can use certain materials to craft useful items like potions and others. The player can craft items while they are inspecting. There is a dictionary called "recipe" that stores all items that can be crafted.
    materialls = [m_breathOfLife, m_pileOfEarth, m_bottle, m_rock, m_hotChocolate, m_air, m_plastic]
    recipe['lists'] = [hPotion1, hPotion2, hPotion3, hPotion4, mPotion1, mPotion2, mPotion3, mPotion4, w_plasticDagger]

-Characters  4 points
    in character.py, Player.talkmerchant()
    The player can talk with the merchant.


3. Other improvements:

-Visual effects of moving on a map, choosing among items
    The map / list of items to be chosen is treated as a list of strings, which is then changed each time the player moves. Many thanks to the capability of computers, the terminal clears the screen and redraws the map / item list over and over again. If we want words to remain on the screen longer, we use time.sleep().
