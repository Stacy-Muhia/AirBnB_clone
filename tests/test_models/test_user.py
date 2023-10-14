#!/usr/bin/python3
"""
    This module is testing the edge cases for user.py.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class TestUser has the tests for class User."""

    def test_user_func(self):
        """ This is testing the class User."""
        self.user = User()

    def test_input_func(self):
        """ Tests the input of the class User."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_assigned_input_func(self):
        """ Tests for assigned values of attributes """
        self.user.email = "roronoa@email.com"
        self.user.password = "password"
        self.user.first_name = "Muzan"
        self.user.last_name = "Kibutsuji"

        self.assertEqual(self.user.email, "roronoa@email.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "Muzan")
        self.assertEqual(self.user.last_name, "Kibutsuji")


if __name__ == '__main__':
    unittest.main()
