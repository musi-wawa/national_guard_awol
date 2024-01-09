import random

def main():
    print("Random name:")
    fullName = ""
    firstNames = open("data/first-names.txt")
    lastNames = open("data/last-names.txt")
    
    firstNameLine = random.randint(1,1003) #total number of lines
    fullName+=firstNames.readlines()[firstNameLine]
    fullName = fullName.strip()
    fullName += " "

    lastNameLine = random.randint(1,199) #total number of lines
    fullName += lastNames.readlines()[lastNameLine]

    firstNames.close()
    lastNames.close()
    
    print(fullName)

def getRandomName():
    fullName = ""
    firstNames = open("data/first-names.txt")
    lastNames = open("data/last-names.txt")
    
    firstNameLine = random.randint(1,1003) #total number of lines
    fullName+=firstNames.readlines()[firstNameLine]
    fullName = fullName.strip()
    fullName += " "

    lastNameLine = random.randint(1,199) #total number of lines
    fullName += lastNames.readlines()[lastNameLine]

    firstNames.close()
    lastNames.close()
    
    return fullName

if __name__ == "__main__":
    main()