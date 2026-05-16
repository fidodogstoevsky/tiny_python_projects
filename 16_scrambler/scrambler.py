#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-24
Purpose: Rock the Casbah
"""

import argparse
import io
import os
import sys
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    ##################################################
    ##### my solution
    # for line in args.text.splitlines():
    #     newline = []
    #     for word in splitter.split(line):
    #         if re.match(f'[{string.ascii_letters}]', word):
    #             newline += scramble(word)
    #         else:
    #             newline += word
    #     print(''.join(newline))
    ##################################################

    ##################################################
    ##### ken's solution
    for line in args.text.splitlines():
        # str.splitlines preserves the line breaks in the input text
        print(''.join(map(scramble, splitter.split(line))))
    ##################################################




# --------------------------------------------------
def scramble(word):
    """Scramble a word"""

    ##################################################
    ##### my solution
    # start = word[0]
    # end = word[-1]
    # if len(word) == 1:
    #     middle = ''
    #     end = ''
    # elif len(word) == 2:
    #     middle = ''
    # else:
    #     middle = list(word[1:-1])
    #     random.shuffle(middle)

    # return start + ''.join([char for char in middle]) + end
    ##################################################

    ##################################################
    ##### ken's solution
    if len(word) > 3 and re.match(r'\w+', word):
        # check if the word is longer than three letters (so that there's a middle to be scrambled)
        # and check if it contains one or more "word characters" (uppercase and lowecase letters, digits, underscores)
        # prefixing with r makes it a raw string, so that backslashes aren't interpreted as escape sequences
        # '\w+' is the regular expression
        # \w means word characters, and + means one or more
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]
    return word
    # if the checks fail, just return the word as-is
    ##################################################


# --------------------------------------------------
def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()
