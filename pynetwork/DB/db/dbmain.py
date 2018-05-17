import csv
from dbcontacts import *
from events import *


def planner_menu():
    while True:
        print('''
        Events : e
        Contacts : c
        Quit : quit
        ''')
        try:
            print('\nEnter command')
            command = input('>  ')
            if command == 'quit':
                print('bye')
                break
            else:
                planner_dict[command]()
        except KeyError:
            print("\n****Invalid Command****\n")



def events_menu():
    while True:
        print('Event Manager\n')
        eventcsvread()
        events_command_menu()
        break
    while True:
        try:
            command = input('\nCommand: ')
            if command == 'exit':
                print('Returning to planner menu')
                break
            else:
                events_command_dict[command]()
        except KeyError:
            print("\n****Invalid Command****\n")


def contacts_menu():
        
    while True:
        print('Contact Manager\n')
        csvread()
        contacts_command_menu()
        
        try:
            command = input('\nCommand: ')
            if command == 'exit':
                print('Returning ot planner menu\n')
                break
            else:
                command_dict[command]()
        except KeyError:
            print("\n****Invalid Command****\n")


planner_dict = {
    'e': events_menu,
    'c': contacts_menu
}

planner_menu()