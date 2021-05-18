from time import sleep

from .egg_base import EggBase
from .shared import NEW_LINE_CHAR, EMPTY_STRING

from .creator_egg import CreatorEgg

NORMAL_DELAY = 0.3
FAST_DELAY = NORMAL_DELAY / 2.0
LOADING_MSG = '...'
SUCCESSFUL_MSG = 'done!'

SPLASH_HINT = \
"""Children love making me,
I cost divers points,
Water and I are inseparable.
What am I?"""
SPLASH_TRIGGER = 'splash'

class SplashScreenEgg(EggBase):
    hint = SPLASH_HINT
    trigger = SPLASH_TRIGGER
    
    def __init__(self):
        super().__init__()
        self.hint = SPLASH_HINT
        self.trigger = SPLASH_TRIGGER
    
    def execute(self, consoleBuffer):
        self.writeConsole.endChar = EMPTY_STRING
        self.clearScreen()
        
        self.writeConsole('Initializing Application Memory')
        self.printLoadingDoneMsg()
        
        self.writeConsole('Loading Application Dependencies :', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('\tLoading builtins')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tLoading sys')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tLoading os')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tLoading pyeggs')
        self.printLoadingMsg()
        self.writeConsole(LOADING_MSG * 3, charDelay=FAST_DELAY)
        self.writeConsole('injecting codecave')
        self.printLoadingMsg()
        self.writeConsole('hijacking process')
        self.printLoadingDoneMsg()
        
        self.writeConsole('Verifying Application Dependencies :', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('\tVerifying builtins')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tVerifying sys')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tVerifying os')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tVerifying pyeggs')
        self.printLoadingMsg()
        self.writeConsole('ERROR!', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('-----BEGIN ERROR HANDLING-----', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('Unexepected Application Dependency detected : pyeggs', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('Unloading Dependency : pyeggs')
        self.printLoadingMsg()
        self.writeConsole('FAILED!', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('\tException : Invalid Memory Address : 0x0by0jman', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('Unhandled Exception encountered')
        self.printLoadingMsg()
        actionTaken = 'terminating'
        self.writeConsole(actionTaken)
        self.writeConsole('\b' * len(actionTaken), charDelay=FAST_DELAY)
        self.writeConsole('continuing ', charDelay=FAST_DELAY, endChar=NEW_LINE_CHAR)
        
        self.writeConsole('------END ERROR HANDLING------', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('Initializing Application Dependencies :', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('\tInitializing builtins')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tInitializing sys')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tInitializing os')
        self.printLoadingDoneMsg()
        
        self.writeConsole('\tInitializing pyeggs')
        self.printLoadingMsg()
        self.writeConsole('intercepting renderer')
        self.printLoadingMsg()
        self.writeConsole('intercepting input')
        self.printLoadingMsg()
        self.writeConsole('hiding easter eggs')
        self.printLoadingDoneMsg()
        
        self.writeConsole('Executing Application...', endChar=NEW_LINE_CHAR)
        
        self.writeConsole('Providing Hint : ')
        self.writeConsole(CreatorEgg.hint, charDelay=FAST_DELAY, endChar=NEW_LINE_CHAR)
        
        self.endPrompt()
        self.restoreScreen(consoleBuffer)
    
    def printLoadingDoneMsg(self):
        self.printLoadingMsg()
        self.writeConsole(SUCCESSFUL_MSG, endChar=NEW_LINE_CHAR)
    
    def printLoadingMsg(self):
        self.writeConsole(LOADING_MSG, charDelay=NORMAL_DELAY)
        sleep(NORMAL_DELAY)
