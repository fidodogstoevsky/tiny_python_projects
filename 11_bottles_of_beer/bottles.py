#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    parser.add_argument('-w',
                        '--written',
                        help='Replace Arabic numerals with written text',
                        action='store_true')

    args = parser.parse_args()

    if args.num:
        if not args.num > 0:
            parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    ##############################################
    ##### my solution
    # for bottle in range(args.num, 0, -1):
    #     print(verse(bottle))
    ##############################################

    ##############################################
    ##### solution 1.1: with map()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))
        # map takes a function and an iterable
        # the function is verse
        # the iterable is a list in descending order
    ##############################################

    ##############################################
    ##### solution 1.2: for loop (verse solution 1)
    # for bottle in range(args.num, 0, -1):
    #     print(verse(bottle), end='\n' * (2 if bottle > 1 else 1))
    #         # we need to add a newline at the end of each
    #         # verse, except for the last (so the verses
    #         # are separated by newlines
    #         # so rather than doing it in verse, we can
    #         # check for it here
    ##############################################

    ##############################################
    ##### solution 1.3: list comp (verse solution 1)
    # verses = [verse(n) for n in range(args.num, 0, -1)]
    # print('\n\n'.join(verses))
    #   # whether in the for loop or list comp, we're just
    #   # repeatedly applying a function to elements in a list
    #   # so might as well do it with map()
    ##############################################



# --------------------------------------------------
def verse(num):
    """sing a verse"""

    ##############################################
    ##### my solution
    # if num == 1:
    #     return '\n'.join([
    #     '1 bottle of beer on the wall,',
    #     '1 bottle of beer,',
    #     'Take one down, pass it around,',
    #     'No more bottles of beer on the wall!'])
    # else:
    #     if num == 2:
    #         plural = ''
    #     else:
    #         plural = 's'
    #     return '\n'.join([
    #         f'{num} bottles of beer on the wall,',
    #         f'{num} bottles of beer,',
    #         'Take one down, pass it around,',
    #         f'{num-1} bottle{plural} of beer on the wall!\n'])
    ##############################################

    ##############################################
    ##### Ken's solution: with map()
    ##### also including going further exercises
    # to_text = ['one', 'two', 'three', 'four', 'five',
    # 'six','seven','eight','nine']

    next_num = num-1
    s1 = '' if num == 1 else 's'
    s2 = '' if next_num == 1 else 's'
        # no plural s if there's just one, pluralize if several
    end = 'No more' if next_num == 0 else next_num
    return '\n'.join([
        f'{num} bottle{s1} of beer on the wall,',
        f'{num} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{end} bottle{s2} of beer on the wall!',])
    ##############################################

# --------------------------------------------------
# def test_verse():
#     """Test verse"""
#     last_verse = verse(1)
#     assert last_verse == '\n'.join([
#     '1 bottle of beer on the wall,', '1 bottle of beer,',
#     'Take one down, pass it around,',
#     'No more bottles of beer on the wall!'])

#     two_bottles = verse(2)
#     assert two_bottles == '\n'.join([
#     '2 bottles of beer on the wall,', '2 bottles of beer,'
#     ,'Take one down, pass it around,',
#     '1 bottle of beer on the wall!'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
