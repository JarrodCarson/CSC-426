'''
    Project: CSC 426 Data Mining
    Authors: Jarrod Carson
'''

import json
import os
import sys

def __collect_json(path, files=[]):
    '''
    Recursively collects JSON files, given a directory.

    Vars:
        path:   A string file path to a directory.
    Returns:
        List of file paths to JSON files.
    '''
    
    for p in os.listdir(path):
        p = os.path.join(path, p)
        if os.path.isdir(p):
            __collect_json(p, files) 
        elif os.path.isfile(p) and p.endswith(".json"):
            files.append(p)
    return files


def __filter_attr(json_file):
    '''
    Removes fields from JSON data

    Vars:
        json_file:  A path to a JSON file.
    Returns:
        Dictionary containing filtered JSON data.
    '''

    filtered_lines = []
    whitelist = [
        #'contributors',
        'coordinates',
        'created_at',
        #'delete',
        #'display_text_range',
        'entities',
        'extended_entities',
        #'extended_tweet',
        #'favorite_count',
        #'favorited',
        #'filter_level',
        #'geo',
        #'id',
        'id_str',
        #'in_reply_to_screen_name',
        #'in_reply_to_status_id',
        'in_reply_to_status_id_str',
        #'in_reply_to_user_id',
        #'in_reply_to_user_id_str',
        #'is_quote_status',
        'lang',
        'place',
        #'possibly_sensitive',
        #'quote_count',
        'quoted_status',
        #'quoted_status_id',
        #'quoted_status_id_str',
        #'quoted_status_permalink',
        #'reply_count',
        #'retweet_count',
        #'retweeted',
        #'retweeted_status',
        #'source',
        'text',
        #'timestamp_ms',
        #'truncated',
        'user'
    ]

    with open(json_file, 'r') as f:
        for line in f:
            try:
                json_dict = json.loads(line)
            # Filters out broken JSON strings
            except json.JSONDecodeError:
                continue
            except:
                raise Exception(f"Something else went wrong. Please inspect in debugger\nFile: {json_file}")
            filtered_dict = {key: json_dict[key] for key in whitelist if key in json_dict}
            if filtered_dict and filtered_dict['lang'] == 'en':
                filtered_lines.append(json.dumps(filtered_dict).strip() + "\n")
    os.remove(json_file)
    return filtered_lines


def parse(json_file, progress_out=False):
    '''
    Parses a given JSON file.

    Vars:
        json_file:      Path to a JSON file or folder containing JSON files
        progress_out:   Bool determining if detailed progress output should be displayed

    Returns:
        Dictionary containing JSON data.
    '''
    files = None

    # If given directory
    if os.path.isdir(json_file):
        if progress_out:
            sys.stdout.write("[ ] Recursively Collecting Files...")
            sys.stdout.flush()
        else:
            print("Recursively Collecting Files... ", end='')

        files = __collect_json(json_file)

        if progress_out:
            sys.stdout.write("\r")
            sys.stdout.write("[+] Recursively Collecting Files -- Complete\n")
            sys.stdout.flush()
        else:
            print("Done")
    # If given file path
    elif os.path.isfile(json_file):
        files.append(json_file)
    # If given anything else
    else:
        raise FileNotFoundError(f"Path {json_file} does not exist.")
    
    out_file = open("resources/twitter_stream_2020_03_01.json", "w")
    
    if progress_out:
        size = len(files)
        sys.stdout.write(f"[ ] Parsing files... ")
        sys.stdout.flush()
    else:
        print("Parsing files... ", end='')

    for i, f in enumerate(files):

        if progress_out:
            # Progress bar
            s = f"%.3F" % (i/float(size) * 100) + "%"
            sys.stdout.write(s)
            sys.stdout.flush()

        out_file.writelines(__filter_attr(f))

        if progress_out:
            sys.stdout.write("\b" * len(s))

    if progress_out:
        sys.stdout.write("\r[+] Parsing Complete 100.000%\n")
        sys.stdout.flush()
    else:
        print("Done")

    out_file.close()
