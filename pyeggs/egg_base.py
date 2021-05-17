class EggBase():
    trigger = None
    
    def __init__(self):
        self.found = False
        self.hint = None
        self.trigger = None
    
    def execute(self, consoleBuffer):
        raise('EggBase.execute() must be overriden!')
