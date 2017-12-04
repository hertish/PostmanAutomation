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

class PostManLogger:
    
    def __init__(self, loggLevel, loggText, param1='', param2=''):
      self.loggLevel = loggLevel
      self.loggText = loggText
      self.param1 = param1
      self.param2 = param2
      
    def postManAutomationLogging(self):
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
        if self.loggLevel == 'warning':
            logging.warning('%s %s %s',self.loggText,self.param1,self.param2)
        elif self.loggLevel == 'debug': 
            logging.debug('%s %s %s',self.loggText,self.param1,self.param2)
        elif self.loggLevel == 'info': 
            logging.info('%s %s %s',self.loggText,self.param1,self.param2)
        elif self.loggLevel == 'critical': 
            logging.critical('%s %s %s',self.loggText,self.param1,self.param2)
        elif self.loggLevel == 'error': 
            logging.error('%s %s %s',self.loggText,self.param1,self.param2)
        else:
            logging.warning('%s %s %s',self.loggText,self.param1,self.param2)
