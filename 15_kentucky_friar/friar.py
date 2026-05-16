#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-24
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import io
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        ##### using map()
        print(''.join(map(fry, re.split(r'(\W+)', line))))
        ##### using a list comp
        # print(''.join([fry(word) for word in re.split(r'(\W+)', line)]))
        ##### using a for loop
        # wordlist = []
        # for word in re.split(r'(\W+)', line):
        #     wordlist += fry(word)
        # print(''.join(wordlist))

# --------------------------------------------------
def fry(word):
    """ drop g from -ing words, change you to y'all """
    ######################################
    ##### with regex
    you_pattern = (
        '([Yy])' # character class is [Yy], and we want to capture it
        # so it's enclosed in parentheses
        'ou' # the next two letters have to match as well, but we don't
        # care about capturing them
        '$' # anchor the expression to the end of the string
        # so the ou has to be the end of the string, it can't be 'your'
    ) # so we find 'You' or 'you', and capture the first char Y/y
    you = re.match(you_pattern, word)
    # pattern is '([Yy])ou$', we re.match because we want to start
    # only at the beginning of a word

    ing_pattern = (
        '(.+)' # . means any character, + means arbitrarily many
        # characters, and they're enclosed () so we capture everything
        'ing' # that arbitrary sequence needs to be followed by ing
        '$' # the ing must be the end of the string
    ) # so we find any string ending in ing, and capture the part before the ing
    ing = re.search(ing_pattern, word)
    # pattern is '(.+)ing$', we re.match because we want to start
    # anywhere in the middle of a word (we're looking for ing)

    if you:
        # the word is 'you' or 'You'
        return you.group(1) + "'all"
            # we captured [Yy], so take whichever one we captured and
            # append 'all to it
    elif ing:
        # the word ends in 'ing'
        first = ing.group(1)
            # select the first part of the match (i.e. everything before the ing)
        if re.search('[aieou]', first, re.IGNORECASE):
            # if there's a vowel in that first part (i.e. it's a two-syllable word like 'fishing')
            return ing.group(1) + "in'"
                # we captured fish, so append in' to it
        else:
            # otherwise it's a one-syllable ing word like "swing"
            return word
                # so we just return it
    else:
        return word
            # if the word is neither you nor ends in ing,
            # we don't do anything to it
    ######################################

    ######################################
    ##### without regex
    # # for you -> y'all
    # if word.lower() == 'you':
    #     return word[0] + "'all"
    # # for -ing -> -in'
    # if word.endswith('ing'):
    #     if any(map(lambda c: c.lower() in 'aeiouy', word[:-3])):
    #           return word[:-1] + "'"
    #     else:
    #           return word
    # return word
    ######################################

# --------------------------------------------------
def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"

# --------------------------------------------------
if __name__ == '__main__':
    main()
