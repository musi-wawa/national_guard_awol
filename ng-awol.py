from combatTest import *
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


if __name__ == "__main__":
    main()