import sqlite3

# global variable
conn = sqlite3.connect('library.db')

def printMenu():
    print("\n==================== Library Client ====================")
    print("1.Find an item")
    print("2.Borrow an item")
    print("3.Return an item")
    print("4.Donate an item")
    print("5.Find an event")
    print("6.Register for an event")
    print("7.Volunteer for the library")
    print("8.Ask for help from a librarian")
    print("9.Exit")

def find_item():
    print("\n==================== Finding Items ====================")
    print("Please enter the following details of the item (can be left blank):")
    title = input("Title: ")
    author = input("Author:")
    year = input("Year: ")

    cursor = conn.cursor()
    query = "SELECT * FROM Entries "
    if(title or author or year):
        query += "WHERE "
        query += "title=:queryTitle " if title else "TRUE "
        query += "AND "
        query += "author=:queryAuthor " if author else "TRUE "
        query += "AND "
        query += "year=:queryYear" if year else "TRUE "

    cursor.execute(query, {"queryTitle":title, "queryAuthor":author, "queryYear":year})
    rows = cursor.fetchall()

    print("\n==================== Results ====================")
    if rows:
        for row in rows:
            print(row)
    else:
        print("\nNo item(s) found")
    
    input("\nPlease press Enter to continue")

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
    cursor = conn.cursor()

    query = "SELECT name, email FROM Personnel WHERE position = 'Librarian' "
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print("\nPlease contact our librarians from the following list:")
        for row in rows:
            print(" - " + row[0] + ": " + row[1])
    else:
        print("\nSorry. No librarian is available at the moment")
        
    input("\nPlease press Enter to continue")



def main():
    isRunning = True
    with conn:
        while (isRunning):
            printMenu()
            userChoice = int(input("Please input the number of your option: "))

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
                isRunning = False
        print("========================================================")
        print("Exited")

if __name__ == "__main__":
    main()