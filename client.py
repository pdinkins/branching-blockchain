NODE_STATUS = [0]

# client interface

def log(message):
    import inspect, logging
    import datetime as dt
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    func = inspect.currentframe().f_back.f_code
    logging.debug("{}\t{}\t{}\t{}".format(
        dt.datetime.now(),
        func.co_filename,
        func.co_name,
        message))


class SuperUser:

    def __init__(self):
        # node status inspect
        self.node_s()

    def node_s(self):
        if NODE_STATUS[0] == 0:
            self._new_user_builder()
        elif NODE_STATUS[0] == 1:
            log('lol')
        
        else:
            log("ERROR_0")


    def _new_user_builder(self):
        from pynetwork.node_0.setup import NewWallet, builder
        from pynetwork.node_0.setup import UserBuild, Admin, log
        # system build out
        self.new_user_build = UserBuild()
        self.newb_os = self.new_user_build.build
        # admin gen
        self.def_adm = Admin()
        self.adm_creds = [self.def_adm.username, self.def_adm.password]
        # user config data
        self.user_config = {'creds': self.adm_creds, 'build': self.newb_os}
        log(self.user_config)

        #### these are the same 
        # log(self.newb_os)
        # log(self.user_config['build'])

        self.decode = self.user_config['creds']
        log(self.decode)

        self.user_name = self.decode[0]
        log(self.user_name)

        self.password = self.decode[1]
        log(self.password)

        self.decode2 = self.user_config['build']
        log(self.decode2)

        self.new_wallet = NewWallet(self.user_name, self.password, self.decode2)
        
        self.wallet_id = self.new_wallet.id
        log(self.wallet_id)

        builder(self.wallet_id, self.user_name, self.decode2)
        log()



nighthawk = SuperUser()

###### project flow
login = True
run = True

## LOGIN
"""
def login_window():
    while login:
        title()
        usn = input('username: ')
                    
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
"""