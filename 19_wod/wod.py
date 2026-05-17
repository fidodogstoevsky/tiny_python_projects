#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-05-17
Purpose: Rock the Casbah
"""

import argparse
import os
import io
import sys
import random
import re
import string
import csv
from pprint import pprint
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    wod = []
    exercises = read_csv(args.file)

    for name, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps/2)
        wod.append((name, reps))
    
    print(tabulate(wod, headers=('Exercise','Reps')))

    #### this is how I did it, but because of the seed it yields different results so tests fail
    # if args.easy:
    #     exercises = [(name, int(random.randint(low, high)/2)) for name,low,high in read_csv(args.file)]
    # else:
    #     exercises = [(name, random.randint(low, high)) for name,low,high in read_csv(args.file)]
    # print(tabulate(random.sample(exercises, k=args.num), headers=('Exercise', 'Reps')))

# --------------------------------------------------
def read_csv(fh):
    """read CSV input
    return list of dictionaries
    each dictionary's keys are column heads, and values are the value for that item
    example: say we have columns 'name' and 'age', storing 26 y.o. Amir and 24 y.o. Beth
    then we return [{'name': 'Amir', 'age': 26},{'name': 'Beth', 'age': 24}]"""
    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        low, high = int(reps.split('-')[0]), int(reps.split('-')[1])
        exercises.append((name, low, high))

    return exercises

# --------------------------------------------------
def test_read_csv():
    """test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]

# --------------------------------------------------
if __name__ == '__main__':
    main()
