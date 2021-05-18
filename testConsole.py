import pyeggs.engine
from pyeggs.shared import ConsoleWriter

writeConsole = ConsoleWriter()

writeConsole('-------------------------------')
writeConsole('Easter Eggs Engine Test Console')
writeConsole('-------------------------------')

userInput = ''
while userInput != 'q':
    userInput = input('Prompt : ')
