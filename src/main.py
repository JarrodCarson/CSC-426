'''
    Project: CSC 426 Data Mining
    Authors: Jarrod Carson & Trinity Stroud
'''
import time
from os import path, system
#pylint: disable=import-error
from .json_parser import parse
from .decompress_files import decompress
from .analysis import frequency

def main(argv):
    system("cls")

    progress_out = False

    if argv and argv[0] in ("-v", "-V"):
        progress_out = True

    # Used for timing function execution time
    timing = False

    # Check if the files have been parsed
    if path.exists(path.join("resources", "twitter_stream_2020_03_01.json")):
        print("Parsed file found. Skipping decompression/parsing")
    
    # Check if the files have been decompressed
    elif path.exists(path.join("resources", "twitter_stream_2020_03_01")):
        parse(path.join("resources", "twitter_stream_2020_03_01"))
    
    # Check if the files have not been decompressed
    else:
        decompress(progress_out)
        parse(path.join("resources", "twitter_stream_2020_03_01"), progress_out)

    if timing:
        start_1 = time.time()
        frequency(5000, progress_out)
        total_1 = time.time() - start_1
        start_2 = time.time()
        frequency(2500, progress_out)
        total_2 = time.time() - start_2

        print(f"Chunk size 5000: {total_1}\nChunk size 2500: {total_2}")
    
    else:
        frequency(progress_out=progress_out)

#if __name__ == "__main__":
#    main()
    