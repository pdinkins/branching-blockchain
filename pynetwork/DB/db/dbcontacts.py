# Parker Dinkins
# Contacts Manager


import csv

# lists to store data from the csv file
names = []
email = []
phone = []

# reads and adds data from the csv to the lists above
def csvread():
    try:
        with open('contacts.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                names.append(row[0])
                email.append(row[1])
                phone.append(row[2])
    except FileNotFoundError:
        print('Could not find contacts file.\nA new was file created.\n')
        open('contacts.csv', 'w')
        csvread()
            
# writes a new contact to the csv file
def csvwrite():
    with open('contacts.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        name = input('name: ')
        email = input('email: ')
        phone = input('phone: ')
        filewriter.writerow([name, email, phone])

# allows the user to view a single contact from the csv file
# display the information in a readble fashion
def view():
    try:
        if len(names) == 0:
            print('*** The contacts file is empyty ***')
        else:    
            v1 = int(input('\nContact number: '))
            v = v1 - 1
            print('\nName: ', names[v])
            print('Email: ', email[v])
            print('Phone #: ', phone[v])
    except ValueError:
        print('*** Invalid Integer ***')
    except IndexError:
        print('*** Invalid Contact Number ***')

# Lists all of the names from the contacts file and gives them index values
# those index values are used for the rest of the functions 
def llist():
    if len(names) == 0:
        print('*** The contacts file is empty ***')
    else:
        namelen = len(names)
        listnum = 1
        for i in range(0, namelen):
            print(listnum, '. ', names[i])
            listnum += 1

# clears the lists so they can be re-parsed in the csvread function
def listclear():
    names.clear()
    email.clear()
    phone.clear()

# adds contact to the file, clears the storage lists and re-parses the csv file
def add():
    csvwrite()
    listclear()
    csvread()
    
# deletes a contact be index number defined in the llist function
def delete():
    try:
        if len(names) == 0:
            print('*** The contacts file is empty ***')
        else:
            file = open('contacts.csv', 'r')
            lines = file.readlines()
            file.close()
            delnum = int(input('Contact number to delete: '))
            delnum -= 1
            del lines[delnum]
            open('contacts.csv', 'w').writelines(lines)
            listclear()
            csvread()
    except IndexError:
        print('*** Invalid Contact Number ***')
    except ValueError:
        print('*** Invalid Integer ***')

# command menu
def contacts_command_menu():
    print('COMMAND MENU')
    menuchoices = [
        'list - Display all contacts',
        'view - View a contact',
        'add - Add a contact',
        'del - Delete a contact',
        'exit - Exit program'
        ]
    size = len(menuchoices)
    for i in range(0, size):
        print(menuchoices[i])

# dictionary with the available commands
command_dict = {
    'list': llist,
    'view': view,
    'add': add,
    'del': delete
    }

# loops that run the program
while True:
    print('Contact Manager\n')
    csvread()
    contacts_command_menu()
    break    

while True:
    try:
        command = input('\nCommand: ')
        if command == 'exit':
            print('Bye')
            break
        else:
            command_dict[command]()
    except KeyError:
        print("\n****Invalid Command****\n")
