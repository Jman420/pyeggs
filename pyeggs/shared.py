import os
from time import sleep

CLEAR_SCREEN_CMD = 'cls' if os.name in ('nt', 'dos') else 'clear'
NEW_LINE_CHAR = '\n'
EMPTY_STRING = ''

def clearScreen():
    os.system(CLEAR_SCREEN_CMD)

class ConsoleWriter():
    def __init__(self):
        self.endChar = NEW_LINE_CHAR
    
    def __call__(self, msg, charDelay=0, endChar=None):
        if endChar == None:
            endChar = self.endChar
        
        if charDelay > 0:
            self.printDelay(msg, charDelay)
        else:
            print(msg, end=EMPTY_STRING, flush=True)
        print(EMPTY_STRING, end=endChar, flush=True)
    
    def printDelay(self, msg, charDelay):
        for char in msg:
            sleep(charDelay)
            print(char, end=EMPTY_STRING, flush=True)
