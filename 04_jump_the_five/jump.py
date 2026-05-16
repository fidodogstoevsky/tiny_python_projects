#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text (phone #)')

    parser.add_argument('-w',
                    '--write',
                    help='Sort the items',
                    action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5',
    }

    writer = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero',
        '-': ','
    }

    args = get_args()

    ### for loop
    # encrypted = ''
    # for char in args.text:
    #     encrypted += jumper.get(char, char)

    # print(encrypted)

    ### list comp
    encrypted = ''.join([jumper.get(char, char) for char in args.text])

    ### str.translate()
    #encrypted = args.text.translate(str.maketrans(jumper))
    # print(encrypted)

    written = ''
    for char in range(len(args.text)):
        enc_char = jumper.get(args.text[char], args.text[char])
        written += writer.get(enc_char, enc_char)
        if char < len(args.text)-1: # check if it's not the last char
            if args.text[char] in writer and args.text[char+1] not in '-':
                written += ' '

    # written = ''
    # for char in args.text:
    #     enc_char = jumper.get(char, char)
    #     written += writer.get(enc_char, enc_char)
    #     if char in writer:
    #         written += ' '

    if args.write:
         print(written)
    else:
         print(encrypted)

# --------------------------------------------------


# --------------------------------------------------
if __name__ == '__main__':
    main()
