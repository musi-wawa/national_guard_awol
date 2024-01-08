import os
import random
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Squad:
    def __init__(self, members=None, name="Unnamed Squad"):
        if members is None:
            members = []
        self.name = name
        self.members = members

    def __str__(self):
        member_names = "".join([str(member.name) for member in self.members])
        return f"{self.name}:\n{member_names}"


class Fighter:
    def __init__(self, name = "John Doe", skills = [0,0,0]):
        self.name = name
        self.flavor = "A generic human being."
        self.weapon = Item(0)
        self.equipment = Item(-1)
        self.gear = Item(-1)
        self.headgear = Item(-1)
        self.storage = Item(-1)
        self.uniform = Item(-2)
        self.skills = skills
        self.actions = 0
        self.morale = 3      #number is a placeholder for combat test
        self.health = 4
    
    def __str__(self):
        return f"{self.name}, {self.flavor}"
    
    def attemptAction(self):                 #  dont use this until we have individual squad management. as long as everyone's being kept track of as a single moving blob, just keep track of turns per side.
        if self.actions == 0:                
            return 1 #"out of actions!"
        elif self.health == 1:
            return 2 #"unconscious!"
        elif self.morale < 0:
            if random.randint(1,5) == 1: #1/5 chance
                return 3 #"refuses to do what they were told!"
            self.actions -= 1
        else:
            self.actions -= 1

"""class Inventory:
    def __init__(self, weapon = None, equipment = None, gear = None, storage = None, uniform = None):
        if weapon == None:
            self.weapon = Item(0)       #if new inventory slots are empty, create item 0 AKA "empty" in that slot
        else: self.weapon = weapon
        if equipment== None:
            self.equipment = Item(-1)
        else: self.equipment = equipment
        if gear == None:
            self.gear = Item(-1)
        else: self.gear = gear
        if storage == None:
            self.storage = [Item(-1)]
        if uniform == None:
            self.uniform = Item(-2)"""

    """def __str__(self):
        return f"{self.weapon}, {self.equipment}, {self.gear}, {self.storage}"""
class Item:
    def __init__(self, id = 0, stack = 1):
        self.id = id
        self.stack = stack
        self.weapon = None
        self.maxStack = 1
        self.utility = None
        self.droppable = True
        match id:
            case -2:
                self.name = "nothing"
                self.droppable = False
                self.maxStack = 0
                self.flavor = "This person is not wearing any clothing whatsoever. Not that anyone cares about that sort of thing anymore."
                self.slots = ["uniform"]
            case -1:
                self.name = "empty"
                self.droppable = False
                self.maxStack = 0
                self.flavor = "This slot is empty. There's nothing here."
                self.slots = ["gear","equipment"]
            case 0:
                self.name = "unarmed"
                self.droppable = False
                self.flavor = "Hand to hand, fisticuffs, close quarters combat, martial arts, whatever you wanna call it. This person is entirely unarmed and is relying purely on their body for offense."
                self.maxStack = 0
                self.weapon = {"range":0,"damage":1,"cost":0,"suppress":0,"ammo":0,"bonus":-1}
                self.slots = ["weapon"] 
            case 1:
                self.name = "modern assault rifle"
                self.flavor = "A standard issue NG14 Assault Weapon, capable of holding 33 rounds of 7.79 HP in each external magazine. The magazine is loaded directly into the chamber so there is no 'plus one'. It is in a bullpup configuration and the magazines are quite bulky."
                self.weapon = {"range":4,"damage":3,"cost":2,"suppress":4,"ammo":4,"bonus":3}
                self.slots = ["weapon"]
            case 2:
                self.name = "modern marksman rifle"
                self.flavor = "The NG20 Reconaissance Weapon, A semi-automatic marksman rifle firing from a small side-fed magazine, integrated irons, and a 10x scope. Using 7.79 High Penetration in the reverse configuration, this weapon smashes through armor like it’s nothing but is ineffective against unarmored opponents. Prototypes for 12.79 HP variants exist, but never saw use due to the scarcity of armored targets to shoot at that need much firepower."
                self.weapon = {"range":6,"damage":2,"cost":1,"suppress":0,"ammo":4,"bonus":2}
                self.slots = ["weapon"]
            case 3:
                self.name = "modern machine gun"
                self.flavor = "A bullpup NG22 Suppression Weapon, holding an impressive 99 rounds. It is extremely bulky and has awful ergonomics, but more than makes up for it with its rate of fire and sheer power. It doesn’t look anything like machine guns of the past wars and the magazine is a horizontal brick above the trigger. Chambered in 7.79 HP."
                self.weapon = {"range":4,"damage":4,"cost":4,"suppress":8,"ammo":4,"bonus":4}
                self.slots = ["weapon"]
            case 4:
                self.name = "modern military rounds"
                self.flavor = "A handful of 7.79 High Penetration rounds. Being a caseless round, they are dull green and rectangular. For long-range use, you can flip them around and they remain effective. Impossible to hand-load."
                self.maxStack = 16
                self.slots = ["equipment"]
            case 5:
                self.name = "tactical armor"
            case 6:
                self.name = "national guard field uniform"
                self.flavor = "The standard issue field uniform for all National Guard troopers in Bastille. With a brodie helmet, red bandana and camouflauged fatigues, it's vaguely comfortable and fits pretty much no one. At least it's warm."
                self.maxStack = 5
                self.slots = ["uniform"]

        if self.stack > self.maxStack:
            self.stack = self.maxStack  #corrects stack size if its higher than max size at init