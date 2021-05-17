import os

CLEAR_SCREEN_CMD = 'cls' if os.name in ('nt', 'dos') else 'clear'

def clearScreen():
    os.system(CLEAR_SCREEN_CMD)
