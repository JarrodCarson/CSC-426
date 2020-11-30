'''
    Project: CSC 426 Data Mining
    Authors: Jarrod Carson & Trinity Stroud
'''

import json
import os
import pandas
import sys

def frequency(chunk_size = 2500):
    '''
    Performs frequency analysis on the data.

    Vars:
        chunk_size: Number of lines represented by each frequency dict. Affects execution time
    Returns:
        Dictionary of words:frequency
    '''

    # Whitelist of words to analyze
    whitelist = []
    # List of multiple frequency dictionary. Splitting them up improves analysis speed
    word_freqs = []
    # Ranks tweets by scores as sorting a dictionary is complicated
    ranks = {}
    # Individual frequency analysis dictionary
    word_freq = {}
    # Scores for each tweet. i.e. the number of keywords that occur for a given tweet
    tweet_scores = {}
    # List of all parsed JSON files
    parsed_json = [os.path.join("resources", f) for f in os.listdir("resources") if f.endswith(".json") and not f.startswith('res_')]

    # Read in whitelist words
    if os.path.exists(os.path.join("resources", "keywords.txt")):
        whitelist = [word.strip().lower() for word in open("resources\\keywords.txt", 'r')]

    for f in parsed_json:
        sys.stdout.write(f"[ ] Frequency analysis on {f}:       ")
        sys.stdout.flush()

        # Number of lines in a file. Used for progress display
        num_lines = 0
        # Progress percentage
        s = '0.000%'
        # Obtaining file size
        with open(f, 'r') as temp:
            for _ in temp:
                num_lines += 1


        for i, line in enumerate(open(f, 'r')):

            # Chunking size. Determines how many lines each freq. dict. represents
            if i % chunk_size == 0:
                # Progress Output
                sys.stdout.write("\b" * len(s))
                s = f"%.3F" % (i/float(num_lines) * 100) + "%"
                sys.stdout.write(s)
                sys.stdout.flush()
                word_freqs.append(word_freq)
                word_freq = {}

            # Parsing Tweet text for words
            line = json.loads(line)
            text = [word.lower().strip() for word in whitelist if word in line['text']]
            if text:
                tweet = {"ID": line["id_str"],
                         "Created": line["created_at"],
                         "Text": line["text"],
                         "Keywords": {word: text.count(word) for word in text},
                         "Coordinates": line["coordinates"],
                         "Place": line["place"],
                         "Score": len(text)}

                if tweet["Score"] not in ranks:
                    ranks[tweet["Score"]] = []

                ranks[tweet["Score"]].append(tweet)

            word_freq = {**word_freq, 
                         **{word: (text.count(word) if word not in word_freq else word_freq[word] + text.count(word)) for word in text}}

        sys.stdout.write("\b" * len(f) + f"\r[+] Frequency analysis complete 100.000%" + " " * len(f) + "\n")
        sys.stdout.flush()

    sys.stdout.write(f"\r[ ] Consolidating results...")
    sys.stdout.flush()

    # Combining all individual freq. dicts. into a single dict.
    freq_final = {}
    for freq in word_freqs:
        freq_final = {**freq_final, **freq}

    sys.stdout.write(f"\r[+] Consolidation complete\n")
    sys.stdout.flush()
    # Writing frequency analysis results to JSON file
    with open("resources\\res_freq_analysis.json", 'w') as out_file:
        out_file.write(json.dumps(freq_final, indent=4))

    # Sorting tweets by rank
    for score in list(ranks.keys())[::-1]:
        for tweet in ranks[score]:
            tweet_id = tweet["ID"]
            del tweet["ID"]
            tweet_scores[tweet_id] = tweet


    # Writing tweet scores to JSON file
    with open("resources\\res_tweet_scores.json", 'w') as out_file:
        out_file.write(json.dumps(tweet_scores, indent=4))
    

def preprocess(data):
    '''
    Preprocesses data.

    Vars:
        data:   Pandas DF, List, or Dictionary containing twitter data
    Returns:
        Preprocessed DF, List, or Dictionary
    '''