#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = './jump.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """test"""

    rv, out = getstatusoutput(f'{prg} 123-456-7890')
    assert rv == 0
    assert out == '987-604-3215'


# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(f'{prg} "That number to call is 098-765-4321."')
    assert rv == 0
    assert out.rstrip() == 'That number to call is 512-340-6789.'

# --------------------------------------------------
def test_num_to_string():
    """ check if numbers are encoded into strings """

    for flag in ['-w', '--write']:
        rv, out = getstatusoutput(f'{prg} {flag} "That number to call is 098-765-4321."')
        assert rv == 0
        assert out.rstrip() == 'That number to call is five one two, three four zero, six seven eight nine.'
        #assert out.rstrip() == 'That number to call is five one two three four zero six seven eight nine.'