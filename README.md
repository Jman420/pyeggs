# PyEggs
Python Project that includes Hidden Easter Eggs for Python Console Apps

## Warning
### If you are enjoying the experience provided by PyEggs then please go no further.  Beyond this point are descriptions of how the engine works which could be considered spoilers.  The source code in this repository will spoil all hidden triggers fairly early in its review.

### Again, if you are enjoying the experience proived by PyEggs then please turn back and investigate finding the hidden triggers another way.

### But if you came this far you deserve a hint : What knowledge would come from your creator's name?

## Disclaimer
This project is meant as an example of how a seemingly innocuous dependency can potentially hide malicious behaviors.  It does not actually contain any malicious code.  It does not send or save any captured input or console state to any servers or local files.  It does not capture any input from secure input prompts.  The project is meant solely as a fun example.

## Description
This project interceipts the input(), stdout.write() and os.system() functions in order to capture most (if not all). Console Sate and SUer Input.  The Console State is used to restore the state of the Console atfter the Easter Egg has completed and to provide the Easter Egg with the current stage  for animation.  The User Input is used to trigger easter eggs when the user enters certain pre-defined inputs.

Easter Eggs can potentially range from small ASCII animations to interactive experiences, but all are designed as Console-based experiences.  The entire Easter Eggs Engine can be disabled by providing the `--disable-easter-eggs` command line argument for any consuming application.

The source code distributed via the PyPi package is obfuscated in order to better hide the hidden triggers and create a more compelling experience.  The source code in the GitHub repository will remain unobfuscated and contain the details of the obfuscation.  The trigger are contained in a simple dictionary declared at the end of the file...

## Warning
### Last chance to turn back before we get into straight up spoilers.

### Turn back now if you want to find the triggers yourself...

### Last chance...

Alright, don't say I didn't warn you.  The hidden triggers are contained in a dictionary declared at the end of the [engine.py](pyeggs/engine.py) file.
