#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-05-17
Purpose: Rock the Casbah
"""

import argparse
import os
import io
import sys
import random
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    # if args.text is the name of an existing file,
    # overwrite its value with the results of reading the file
    # otherwise just use the string itself as the text

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    for line in text.splitlines():
        #print(' '.join([word2num(word) for word in line.split()]))
        print(' '.join(map(word2num, line.split())))


# --------------------------------------------------
def word2num(word):
    """removes unwanted characters from word,
    converts remaining characters to ord
    returns string of sum of them
    """
    # cleaned = re.sub('[^A-Za-z0-9]', '', word)
    # ords = list(map(ord, cleaned))
    # return str(sum(ords))
    return str(sum(map(ord, re.sub('[^A-Za-z0-9]', '', word))))

# --------------------------------------------------
# def test_word2num():
#     """Test word2num"""
#     assert word2num("a") == "97"
#     assert word2num("abc") == "294"
#     assert word2num("ab'c") == "294"
#     assert word2num("4a-b'c,") == "346"

# --------------------------------------------------
if __name__ == '__main__':
    main()
