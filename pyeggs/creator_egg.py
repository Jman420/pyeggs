from random import randint

from .egg_base import EggBase

JMAN_HINT = "What knowledge would come from your creator's name?"

NO_EGGS_AVAILABLE_MSG = \
'''I left this hint for you to find,
that you might return another time.'''

ALL_EGGS_FOUND_MSG = \
'''You've found the Eggs, they're all through,
but we'll still wait and listen to you.'''

class CreatorEgg(EggBase):
    trigger = 'jman'

    def __init__(self, eggsMap, splashScreenEgg):
        super().__init__()
        self.hint = JMAN_HINT
        
        self.eggsList = list(eggsMap.values())
        if self in self.eggsList:
            self.eggsList.remove(self)
        if splashScreenEgg in self.eggsList:
            self.eggsList.remove(splashScreenEgg)
        self.splashScreenEgg = splashScreenEgg
    
    def execute(self, consoleBuffer):
        if len(self.eggsList) < 1:
            print(NO_EGGS_AVAILABLE_MSG)
            return
        
        hintsList = [ egg.hint for egg in self.eggsList if not egg.found ]
        if not self.splashScreenEgg.found:
            hintsList.append(self.splashScreenEgg.hint)
        
        if len(hintsList) < 1:
            print(ALL_EGGS_FOUND_MSG)
            return
        
        hintIndex = randint(0, len(hintsList)-1)
        print(hintsList[hintIndex])
