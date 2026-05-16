#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-22
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
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = map(verse, range(1,args.num+1))
    print('\n\n'.join(verses), file=args.outfile)

# --------------------------------------------------
def verse(day):
    ordinal = ['first','second','third','fourth',
            'fifth','sixth','seventh','eighth',
            'ninth','tenth','eleventh','twelfth']

    gifts = ['A partridge in a pear tree.', 'Two turtle doves,',
    'Three French hens,', 'Four calling birds,', 'Five gold rings,',
    'Six geese a laying,', 'Seven swans a swimming,', 'Eight maids a milking,',
    'Nine ladies dancing,', 'Ten lords a leaping,', 'Eleven pipers piping,',
    'Twelve drummers drumming,']

    #####################################################
    ##### my solution (need to change "A" to "a" in partridge in gifts[0])
    # part1 = '\n'.join([
    #     f'On the {ordinal[day-1]} day of Christmas,',
    #     f'My true love gave to me,',
    # ])
    #     # On the second day of Christmas,
    #     # My true love gave to me,

    # part2 = '\n'.join([gifts[i] for i in reversed(range(1,day))])
    #     # Two turtle doves

    # part3 = f'A {gifts[0]}' if day == 1 else f'\nAnd a {gifts[0]}'
    #     # And a partridge in a pear tree

    # return part1 + '\n' + part2 + part3
    #####################################################

    #####################################################
    ##### Ken's solution
    lines = [f'On the {ordinal[day-1]} day of Christmas,',
             f'My true love gave to me,']
    
    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()


    return '\n'.join(lines)
    #####################################################

    

# --------------------------------------------------
def test_verse():
    assert verse(1) == '\n'.join([
    'On the first day of Christmas,', 'My true love gave to me,',
    'A partridge in a pear tree.'
    ])
    assert verse(2) == '\n'.join([
    'On the second day of Christmas,', 'My true love gave to me,',
    'Two turtle doves,', 'And a partridge in a pear tree.'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
