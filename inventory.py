#This program prints a menu for the user, displays the contents of a file, and adds new lines to the file
#Added functionality to update a pre-existing entry to increase quantity of that item

#the os module comes with the system function to pause and clear the screen
import os

#this function will display the menu and return a corrected form of the user's input
def displayMenuAndGetInput():
    inputString = " "
    choice = ' '
    pauseChar = ' '
    
    #clear the screen and then print the menu
    os.system('cls')
    print("")
    print ("*******************************************************************")
    print("")
    print("")
    print("Game Item Inventory")
    print("")
    print("")
    print ("*******************************************************************")
    print("")
    print("")
    
    print("[d] Display all the inventory from file.")
    print("[a] Append an item to the inventory file.")
    print("[q] Quit and commit changes to file.")
    
    #get the next character that the user inputs
    print("Choice (enter upper or lowercase letter option: ")
    inputString = input()
    inputString.lower()
    choice = inputString[0]
    
    while (choice != 'a' and choice != 'd' and choice != 'q') :
        #error message
        print("")
        print ("That is not an option")
        os.system('PAUSE')
        #reprint the menu
        choice = displayMenuAndGetInput()
    
    return choice

#this function will display the inventory's contents
def display_inventory():
    #initialize all variables
    inputFile = open("gameinventory.txt", "r")
    column1 = ""
    column2 = ""
    column3 = ""
    
    #clear the screen before printing
    os.system('cls')
    
    #the following lines check to determine whether the file is already open and whether it exists
    if os.path.exists("gameinventory.txt"):
        #store the file's contents
        linesList = inputFile.readlines()
        #iterate through file's contents by separating them into individual lines
        for line in linesList:
            #split up the line into individual entries based on whitespaces and store in array
            row = line.split()
            #print row out as individual blocks with a column width of 10
            #print("{:10x}".format(row[0]) +  "{:10x}".format(row[1]) +  "{:10x}".format(row[2]))
            #print('{:>10}'.format(row[0]))
            print(row[0].ljust(10, ' ') + row[1].ljust(10, ' ') + row[2].ljust(10, ' '))
    else:
        print("File does not exist")
    
    #return to main menu
    print("Press a key to return to main menu.")
    inputFile.close()
    os.system('PAUSE')

#this function will add new items to the inventory
def add_item():
    #initialize all variables
    inFile = open("gameinventory.txt", 'r')
    name = " "
    cost = " "
    amount = " "
    tempValue = 0
    updatedLine = False
    
    #Clear the screen
    os.system('cls')
	
    #the following lines check to determine whether the file is already open and whether it exists
    if os.path.exists("gameinventory.txt"):           
        #get the user input
        print ("Enter the name for this new item: ")
        name = input()
        print ("Enter unit cost for this item: ")
        cost = input()
        print ("Enter quantity in stock for this item: ")
        amount = input()
            
        #set all letters in the name to lowercase
        name.lower()
            
        #create the temporary file
        tempFile = open("gameinventory1.txt", 'w+')
            
        #store the file's contents
        linesList = inFile.readlines()
        #iterate through file's contents by separating them into individual lines
        for line in linesList:
            #split up the line into individual entries based on whitespaces and store in array
            row = line.split()
            #if that item already exists in the file, increment the quantity of that item
            if (row[0] == name and row[1] == cost):
                tempValue = int(row[2]) + int(amount)
                tempFile.write(row[0] + " " + row[1] + " " + str(tempValue) + "\n")
                updatedLine = True
            else:
                tempFile.write(row[0] + " " + row[1] + " " + row[2] + "\n")
        #if the user's input did not update a pre-existing line, write the new line to the bottom of the file
        if not updatedLine:
            tempFile.write(str(name) + " " + str(cost) + " " + str(amount) + "\n")
                
        #open actual file to ouput to it and empty out what is already there
        outputFile = open("gameinventory.txt", 'w')
            
        #reset cursor back to start
        tempFile.seek(0)
            
        #store the file's contents
        linesList = tempFile.readlines()
        #iterate through file's contents by separating them into individual lines
        for line in linesList:
            #split up the line into individual entries based on whitespaces and store in array
            row = line.split()
            #write content of tempFile to outputFile
            outputFile.write(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + "\n")
            
        #successfully added
        print("Item added to the inventory!")
            
        #close and delete the temporary file from earlier
        tempFile.close()
        os.remove("gameinventory1.txt")
        inFile.close()
        outputFile.close()
    else:
        print("File does not exist")
    #return to main menu
    print("Press a key to return to main menu.")
    os.system('PAUSE')

choice = ' '
shouldContinue = True

while shouldContinue:
    choice = displayMenuAndGetInput()
    
    if (choice == 'q') :
        shouldContinue = False
    elif (choice == 'd'):
        display_inventory()
    elif (choice == 'a'):
        add_item()