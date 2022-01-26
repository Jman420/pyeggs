from .egg_base import EggBase

SOCCER_HINT = ''
SOCCER_TRIGGER = 'soccer'

class SoccerEgg(EggBase):
    hint = SOCCER_HINT
    trigger = SOCCER_TRIGGER
    
    def __init__(self):
        super().__init__()
        self.hint = SOCCER_HINT
        self.trigger = SOCCER_TRIGGER
    
    def execute(self, consoleBuffer):
        self.clearScreen()
