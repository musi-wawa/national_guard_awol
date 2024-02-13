from combat import *
import sys

def main():
    choice = ""
    while choice != "exit" and choice != "4":
        printMainMenu()
        choice = str(input("    "))
        choice = choice.lower()
        clear()
        if choice == "1" or choice == "new game" or choice == "new":
            print("Under contruction!")
        elif choice == "2" or choice == "load game" or choice == "load":
            print("Under contruction!")
        elif choice == "3" or choice == "combat test" or choice == "combat":
            combatTest()
        else:
            print("Invalid option.")
    print("Thanks for playing!")
    sys.exit()

def printMainMenu():
    print("""National Guard: AWOL
    Created by Avery and Niah
          
---------------------------------

    1: New Game
    2: Load game
    3: Combat Test (debug)
    4: Exit
""")

def combatTest():
    clear()
    print("""COMBAT TEST
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

if __name__ == "__main__":
    main()