'''
    Project: CSC 426 Data Mining
    Authors: Jarrod Carson & Trinity Stroud

    This is where the program is run from if using the command line
'''

from sys import argv
from src.main import main

if __name__ == "__main__":
    main(argv[1:])