import sqlite3
import datetime

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
    print("\n==================== Borrow Item ====================")
    entryID = input("Please input the entry ID (the first field in \"Find an Item\" results): ")
    findCursor = conn.cursor()

    # check availability of items
    availabilityQuery = "SELECT * FROM Items WHERE entryID=:id AND status=:isAvailable"
    findCursor.execute(availabilityQuery, {"id":entryID, "isAvailable":"AVAILABLE"})
    row = findCursor.fetchone()

    if row:
        # set up data to insert
        itemID = row[0]
        print("Borrowing item with\n\tEntry ID: " + str(entryID) + "\n\tItem ID: " + str(itemID) + "\nPlease note down your Item ID for return")
        libraryID = input("Please input your library ID number: ")
        currentTime = datetime.date.today()
        returnTime = currentTime + datetime.timedelta(days=14)

        # insert
        insertCursor = conn.cursor()
        borrow = "INSERT INTO Borrow(itemID, libraryID, borrowDate, returnDate, returned, outstandingFee) "
        values = "VALUES (:iid, :lid, :bdate, :rdate, :returned, :fee)"
        insertQuery = borrow + values
        try:
            insertCursor.execute(insertQuery, {"iid":itemID, "lid":libraryID, "bdate":currentTime.strftime('%Y-%m-%d'), "rdate":returnTime.strftime('%Y-%m-%d'), "returned":"No", "fee":0})
        except sqlite3.IntegrityError:
            print("ERROR: Some information provided was wrong!\n")
        if conn:
            conn.commit()
        print("\nBorrow successful. Happy reading!")
    else:
        print("\n** That item is not currenly available **")
    
    input("\nPlease press Enter to continue")


def return_item():
    print("\n==================== Return Item ====================")
    print("Please input the following information:")
    libraryID = input("Your library ID: ")
    itemID = input("Item ID (not Entry ID): ")

    findCursor = conn.cursor()
    findQuery = "SELECT borrowID, returnDate FROM Borrow WHERE libraryID=:lid AND itemID=:iid AND returned=:r"
    findCursor.execute(findQuery, {"lid":libraryID, "iid":itemID, "r":"No"})
    rows = findCursor.fetchall()
    
    if (len(rows) == 0):
        print("No such record of a borrow")
        input("\nPlease press Enter to continue")
        return
    elif (len(rows) > 1):
        print("\n*** Concurrent borrows of one item. Please inform library staffs ***\n")
    
    borrowID = rows[0][0]
    returnDateStr = rows[0][1]
    returnDate = datetime.datetime.strptime(returnDateStr, '%Y-%m-%d')
    # fine for late return
    fee = 15 if returnDate.date() < datetime.date.today() else 0
    updateQuery = "UPDATE Borrow SET returned=:status, outstandingFee=:ofee WHERE borrowID=:bid"
    updateCursor = conn.cursor()
    try:
        updateCursor.execute(updateQuery, {"status":"Yes", "ofee":fee, "bid":borrowID})
    except sqlite3.IntegrityError:
        print("ERROR: Some information provided was wrong!\n")
    if conn:
        conn.commit()
    fineStatus = "No fine" if fee == 0 else "Fine of " + str(fee) + " dollars for late return."
    print("\n*** Return successful. " + fineStatus + " ***")
    
    input("Please press Enter to continue")


def donate_item():
    pass


def find_event():
    print("\n==================== Finding Events ====================")
    print("Please enter the following details of the event (can be left blank):")
    name = input("Name: ")
    time = input("Time:")
    location = input("Location: ")

    cursor = conn.cursor()
    query = "SELECT * FROM Events "
    if(name or time or location):
        query += "WHERE "
        query += "name=:queryName " if name else "TRUE "
        query += "AND "
        query += "time=:queryTime " if time else "TRUE "
        query += "AND "
        query += "location=:queryLocation" if location else "TRUE "

    cursor.execute(query, {"queryName":name, "queryTime":time, "queryLocation":location})
    rows = cursor.fetchall()

    print("\n==================== Results ====================")
    if rows:
        for row in rows:
            print(row)
    else:
        print("\nNo event(s) found")
    
    input("\nPlease press Enter to continue")



def register_event():
    pass

def volunteer():
    print("\n==================== Volunteer ====================")
    print("Please enter the following details of the event:")
    name = input("Name: ")
    while (name == ''):
        print("You must provide your name!")
        name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    email = input("Email: ")

    cursor = conn.cursor()
    query = "INSERT INTO Personnel(name, dob, position, email)" + "VALUES (:fullname, :date, :pos, :em)"
    try:
        cursor.execute(query, {"fullname":name, "date":dob, "pos":"Volunteer", "em":email})
    except sqlite3.IntegrityError:
        print("ERROR: Some information provided was wrong!\n")
    if conn:
        conn.commit()
    print("\nYou are now a volunteer for our library. Have fun!")

def get_contact_information():
    print("\n==================== Help from Librarian ====================")
    cursor = conn.cursor()

    query = "SELECT name, email FROM Personnel WHERE position = 'Librarian' "
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print("\nPlease contact our librarians from the following list:")
        for row in rows:
            print(" Name: " + row[0] + " - Email: " + row[1])
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
    if conn:
        conn.close()

if __name__ == "__main__":
    main()