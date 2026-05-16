#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-14
Purpose: choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('thing',
                        metavar='thing',
                        help='thing spotted (i.e. octopus, narwhal, etc)')
    
    ###### OPTION 1: --side flag that defaults to larboard
    parser.add_argument('-s',
                        '--side',
                        help='side of the boat, larboard/starboard',
                        metavar='side',
                        type=str,
                        default='larboard')

    ###### OPTION 2: --starboard flag that changes the side to larboard
    # parser.add_argument('-s',
    #                     '--starboard',
    #                     help='change side to starboard (from larboard)',
    #                     action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    thing = args.thing
    
    ##### for OPTION 1
    side = args.side
    #####



    ##### for OPTION 2
    # strb = args.strb
    # if strb == '':
    #     side = 'larboard'
    # else:
    #     side = 'starboard'
    #####
    
    ##### for case matching of article, i.e. "An Octopus"
    # if word[0].isupper():
    #     article = 'An' if thing[0].lower() in 'aeiou' else 'A' 
    # else:
    #     article = 'an' if thing[0].lower() in 'aeiou' else 'a' 

    article = 'an' if thing[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {thing} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
