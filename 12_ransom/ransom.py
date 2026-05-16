#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-22
Purpose: Rock the Casbah
"""

import argparse
import random
import os
import sys
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
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
    text = args.text

    ################################################
    ##### approach 1: for loop, build char by char
    # new_text = []
    # for char in text:
    #     new_text += choose(char)
    ################################################

    ################################################
    ##### approach 2: list comp, join list to string
    # new_text = [choose(char) for char in text]
    ################################################

    ################################################
    ##### approach 3: map()
    new_text = map(choose, text)
    ################################################

    print(''.join(new_text))

# --------------------------------------------------
def choose(char):
    """ randomly choose to uppercase or lowercase the input letter """
    return char.upper() if random.choice([0,1]) else char.lower()

# --------------------------------------------------
def test_choose():
    """ a test to """
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)
        # random.seed(1) globally resets the state for the entire program
        # we don't want to interfere with the rest of the program when testing this function
        # so we save the state, change the seed, then reset to the original seed after testing

# --------------------------------------------------
if __name__ == '__main__':
    main()

