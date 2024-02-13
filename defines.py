import os
import random
import json

with open("data/items.json") as itemDataFile:
    itemData = json.load(itemDataFile)

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
        self.skills = skills #marksmanship,melee,communication,medical,repair,animal,cooking
        self.actions = 0
        self.discipline = 0
        self.morale = self.discipline + 3 #discipline directly impacts maximum morale
        self.health = 100
    
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

class Item:
    def __init__(self, id="0", stack=1):
        self.id = id
        self.stack = stack
        data = itemData.get(self.id, {})
        self.flavor = data.get("flavor", None)
        self.maxStack = data.get("maxStack", None)
        self.droppable = data.get("droppable", None)
        self.stats = data.get("stats", None)
        self.slots = data.get("slots", None)

        if self.maxStack is not None and self.stack > self.maxStack:
            self.stack = self.maxStack  #corrects stack size if its higher than max size at init