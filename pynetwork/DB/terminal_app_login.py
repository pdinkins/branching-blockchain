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
        print(datetime.datetime.now().date(), datetime.datetime.now().time())


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


def testfunc():
    print('this is the function')


login = True
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
    testfunc()

