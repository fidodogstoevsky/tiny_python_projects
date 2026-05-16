#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-26
Purpose: Rock the Casbah
"""

import argparse
import os
import io
import sys
import random
import re
import string
from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        nargs='*',
                        type=str)

    return parser.parse_args()

# --------------------------------------------------
def main():
    """do the work"""

    args = get_args()
    text = args.file.read().rstrip()

    matches = re.findall('(<([^<>]+)>)', text)

    if len(matches) == 0:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    if args.inputs:
        inputs = args.inputs
    else:
        inputs = []
        for placeholder, name in matches:
            article = 'an' if name[0] in 'aeiou' else 'a'
            word = input(f'Give me {article} {name}: ')
            inputs.append(word)

    while len(inputs) > 0:
        word = inputs.pop(0)
        text = re.sub('(<([^<>]+)>)', word, text, count=1)

    print(text)

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
