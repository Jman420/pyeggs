from random import randint

from .egg_base import EggBase

JMAN_HINT = "What knowledge would come from the creator's name?"
JMAN_TRIGGER = 'jman'

NO_EGGS_AVAILABLE_MSG = \
'''I left this hint for you to find,
that you might return another time.'''

ALL_EGGS_FOUND_MSG = \
'''You've found the Eggs, they're all through,
but I'll still wait and listen to you.'''

class CreatorEgg(EggBase):
    hint = JMAN_HINT
    trigger = JMAN_TRIGGER

    def __init__(self, eggsMap, splashScreenEgg):
        super().__init__()
        self.hint = JMAN_HINT
        self.trigger = JMAN_TRIGGER
        
        self.eggsList = list(eggsMap.values())
        if self in self.eggsList:
            self.eggsList.remove(self)
        if splashScreenEgg in self.eggsList:
            self.eggsList.remove(splashScreenEgg)
        self.splashScreenEgg = splashScreenEgg
    
    def execute(self, consoleBuffer):
        self.clearScreen()
        
        if len(self.eggsList) < 1:
            self.writeConsole(NO_EGGS_AVAILABLE_MSG)
            self.endEgg(consoleBuffer)
            return
        
        hintsList = [ egg.hint for egg in self.eggsList if not egg.found ]
        if not self.splashScreenEgg.found:
            hintsList.append(self.splashScreenEgg.hint)
        
        if len(hintsList) < 1:
            self.writeConsole(ALL_EGGS_FOUND_MSG)
            self.endEgg(consoleBuffer)
            return
        
        hintIndex = randint(0, len(hintsList)-1)
        self.writeConsole(hintsList[hintIndex])
        
        self.endEgg(consoleBuffer)
        
    def endEgg(self, consoleBuffer):
        self.endPrompt()
        self.restoreScreen(consoleBuffer)
