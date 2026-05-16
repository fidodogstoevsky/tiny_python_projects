#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-19
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import io
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-i',
                    '--insertions',
                    help='Percent insertions',
                    metavar='insertions',
                    type=float,
                    default=0)

    parser.add_argument('-d',
                    '--deletions',
                    help='Percent deletions',
                    metavar='deletions',
                    type=float,
                    default=0)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        # check if the input is a filename
        args.text = open(args.text).read().strip()
            # if it is, read the file

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    random.seed(args.seed)
    len_text = len(text)

    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
        # list of characters from which we choose replacements

    num_mutations = round(len(text) * args.mutations)
        # number of characters to change (i.e. percent of text to change times length of text, rounded)


    #############################################################################
    ##### aproach 1: text as string
    # new_text = text
    #   # make a copt of the original text
    # for i in random.sample(range(len_text), num_mutations):
    #     # generate indices and loop through them
    #     new_char = random.choice(alpha.replace(new_text[i], ''))
    #         # get the new character by choosing from one of the options in alpha
    #         # and replace the current character with a blank space (get rid of it)
    #         # string.replace() returns a copy of the string, doesn't modify original
    #     new_text = new_text[:i] + new_char + new_text[i + 1:]
    #         # assemble the new text by taking everything before the new character,
    #         # the new character, and everything after
    # print(f'You said: "{text}"\nI heard : "{new_text}"')
    #############################################################################

    #############################################################################
    # ##### approach 2: text as list
    # new_text = list(text)
    #     # make a copy of the original text, as a list of characters
    # for i in random.sample(range(len_text), num_mutations):
    #         # randomly choose some indices at which to mutate, loop through them
    #     new_text[i] = random.choice(alpha.replace(new_text[i], ''))
    #         # at each index, change that char to a random one in alpha without the char in question
    # print(f'You said: "{text}"\nI heard : "{''.join(new_text)}"')
    #     # join the new list without intervening characters, to make a new string
    #############################################################################

    #############################################################################
    ##### going further 1: mutations to randomly selected words
    # new_text = text.split()
    #     # split the text along spaces, so new_text is a list of words in text
    # num_mutations = round(len(new_text) * args.mutations)
    #     # number of words to change
    # for word in random.sample(range(len(new_text)), num_mutations):
    #     # randomly choose at which indices to mutate, loop through them
    #     new_text[word] = ''.join(random.choices(alpha, k=len(new_text[word])))
    #         # at each index at which the word should be changed, replace it with
    #         # a string of random letters the same length as the original word
    # print(f'You said: "{text}"\nI heard : "{' '.join(new_text)}"')
    ############################################################################

    #############################################################################
    # ##### going further 2: insertions and deletions
    new_text = list(text)
        # make a copy of the original text, as a list of characters
    for i in random.sample(range(len_text), num_mutations):
            # randomly choose some indices at which to mutate, loop through them
        new_text[i] = random.choice(alpha.replace(new_text[i], ''))
            # at each index, change that char to a random one in alpha without the char in question
    print(f'You said: "{text}"\nI heard : "{''.join(new_text)}"')
        # join the new list without intervening characters, to make a new string
    #############################################################################

# --------------------------------------------------
if __name__ == '__main__':
    main()
