#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """ checks if the file exists """

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """ checks if the program outputs usage instructions """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """ brigantine -> a brigantine """

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """ Brigantine -> a Brigantine """

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('a', word.title())


# --------------------------------------------------
def test_vowel():
    """ octopus -> an octopus """

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """ Octopus -> an Octopus """

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('an', word.upper())

# --------------------NEW TESTS---------------------

# # --------------------------------------------------
# def test_consonant_upper_article():
#     """ Brigantine -> A Brigantine """

#     for word in consonant_words:
#         out = getoutput(f'{prg} {word.title()}')
#         assert out.strip() == template.format('A', word.title())

# # --------------------------------------------------
# def test_vowel_upper_article():
#     """ Octopus -> an Octopus """

#     for word in vowel_words:
#         out = getoutput(f'{prg} {word.upper()}')
#         assert out.strip() == template.format('An', word.upper())

