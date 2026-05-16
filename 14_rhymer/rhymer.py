#!/usr/bin/env python3
"""
Author : gidonkaminer <gidonkaminer@localhost>
Date   : 2026-02-23
Purpose: Rock the Casbah
"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    clusters = """bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl
    sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ
    str thr"""

    prefixes = sorted([c for c in string.ascii_lowercase if c not in 'aieou'] + clusters.split())

    if stemmer(args.word)[1] == '':
        print(f'Cannot rhyme "{args.word}"')
    else:
        for prefix in prefixes:
            if prefix != stemmer(args.word)[0]:
                print(prefix + stemmer(args.word)[1])
    
    # Ken's solution uses a list comp thjat does a similar thing
    # print('\n'.join(sorted([p + rest for p in prefixes if p != start])))

# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word
    input: a word (str)
    output: start, rest of word
    """
    consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aieou'])

    # we could also write this with filter() as follows
    # consonants = ''.join(filter(lambda c: c not in vowels, string.ascii_lowercase))
    # like map(), filter() takes two arguments: a function and an iterable
    # for filter, it has to be a function that returns a boolean
    # the function is lambda c: c not in vowels, a function that takes c and returns True if it's not a vowel and False otherwise
    # applying the boolean function to each item in the list of letters, it filters out all the False items (all the vowels)
    # so filter returns a list of only consonants
    
    vowels = 'aeiou'

    pattern = (
        f'([{consonants}]+)?' # capture one or more initial consonants (optional)
        f'([{vowels}])'       # capture at least one vowel
        '(.*)'                # capture zero or more of anything
    )

    match = re.match(pattern, word.lower())
    # re.match is a function that takes a regex and a text
    # and searches for a match in the text (beginning at the start)

    if match:
    # a match was found
        p1 = match.group(1) or ''
        # the word starts with a consonant
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
    # no match was found, i.e. there are no vowels anywhere in the word
        return (word, '')

# --------------------------------------------------
def test_stemmer():
    """test stemmer"""
    assert stemmer('') == ('','')
    # the empty string's stem is the empty string
    assert stemmer('cake') == ('c','ake')
    # a word with a single leading consonant has that consonant as its stem
    assert stemmer('chair') == ('ch', 'air')
    # a word with a leading consonant cluser
    assert stemmer('APPLE') == ('', 'apple')
    # a word starting with a vowel has no leading consonant
    # also, checks if it works for uppercase
    assert stemmer('RDNZL') == ('rdnzl', '')
    # a word with no vowels has the entire leading consonant
    assert stemmer('123') == ('123', '')
    # same for something that isn't a word



# --------------------------------------------------
if __name__ == '__main__':
    main()