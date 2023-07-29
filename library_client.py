import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

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
    print("========================================================")

def find_item():
    pass

def borrow_item(): 
    pass

def return_item():
    pass

def donate_item():
    pass

def find_event():
    pass

def register_event():
    pass

def volunteer():
    pass

def get_contact_information():
    query = "SELECT name, email FROM Personnel WHERE position = 'Librarian' "
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)



def main():
    isRunning = True
    while (isRunning):
        printMenu()
        userChoice = int(input("Please input the number of your option: "))
        print("========================================================")

        if (userChoice == 1):
            find_item()
        elif (userChoice == 2):
            borrow_item()
        elif (userChoice == 3):
            return_item()
        elif (userChoice == 4):
            donate_item()
        elif (userChoice == 5):
            find_event()
        elif (userChoice == 6):
            register_event()
        elif (userChoice == 7):
            volunteer()
        elif (userChoice == 8):
            get_contact_information()
        else:
            print("Exited")
            return

if __name__ == "__main__":
    main()