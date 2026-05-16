#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-18
Purpose: Rock the Casbah
"""

import argparse
import os
import io
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        default='a',
                        #choices=['a','e','i','o','u']
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        # if args.text is a file, replace it
        # with an open file handle for it
        # then read the file and strip it
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    ### MY SOLUTION
    # text = args.text
    # vowel = args.vowel
    # replacements = {'a': vowel.lower(), 'e': vowel.lower(),
    # 'i': vowel.lower(), 'o': vowel.lower(), 'u': vowel.lower(),
    # 'A': vowel.upper(), 'E': vowel.upper(),
    # 'I': vowel.upper(), 'O': vowel.upper(), 'U': vowel.upper()}

    # for line in text:
    #     print(line.translate(str.maketrans(replacements)))
    ###

    ######################################################
    ###### method 1: iterate through every character
    # text = args.text
    # vowel = args.vowel
    # new_text = ''
    # for char in text:
    #     if char in 'aieou':
    #         new_text += vowel.lower()
    #     elif char in 'AIEOU':
    #         new_text += vowel.upper()
    #     else:
    #         new_text += char
    # print(new_text)
    ######################################################

    ######################################################
    ##### method 2: str.replace()
    # text = args.text
    # vowel = args.vowel
    # for v in 'aieou':
    #     text = text.replace(v.lower(), vowel.lower())
    #     # replace each lowercase vowel with the lowercase vowel from input
    #     text = text.replace(v.upper(), vowel.upper())
    #     # same for uppercase
    # print(text)
    ######################################################

    ######################################################
    ##### method 3: str.translate()
    # vowel = args.vowel
    # trans = str.maketrans('aeiouAEIOU', vowel.lower()*5 + vowel.upper()*5)
    # text = args.text.translate(trans)
    # print(text)
    ######################################################

    ######################################################
    ##### method 4: list comp
    # vowel = args.vowel
    # text = [vowel.lower() if c in 'aeiou'
    #         else vowel.upper() if c in 'AEIOU'
    #         else c for c in args.text]
    # print(''.join(text))
    ######################################################

    ######################################################
    ##### method 5: list comp with function
    # vowel = args.vowel
    # def new_char(c):
    #     return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    # text = ''.join([new_char(c) for c in args.text])
    # print(text)
    ######################################################

    ######################################################
    ##### method 6: map()
    # vowel = args.vowel
    # text = map(
    #     # map() takes a function as its first argument and
    #     # an iterable (list) as its second argument
    #     lambda c: vowel.lower() if c in 'aeiou'
    #     else vowel.upper() if c in 'AEIOU' else c,
    #         # first argument: an anonymous function that
    #         # takes a character c and returns the corresponding
    #         # character, either replaced or not
    #     args.text)
    #         # second argument: the string (taken as a list)
    # print(''.join(text))
    # # map returns a new list, so we join it
    ######################################################

    ######################################################
    ##### method 7: map() with named function
    # vowel = args.vowel

    # def new_char(c):
    #     return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    # print(''.join(map(new_char, args.text)))
    # # map uses new_char without parentheses. It's not CALLING
    # # it, it's just APPLYING it to the iterable
    # # map takes each character from the text and calls
    # # new_char witht that character as an argument
    ######################################################

    ######################################################
    ##### method 8: regular expressions
    # import re
    # text = args.text
    # vowel = args.vowel
    # text = re.sub('[aeiou]', vowel, text)
    # # re.sub takes three arguments:
    # # 1. pattern of letters for which to do the replacement
    # # 2. thing to replace them with
    # # 3. text in which to do the replacement
    # text = re.sub('[AEIOU]', vowel.upper(), text)
    # print(text)
    ######################################################

    ######################################################
    ##### going further
    vowel = args.vowel
    text = map(
        # map() takes a function as its first argument and
        # an iterable (list) as its second argument
        lambda c: vowel.lower() if c in 'aeiou'
        else vowel.upper() if c in 'AEIOU' else c,
            # first argument: an anonymous function that
            # takes a character c and returns the corresponding
            # character, either replaced or not
        args.text)
            # second argument: the string (taken as a list)
    print(''.join(text))
    # map returns a new list, so we join it
    ######################################################




# --------------------------------------------------
if __name__ == '__main__':
    main()
