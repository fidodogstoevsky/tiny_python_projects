#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-18
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import io
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--filenames',
                        help='Input file(s)',
                        nargs='?',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default='2')

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not args.adjectives > 0:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if not args.number > 0:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)

    adj_list="""
    bankrupt base caterwauling corrupt cullionly
    detestable dishonest false filthsome filthy
    foolish foul gross heedless indistinguishable
    infected insatiate irksome lascivious lecherous
    loathsome lubbery old peevish rascaly rotten
    ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.split()

    noun_list="""
    Judas Satan ape ass barbermonger beggar block
    boy braggart butt carbuncle coward coxcomb cur
    dandy degenerate fiend fishmonger fool gull harpy
    jack jolthead knave liar lunatic maw milksop
    minion ratcatcher recreant rogue scold slave swine
    traitor varlet villain worm
    """.split()

    if arg.filenames:
        if len(arg.filenames) == 1:
            pass
        else:
            pass
    else:
        # if 
        nouns = noun_list
        adjectives = adj_list


    for _ in range(args.number):
        chosen_adj = random.sample(adjectives, args.adjectives)
        chosen_noun = random.choice(nouns)
        print(f'You {', '.join(chosen_adj)} {chosen_noun}!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
