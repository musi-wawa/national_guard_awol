from names import getRandomName
from defines import *
import random

def combatTest():
    print("""
COMBAT TEST
---------------------------------""")
    print("PLAYER SQUAD SIZE:")
    squadHolder = []
    playerSquadSize = getTestSquadSize()
    squadHolder = generateTestSquad(squadHolder,playerSquadSize)
    playerSquad = Squad(squadHolder,"Player Squad")
    print("COMPUTER SQUAD SIZE:")
    squadHolder = []
    computerSquadSize = getTestSquadSize()
    squadHolder = generateTestSquad(squadHolder,computerSquadSize)
    computerSquad = Squad(squadHolder,"Computer Squad")
    distance = 10 #change as needed
    while True:
        battle(playerSquad,computerSquad,distance)      #start the fight!

def generateTestSquad(newSquad,newSquadSize):
    for _ in range(newSquadSize):
        newFighter = Fighter(getRandomName(),[1,0,0])
        newFighter.inventory.weapon = Item(1)
        newFighter.inventory.equipment = Item(3)
        newFighter.inventory.gear = Item(2,5)
        newFighter.inventory.uniform = Item(10)
        newSquad.append(newFighter)
    return(newSquad)

def getTestSquadSize():
    validNumber = False    
    squadSize = 0
    while validNumber != True:
        try:
            squadSize = int(input("Size of squad? (1-10) "))
            if squadSize > 0 and squadSize <= 10:
                validNumber = True
            else:
                raise()
        except:
            print("Invalid input. Please enter a number from 1-10.")
    return squadSize

def battle(playerSide,computerSide,distance):
    playerTurn = True
    while True:
        actionsLeft = 2
        clear()              #new player turn
        narrateScene(playerSide,computerSide,distance)
        showOptions(actionsLeft)
        while playerTurn == True:
            if actionsLeft == 0:
                playerTurn = False
            choice = input("\n   What do you do? ")
            match choice.lower():
                case "1" | "advance":
                    distance -= 1
                    actionsLeft -=1
                case "2" | "retreat":
                    distance += 1
            
"""             case 3 | "attack":
                case 4 | "gear":
                case 5 | "suppress":
                case 6 | "talk":
                case 7 | "examine":
                case 8 | "end" | "end turn": 
                    
def getFighters(squad):"""

def showOptions(actionsLeft):
    if actionsLeft == 1:
        print("It's your turn. You have 1 action left. Here are your options:")
    else:
        print("It's your turn. You have 2 actions left. Here are your options:")
    print("1. Advance")
    print("2. Retreat")
    print("3. Attack")
    print("4. Gear")
    print("5. Suppress")
    print("6. Talk")
    print("7. Examine")
    print("8. End turn")
    print("Remember that you can do 'help' to learn about any command.")

def narrateScene(yourSide,enemySide,distance):
    print(f"Your side has a size of {len(yourSide.members)} and the enemy has a size of {len(enemySide.members)}.")
    print(f"The enemy is {distance} tiles away from you")


if __name__ == "__main__":
    combatTest()