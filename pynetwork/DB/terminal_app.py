from time import sleep
import os

class Admin:

    def __init__(self, username, password):
        self.username = username
        self.password = password


admin1 = Admin('admin', 'password')

class DateTime():
    def dt(self):
        import datetime
        print(datetime.datetime.now().date(),'    ', datetime.datetime.now().time())


dt1 = DateTime()


def title():
    print('=' * 30)
    dt1.dt()
    print('=' * 30)


def clear():
    import platform
    ops = platform.system()
    if ops == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def q():
    quit()

def testfunc():
    print('this is the function')

def commandinput():
    try:
        func_dict = {'dt': dt1.dt,
                     't': title,
                     'web': webscraper,
                     'quit': q}
        print('dt: date/time\nt: title\nweb: webscraper\nquit: quit\n')
        print('Enter a Command')
        command = input('>>>')
        if command != 'quit':
            func_dict[command]()
        elif command == 'quit':
            q()
    except KeyError:
        print('error')

def webscraper():
    from bs4 import BeautifulSoup
    import requests


    '''
    input file name
    input target website url
    scrapes html content from the target 
    
    '''

    print("================")
    print("Website Scrapper")
    print("====================")
    print("file will be saved as an .html\nin the folder the script is run from")
    print("====================")

    filename = input(str("file save name: "))
    print("========================")
    url = input(str(" target url: "))
    print("========================")

    r = requests.get(url)

    soup = BeautifulSoup(r.text)

    print(soup.prettify())
    print(soup.find_all('a'))
    f = open(filename + ".html", "w+")
    f.write(soup.prettify())
    s = soup.prettify()
    f.write(s)
    f.close()

login = False
run = True

while login:
    title()
    usn = input('username: ')
    if usn != admin1.username:
        clear()
                
    elif usn == admin1.username:
        clear()
        title()
        pasw = input('password: ')

        if pasw == admin1.password:
            clear()
            title()
            print('login succesfull')
            sleep(1)
            clear()
            break
            
while run:
    commandinput()
    sleep(3)
    clear()
    

