'''
Project: CSC 426 Data Mining
Author: Trinity Stroud
'''

import bz2
import os, os.path
import sys
from shutil import copy

def decompress():
    '''
    Decompresses all .json.bz2 files into readable json files

    Vars:
        None
    Returns:
        None
    '''
    
    # Path to where GitHub repo is stored
    userpath = os.getcwd()
    # Path to Twitter stream data from March 1, 2020
    olddirpath = os.path.join(userpath, "twitter_stream_2020_03_01", "03", "01")
    # Path to where decompressed files will be stored
    newdirpath = os.path.join(userpath, "resources", "twitter_stream_2020_03_01")
    # Creates new directory if it doesn't exist
    if not os.path.exists(newdirpath):
        os.mkdir(newdirpath)

    # List of directories in the current directory (represents hours)
    dirs = [name for name in os.listdir(olddirpath) if not os.path.isfile(name)]

    size = len(dirs)
    sys.stdout.write(f"[ ] Decompressing files... ")
    sys.stdout.flush()

    # For each directory...
    for i, dirname in enumerate(dirs):

        s = f"%.3F" % (i/float(size) * 100) + "%"
        sys.stdout.write(s)
        sys.stdout.flush()

        path = os.path.join(olddirpath, dirname)
        # List of files in the current subdirectory
        files = [name for name in os.listdir(path)]

        # For each file...
        for filename in files:
            oldfilepath = os.path.join(olddirpath, dirname, filename)
            newfilepath = os.path.join(newdirpath, dirname)

            # Creates new directory if it doesn't exist
            if not os.path.exists(newfilepath):
                os.mkdir(newfilepath)
            # If file is already decompressed, just copies it over
            if not oldfilepath.endswith(".bz2"):
                copy(oldfilepath, newfilepath)
                continue
            newfilepath = os.path.join(newfilepath, filename[:-4])
            # If decompressed file already present in resources
            if os.path.exists(newfilepath):
                continue

            newfile = open(newfilepath, 'wb')
            file = bz2.BZ2File(oldfilepath, 'rb')

            # Decompress the file and save the data to a new file
            for data in iter(lambda : file.read(100 * 1024), b''):
                newfile.write(data)

            # Close the open files
            file.close()
            newfile.close()

        sys.stdout.write("\b" * len(s))

    sys.stdout.write("\r[+] Decompression Complete 100.000%\n")
    sys.stdout.flush()
        
