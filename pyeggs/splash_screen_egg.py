from .egg_base import EggBase

SPLASH_HINT = \
"""Children love making me,
Divers avoid me at all costs,
Water and I go hand in hand,
What am I?"""

class SplashScreenEgg(EggBase):
    trigger = 'splash'
    
    def __init__(self):
        super().__init__()
        self.hint = SPLASH_HINT
    
    def execute(self, consoleBuffer):
        print('SPLASH SCREEN NEEDED!')
