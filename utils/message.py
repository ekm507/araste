# message handling
# levels ( Error, Warning, Info, Text )
# note: levels and text with string types

from colorama import Fore

LevelColor = ''
def message(level, text):
    if level == 'Error':
        LevelColor = Fore.RED
    elif level == 'Warning':
        LevelColor = Fore.YELLOW
    elif level == 'Info':
        LevelColor = Fore.BLUE
    elif level == 'Text':
        LevelColor = Fore.WHITE
    else:
        LevelColor = Fore.WHITE

    print(f"{LevelColor}{level}:\n\t{text}")
