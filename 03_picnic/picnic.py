#!/usr/bin/env python3
"""
Author : gidonkaminer
Date   : 2026-02-15
Purpose: picnic list
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnick game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-p',
                    '--punc',
                    help='punctuation for separating list items',
                    metavar='punc',
                    type=str,
                    default=',')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('-o',
                        '--oxford',
                        help='Remove the oxford comma',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        part1 = f'{args.punc} '.join(items[:-1])
        part2 = f'{args.punc} and ' + items[-1] if not args.oxford else ' and ' + items[-1]
        bringing = part1 + part2

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
