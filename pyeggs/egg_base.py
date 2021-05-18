from .shared import clearScreen, ConsoleWriter

class EggBase():
    hint = None
    trigger = None
    
    def __init__(self):
        self.found = False
        self.hint = EggBase.hint
        self.trigger = EggBase.trigger
        self.writeConsole = ConsoleWriter()
    
    def execute(self, consoleBuffer):
        raise('EggBase.execute() must be overriden!')
    
    def clearScreen(self):
        clearScreen()
    
    def endPrompt(self):
        input('Press enter to continue...')
    
    def restoreScreen(self, consoleBuffer):
        self.clearScreen()
        if consoleBuffer:
            self.writeConsole(consoleBuffer, endChar='')
