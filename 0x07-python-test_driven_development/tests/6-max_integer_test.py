#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    class for tests max integer
    """
    def test_max_integer_pos(self):
        """
        normal behavor in positiv elements
        """
        given_list = [2, 3, 5, 9]
        self.assertEqual(max_integer(given_list), max(given_list))

    def test_max_integer_ntv(self):
        """
        negative elements
        """
        given_list = [2, 3, -5, -9]
        self.assertEqual(max_integer(given_list), max(given_list))

    def test_max_integer_raise(self):
        """
        TypeError
        """
        given_list = [2, "str", 5, 9]
        self.assertRaises(TypeError, max_integer, given_list)

    def test_max_integer_empty(self):
        """
        empty list
        """
        given_list = []
        self.assertEqual(max_integer(given_list), None)
