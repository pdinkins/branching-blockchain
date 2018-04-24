'''
#MENU
This is a simple module for displaying a menu, making a choice, and calling the linked function.

USE:
    1. import menu
    2. define menu choice functions
    3. define menu dictionary
        {'menu choice label': corresponding function}
    4. menu.initialize_menu(**menu_dictionary, **menutitle)
'''

def display_menu_choices(menu_dictionary, menutitle):
    menulist = list(menu_dictionary.keys())
    j = 1
    print('\n' + menutitle, '\n')
    for i in range(0,len(menulist)):
        print(j,'-', menulist[i])
        j += 1 
    choose_from_menu(menulist, menu_dictionary)


def choose_from_menu(menulist, menu_dictionary):
    try:
        menuchoice = int(input('\nMenu Choice:  '))
        menuchoice -= 1
        print()
        menu_dictionary[menulist[menuchoice]]()
    except (IndexError, ValueError):
        print('***invalid choice***')


def initialize_menu(menu_dictionary, menutitle):
    display_menu_choices(menu_dictionary, menutitle)
