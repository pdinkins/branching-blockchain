# setup.py 
# sniffs current build and generates current config file
class UserBuild:
    def __init__(self):
        self.build = self.user_build()


    def user_build(self):
        # for testing the current local build
        # initial import
        try:
            import os, sys
            import platform
            import datetime
            import subprocess
            import requests
            import time
            import ipfsapi


        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        
        try:
            # current cpu system configuration 
            log('0_SYSTEM_CONFIG')
            try:  
                self._0_node_ip = requests.get('http://ip.42.pl/raw').text
                log(self._0_node_ip) 
            except:
                self._0_node_ip = 'No network connection'
                log('REQUESTS_ERROR')
                
            self.node = platform.platform()
            log(self.node)
                
            self._python_build = platform.python_build()
            log(self._python_build)
                
            self._python_compiler = platform.python_compiler()
            log(self._python_compiler)

            self.pmachine = platform.machine()
            log(self.pmachine)



            log('0_SYSTEM_CONFIGFILE')
            self.n0osd = [
                self._0_node_ip,
                self.node,
                self._python_build,
                self._python_compiler,
                self.pmachine]
            return self.n0osd

        except:
            print(datetime.datetime.now(), 'SYSTEM LOG')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise


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


user = UserBuild()

