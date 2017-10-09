import logging
import sys
import ConfigParser
from logging.handlers import RotatingFileHandler
from logging import handlers




#read system logging level
config = ConfigParser.ConfigParser()
config.readfp(open(r'postmanAutomation.ini'))
SystemLoggingLevel = config.get('Logging', 'loggingLevel')
SystemLoggingLevel = SystemLoggingLevel.upper()

#Read the logging level from standarIn
#Use ini file for this info
#loggingLevel = str(sys.argv)
#loggingLevel = loggingLevel.split("=")[1]
#loggingLevel = loggingLevel[:-2]
#loggingLevel = loggingLevel.upper()

#Setup the logging
log = logging.getLogger('')
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#Set standOut logging config	
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
log.addHandler(ch)
#Set file logging config
fh = handlers.RotatingFileHandler('PostManLog.txt')
fh.setFormatter(format)
log.addHandler(fh)

def postManAutomationLogging(loggLevel,logText,param1='',param2=''):
    #Set correct SystemLoggingLevel
    if SystemLoggingLevel == 'WARNING':
        log.setLevel(logging.WARNING)
    elif SystemLoggingLevel == 'INFO':    
        log.setLevel(logging.INFO)
    elif SystemLoggingLevel == 'DEBUG':
        log.setLevel(logging.DEBUG)
    elif SystemLoggingLevel == 'CRITICAL':
        log.setLevel(logging.CRITICAL)
    elif SystemLoggingLevel == 'ERROR':
        log.setLevel(logging.ERROR)
    else:
        logging.warning('Unknown SystemLoggingLevel. Warning level will be set')
        log.setLevel(logging.WARNING)

    #Start system logging
    if loggLevel == 'warning':
        logging.warning('%s %s %s',logText,param1,param2)
    elif loggLevel == 'debug': 
        logging.debug('%s %s %s',logText,param1,param2)
    elif loggLevel == 'info': 
        logging.info('%s %s %s',logText,param1,param2)
    elif loggLevel == 'critical': 
        logging.critical('%s %s %s',logText,param1,param2)
    elif loggLevel == 'error': 
        logging.error('%s %s %s',logText,param1,param2)
    else:
        logging.warning('%s %s %s',logText,param1,param2)
        print 'Sune'

