from configparser import ConfigParser

EGGS_CONFIG_FILE = 'eggs.ini'
SPLASH_SCREEN_SECTION = 'splashScreen'
SPLASH_SCREEN_PLAYED_ENTRY = 'played'
EGGS_FOUND_SECTION = 'eggsFound'
TRUE_STRING = 'True'

class EggTracker():
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(EGGS_CONFIG_FILE)
        
        self.splashScreenPlayed = False
        if self.config.has_section(SPLASH_SCREEN_SECTION):
            self.splashScreenPlayed = (self.config[SPLASH_SCREEN_SECTION].get(SPLASH_SCREEN_PLAYED_ENTRY) == TRUE_STRING)
        
        self.eggsFound = list()
        if self.config.has_section(EGGS_FOUND_SECTION):
            for foundEgg in self.config[EGGS_FOUND_SECTION]:
                if self.config[EGGS_FOUND_SECTION][foundEgg] == TRUE_STRING:
                    self.eggsFound.append(foundEgg)

    def saveConfig(self):
        if not self.config.has_section(SPLASH_SCREEN_SECTION):
            self.config.add_section(SPLASH_SCREEN_SECTION)
        self.config[SPLASH_SCREEN_SECTION][SPLASH_SCREEN_PLAYED_ENTRY] = str(self.splashScreenPlayed)
        
        if not self.config.has_section(EGGS_FOUND_SECTION):
            self.config.add_section(EGGS_FOUND_SECTION)
        
        for foundEgg in self.eggsFound:
            self.config[EGGS_FOUND_SECTION][foundEgg] = TRUE_STRING
        
        with open(EGGS_CONFIG_FILE, 'w') as configFile:
            self.config.write(configFile)
