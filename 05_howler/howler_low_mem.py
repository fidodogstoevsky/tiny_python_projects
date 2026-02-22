#!/usr/bin/env python3
"""
low-memory howler
"""

import argparse
import os
import io
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

    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        # if args.text is a file, replace it
        # with an open file handle for it
        args.text = open(args.text)
    elif os.path.isdir(args.text):
        # if args.text is a directory
        pass
    else:
        # otherwise, replace it with an io.StringIO()
        # this value acts like an open file handle
        args.text = io.StringIO(args.text + '\n')
    
    return args




# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    for line in args.text:
        # read the input line by line
        # regardless of if the initial input was a filename or text
        # they're now both formatted as io.StringIO() values
        # so we can loop through and read each line
        out_fh.write(line.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
