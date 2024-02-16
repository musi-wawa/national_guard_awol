from names import getRandomName
from defines import *
import random

def generateTestSquad(newSquad,newSquadSize):
    for _ in range(newSquadSize):
        newFighter = Fighter(getRandomName(),[1,0,0])
        newFighter.weapon = Item(1)
        newFighter.equipment = Item(3)
        newFighter.gear = Item(2,5)
        newFighter.uniform = Item(10)
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

    while True:
        playerTurn = True
        actionsLeft = 2
                      #new player turn
        while playerTurn == True:
            clear()
            narrateScene(playerSide,computerSide,distance)
            showOptions(actionsLeft)
            if actionsLeft == 0:
                playerTurn = False
                continue 
            choice = input("\n   What do you do? ")
            match choice.lower():
                case "1" | "advance":
                    if distance > 0:
                        distance -= 1
                        actionsLeft -=1
                    else:
                        print("Cannot advance any more!")
                case "2" | "retreat":
                    distance += 1
                    actionsLeft -=1
                case "3" | "attack":
                    actionsLeft -=1
                    attack(distance,playerSide,computerSide)
                case "4" | "suppress":
                    actionsLeft -=1
                    attack(distance,playerSide,computerSide,True)
                case 5 | "equipment":
                    print("Equipment not added to the game yet. Sorry.")
                case "6" | "inventory":
                    viewInventoryCombat(playerSide)
                case "7" | "examine":
                    print()
                case "8" | "pass" | "pass turn":
                    actionsLeft -= 1

def attack(distance,attackingSide,defendingSide,suppression = False):
    if suppression == False:
        for fighter in attackingSide.members:
            if fighter.inventory.weapon.weapon["range"] <= distance and hasAmmo(fighter,attackingSide) == True:
                print("bang")

def hasAmmo(fighter,squad):
    ammoNeeded = fighter.inventory.weapon.ammo
    return True

def viewInventoryCombat(squad): #doing things would cost actions if we were tracking actions per fighter instead of per squad. for now, moving and viewing items costs nothing
    print()
    print(squad)
        

def showOptions(actionsLeft):
    if actionsLeft == 1:
        print("It's your turn. You have 1 action left. Here are your options:")
    else:
        print("It's your turn. You have 2 actions left. Here are your options:")
    print("1. Advance")
    print("2. Retreat")
    print("3. Attack")
    print("4. Suppress")
    print("5. Equipment")
    print("6. Inventory")
    print("7. Examine")
    print("8. Pass turn")
    print("Remember that you can do 'help' to learn about any command.")

def narrateScene(yourSide,enemySide,distance):
    print(f"Your side has a size of {len(yourSide.members)} and the enemy has a size of {len(enemySide.members)}.")
    print(f"The enemy is {distance} tiles away from you")
