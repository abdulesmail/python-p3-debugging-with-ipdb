#!/usr/bin/env python3

import ipdb

def plus_two(num):
    result = num + 2
    return result

def test_plus_two():
    assert plus_two(3) == 5

# Run the test function
test_plus_two()
