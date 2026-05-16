#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-15
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-e',
                        '--ee',
                        help='lowercase the input instead',
                        action='store_true')


    ##### Ken's solution
    # args = parser.parse_args()
    # if os.path.isfile(args.text):
    #     args.text = open(args.text).read().rstrip()
    # # if args.text is the name of an existing file,
    # # overwrite its value with the results of reading the file
    # return args
    #####

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    # READING
    if os.path.isfile(args.text): 
        # if the positional argument is a filename, read that file
        text = open(args.text).read()
    else:
        # otherwise the text is just the positional argument itself
        text = args.text

    # WRITING
    if args.ee:
        text = text.lower()
    else:
        text = text.upper()


    if args.outfile:
        # if the outfile flag is up, write to that file
        out_fh = open(args.outfile, 'wt')
        out_fh.write(text+'\n')
        out_fh.close()
    else:
        # otherwise just write to the terminal
        print(text)

    ##### Ken's solution
    # args = get_args()
    # out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    # # if out is flagged, write to the output file. otherwise, write to terminal
    # out_fh.write(args.text.upper() + '\n')
    # out_fh.close()
    #####

# --------------------------------------------------
if __name__ == '__main__':
    main()
