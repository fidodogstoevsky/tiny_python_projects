#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-16
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    parser.add_argument('-l',
                        '--lines',
                        help='Only show line count',
                        action='store_true')

    parser.add_argument('-w',
                        '--words',
                        help='Only show word count',
                        action='store_true')

    parser.add_argument('-c',
                        '--characters',
                        help='Only show character count',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # args.file is a list of file handles

    tot_lines, tot_words, tot_bytes = 0, 0, 0

    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_words += len(str.split(line))
            num_bytes += len(line)
        tot_lines += num_lines
        tot_words += num_words
        tot_bytes += num_bytes
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')
    
    if len(args.file)>1:
        print(f'{tot_lines:8}{tot_words:8}{tot_bytes:8} total')

    

# --------------------------------------------------
if __name__ == '__main__':
    main()
