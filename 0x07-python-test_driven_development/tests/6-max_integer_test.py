#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        liststring = ['holberton', 'school', 'python']
        self.assertEqual(max_integer(liststring), 'school')

    def test_dict(self):
        liststring = [{'holberton':1, 'school':3, 'python':8}, \
            {'holberton':1, 'school':3, 'python':8}]
        with self.assertRaises(TypeError):
            max_integer(liststring)

    def test_float(self):
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 4.3)
        self.assertEqual(max_integer([1.3, 1.8, 2.9]), 2.9)

    def test_strin(self):
        self.assertIsInstance(max_integer([1, 2, 3, 4]), int)

if __name__ == "__main__":
    unittest.main()
