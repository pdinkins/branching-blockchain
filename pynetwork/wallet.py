# Wallet
# stores all functions relating to the user hash wallet

# dyanmically stores data for wallet currently in use
current_wallet = []
wallet_data = []

class NewWallet:
    def __init__(self):
        self.timestamp = self.time_stamp()
        self.usr_nym = self.user_nym()
        self.id = self.generate_user_id()

    def time_stamp(self):
        import datetime 
        return datetime.datetime.now()

    def user_nym(self):
        usernym = input('This info will be used to name the local wallet file.\nuser_nym> ')
        return usernym

    def generate_user_id(self):
        import hashlib
        wid = hashlib.sha256()
        wid.update(str(self.timestamp).encode('utf=8') +
                    str(self.usr_nym).encode('utf-8'))
        return wid.hexdigest()

def generate_new_wallet():
    wallet = NewWallet()
    wd = [wallet.id, wallet.usr_nym, wallet.timestamp]
    for i in range(0, len(wd)):
        print(wd[i])
    set_current_wallet(wd)

def set_current_wallet(rgw):
    try:
        d = str(input('Use recently generated wallet as current usable hash wallet [y/n]? >')).lower()
        if d == 'y':
            for i in range(0, len(rgw)):
                current_wallet.append(rgw[i])
            print('Succesfully set the current usable wallet')
            # pipe back to client interface
        elif d == 'n':
            aus = str(input('are you sure [y/n]? > ')).lower()
            if aus == 'y':
                # pipe to client interface 
                print('Did not set current usable wallet')
            elif aus == 'n':
                for i in range(0, len(rgw)):
                    current_wallet.append(rgw[i])
            else: 
                raise TypeError
        else:
            raise TypeError

    except TypeError:
        print("ERROR: Not a valid input")
        return


def print_cw():
    for i in range(0, len(current_wallet)):
        print(current_wallet[i])

class WalletFile:
    def __init__(self):
        self.wfn = self.gwfn()
        self.walletfile = self.generate_nwf()

    def gwfn(self):
        # relay function for future security checks on wallet
        file_nym = self.cwe()
        return file_nym

    # checks if current wallet exists and generates if not
    def cwe(self):
        if not current_wallet:
            print('No current usable wallet')
            try:
                gen = str(input('Generate new wallet [y/n]? >')).lower()
                if gen == 'y':
                    generate_new_wallet()
                    print('Test statement for flow..........')
                elif gen == 'n':
                    # pipe to function to set wallet from file
                    pass
                else:
                    raise TypeError
            except TypeError:
                print('ERROR: Invalid input')
        elif current_wallet:
            w_nym = current_wallet[0]
            wfn = w_nym + '.csv'
            return wfn


    def generate_nwf(self):
        import csv
        open(self.wfn, mode='w')


def write_wallet():
    wallet_f = WalletFile()
    name = wallet_f.wfn
    import csv
    with open(name, 'a', newline='') as wallet:
        writer = csv.writer(wallet)
        writer.writerow([current_wallet[0],
                        current_wallet[1],
                        current_wallet[2]])

def write_cwf():
    import csv
    try:
        with open ('main.csv', 'w', newline='') as cwallet:
            writer = csv.writer(cwallet)
            writer.writerow([current_wallet[0],
                            current_wallet[1],
                            current_wallet[2]])
    except FileNotFoundError:
        open('main.csv', 'w')
        return



def parse_wallet():
    try:
        wallet_data.clear()
        import csv
        walletfile = str(input('walletfile> '))
        with open(walletfile) as wallet:
            reader = csv.reader(wallet)
            for row in reader:
                wallet_data.append(row[0])
                wallet_data.append(row[1])
                wallet_data.append(row[2])
    except FileNotFoundError:
        print('ERROR: WALLET__NOT__FOUND')





debug_menu = False
'''
import app.menu as m

md = {'new wallet': generate_new_wallet,
    'print current wallet info': print_cw,
    'write wallet': write_wallet,
    'quit': m.quit_menu}

while debug_menu:
    m.initialize_menu(md, 'title')
'''