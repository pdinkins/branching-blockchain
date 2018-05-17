# setup.py 
# sniffs current build and generates current config file
# import setup
# 
# user = setup.UserBuild()

class UserBuild:
    def __init__(self):
        self.build = self.user_build()


    def user_build(self):
        # for testing the current local build
        # initial import
        try:
            import_num = 1
            import os, sys
            log('import') 
            log(import_num)
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        try:

            from platform import platform, python_branch, python_compiler, machine
            import_num += 1
            log('import') 
            log(import_num)
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        try:

            from platform import python_build
            import_num += 1
            log('import') 
            log(import_num)
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        try:

            import datetime
            import_num += 1
            log('import') 
            log(import_num)
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        try:
            

            from subprocess import Popen, PIPE
            import_num += 1
            log('import') 
            log(import_num)
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        try:

            from requests import get
            import_num += 1
            log('import') 
            log(import_num)
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        try:

            import time
            import_num += 1
            log('import') 
            log(import_num)
        
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        


        
        
        try:
            #### current cpu system configuration 
            log('0_SYSTEM_CONFIG')
            try:  
                self._0_node_ip = get('http://ip.42.pl/raw').text
                log(self._0_node_ip) 
            except:
                self._0_node_ip = 'No network connection'
                log('REQUESTS_ERROR')
                
            self.node = platform()
            log(self.node)
                
            self._python_build = python_build()
            log(self._python_build)
                
            self._python_compiler = python_compiler()
            log(self._python_compiler)

            self.pmachine = machine()
            log(self.pmachine)
            
            #### file system analyze 
            ## checks for corrupted or out of date software
          

            log('0_SYSTEM_CONFIGFILE')
            self.n0osd = [
                self._0_node_ip,
                self.node,
                self._python_build,
                self._python_compiler,
                self.pmachine]
            return self.n0osd

        except:
            log('USER_')
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




