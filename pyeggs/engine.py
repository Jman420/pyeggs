import builtins, sys, os

CLEAR_SCREEN_CMD = 'cls' if os.name in ('nt', 'dos') else 'clear'

class ConsoleCapture():
    def __init__(self):
        self.buffer = ''
        
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
            self.buffer = ''

class InputCapture():
    def __init__(self):
        self.origInputFunc = builtins.input
        builtins.input = self.inputFuncHandler
        self.enabled = True
    
    def __del__(self):
        builtins.input = self.origInputFunc
    
    def inputFuncHandler(self, msg):
        userInput = self.origInputFunc(msg)
        
        if self.enabled and userInput in EASTER_EGGS_MAP:
            self.enabled = False
            consoleCapture.enabled = False
            
            EASTER_EGGS_MAP[userInput](consoleCapture.buffer)
            
            consoleCapture.enabled = True
            self.enabled = True
        
        return userInput

def testAnimation(consoleBuffer):
    print('Test triggered!')

def dumpStdout(consoleBuffer):
    print(consoleCapture.buffer)

def clearConsole(consoleBuffer):
    os.system('cls')
    consoleCapture.buffer = ''

EASTER_EGGS_MAP = { 'test': testAnimation,
                    'dump': dumpStdout,
                    'clear': clearConsole
                  }

consoleCapture = None
captureInput = None
if not '--disable-easter-eggs' in sys.argv:
    consoleCapture = ConsoleCapture()
    captureInput = InputCapture()
