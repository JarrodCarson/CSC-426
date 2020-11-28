'''
    Project: CSC 426 Data Mining
    Authors: Jarrod Carson & Trinity Stroud
'''
from os import path, system
#pylint: disable=import-error
from json_parser import parse
from decompress_files import decompress

def main():
    system("cls")

    if path.exists(path.join("resources", "twitter_stream_2020_03_01.json")):
        print("Parsed file found. Skipping decompression/parsing")
        exit()
    decompress()
    parse(path.join("resources", "twitter_stream_2020_03_01"))


if __name__ == "__main__":
    main()
    