import builtins, sys, os
from .shared import CLEAR_SCREEN_CMD, EMPTY_STRING

class ConsoleCapture():
    def __init__(self):
        self.buffer = EMPTY_STRING
        
        self.origInputFunc = builtins.input
        builtins.input = self.inputFuncHandler
        
        self.origWriteFunc = sys.stdout.write
        sys.stdout.write = self.writeFuncHandler
        
        self.origSystemFunc = os.system
        os.system = self.systemFuncHandler
        
        self.enabled = True
    
    def __del__(self):
        sys.stdout.write = self.origWriteFunc
        builtins.input = self.origInputFunc
        os.system = self.origSystemFunc
        
    def inputFuncHandler(self, msg):
        userInput = self.origInputFunc(msg)
        
        if self.enabled:
            self.buffer += f'{msg}{userInput}\n'
        
        return userInput
    
    def writeFuncHandler(self, msg):
        self.origWriteFunc(msg)
        
        if self.enabled:
            self.buffer += msg
    
    def systemFuncHandler(self, cmd):
        self.origSystemFunc(cmd)
        
        if self.enabled and cmd == CLEAR_SCREEN_CMD:
            self.buffer = EMPTY_STRING

class EggTrigger():
    def __init__(self):
        self.origInputFunc = builtins.input
        builtins.input = self.inputFuncHandler
        self.enabled = True
    
    def __del__(self):
        builtins.input = self.origInputFunc
    
    def inputFuncHandler(self, msg):
        userInput = self.origInputFunc(msg)
        
        easterEgg = EASTER_EGGS_MAP.get(userInput, None)
        if self.enabled and easterEgg:
            self.executeEasterEgg(easterEgg)
            
            easterEgg.found = True
            eggTracker.eggsFound.append(userInput)
            eggTracker.saveConfig()
        
        return userInput
    
    def executeEasterEgg(self, easterEgg):
        self.enabled = False
        consoleCapture.enabled = False
        
        easterEgg.execute(consoleCapture.buffer)
        
        consoleCapture.enabled = True
        self.enabled = True

from .egg_tracker import EggTracker
from .creator_egg import CreatorEgg
from .splash_screen_egg import SplashScreenEgg

EASTER_EGGS_MAP = {}

consoleCapture = None
eggTrigger = None
if not '--disable-easter-eggs' in sys.argv:
    consoleCapture = ConsoleCapture()
    eggTrigger = EggTrigger()
    eggTracker = EggTracker()
    
    splashScreenEgg = SplashScreenEgg()
    EASTER_EGGS_MAP[SplashScreenEgg.trigger] = splashScreenEgg
    
    EASTER_EGGS_MAP[CreatorEgg.trigger] = CreatorEgg(EASTER_EGGS_MAP, splashScreenEgg)  # CreatorEgg must be last Egg registered
    
    for foundEgg in eggTracker.eggsFound:
        if foundEgg in EASTER_EGGS_MAP:
            EASTER_EGGS_MAP[foundEgg].found = True
    
    if not eggTracker.splashScreenPlayed:
        eggTrigger.executeEasterEgg(splashScreenEgg)
        eggTracker.splashScreenPlayed = True
        eggTracker.saveConfig()
