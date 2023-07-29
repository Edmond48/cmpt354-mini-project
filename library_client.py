def printMenu():
    print("\n\n==================== Library Client ====================")
    print("1.Find an item")
    print("2.Borrow an item")
    print("3.Return an item")
    print("4.Donate an item")
    print("5.Find an event")
    print("6.Register for an event")
    print("7.Volunteer for the library")
    print("8.Ask for help from a librarian")
    print("9.Exit")

def findItem():
    return

def borrowItem():
    return

def returnItem():
    return

def donateItem():
    return

def findEvent():
    return

def registerEvent():
    return

def volunteer():
    return

def contactLibrarian():
    return

def main():
    isRunning = True
    while (isRunning):
        printMenu()
        userChoice = int(input("Please input the number of your option: "))
        if (userChoice == 1):
            findItem()
        elif (userChoice == 2):
            borrowItem()
        elif (userChoice == 3):
            returnItem()
        elif (userChoice == 4):
            donateItem()
        elif (userChoice == 5):
            findEvent()
        elif (userChoice == 6):
            registerEvent()
        elif (userChoice == 7):
            volunteer()
        elif (userChoice == 8):
            contactLibrarian()
        elif (userChoice == 9):
            isRunning = False
        else:
            print("Invalid choice.")
        print("========================================================")
    
    print("*** Exited Application ***")

if __name__ == "__main__":
    main()