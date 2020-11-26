'''
    Project: CSC 426 Data Mining
    Authors: Jarrod Carson & Trinity Stroud
'''
from os import path, system
#pylint: disable=import-error
from json_parser import parse

def main():
    system("cls")

    tweet_loc = path.join("twitter_stream_2020_03_01", "03", "01")
    print(f"Initializing Data Path: {tweet_loc}")
    parse(tweet_loc)


if __name__ == "__main__":
    main()
    