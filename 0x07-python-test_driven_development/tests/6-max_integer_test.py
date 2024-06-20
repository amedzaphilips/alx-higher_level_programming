#!/usr/bin/env python3

""" This is a module that uses unittest """

import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_max_integer(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_unordered_list(self):
        """ Test case for unordered list """
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_ordered_list(self):
        """" Test case for ordered list """
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)


if __name__ == "__main__":
    unitttest.main()
