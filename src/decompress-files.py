'''
Project: CSC 426 Data Mining
Author: Trinity Stroud
Description: This program decompresses all of the .json.bz2 files into readable json files
'''

import bz2
import os, os.path

# Path to where GitHub repo is stored
userpath = r"C:\Users\[username]\Documents\GitHub"
# Path to Twitter stream data from March 1, 2020
olddirpath = userpath + r"\CSC-426\twitter_stream_2020_03_01\03\01"
# Path to where decompressed files will be stored
newdirpath = userpath + r"\CSC-426\resources\twitter_stream_2020_03_01"

# List of directories in the current directory (represents hours)
dirs = [name for name in os.listdir(olddirpath) if not os.path.isfile(name)]

# For each directory...
for dirname in dirs:
    path = os.path.join(olddirpath, dirname)
    # List of files in the current subdirectory
    files = [name for name in os.listdir(path)]

    # For each file...
    for filename in files:
        oldfilepath = os.path.join(olddirpath, dirname, filename)
        newfilepath = os.path.join(newdirpath, dirname, filename[0:-4])

        newfile = open(newfilepath, 'wb')
        file = bz2.BZ2File(oldfilepath, 'rb')

        # Decompress the file and save the data to a new file
        for data in iter(lambda : file.read(100 * 1024), b''):
            newfile.write(data)

        # Close the open files
        file.close()
        newfile.close()
