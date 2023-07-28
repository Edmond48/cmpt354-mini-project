def printMenu():
    print("==================== Library Client ====================")
    print("1.Find an item")
    print("2.Borrow an item")
    print("3.Return an item")
    print("4.Donate an item")
    print("5.Find an event")
    print("6.Register for an event")
    print("7.Volunteer for the library")
    print("8.Ask for help from a librarian")
    print("9.Exit")

def main():
    isRunning = True
    while (isRunning):
        printMenu()
        userChoice = input("Please input the number of your option: ")

        print("========================================================")
        print("Exited")
        return

if __name__ == "__main__":
    main()