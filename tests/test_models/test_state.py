#!/usr/bin/python3
"""
    This module defines the edge cases for state.py.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class TestState has the tests for class TestStatw."""

    def test_state_func(self):
        """Tests the State."""
        self.state = State()

    def test_input_func(self):
        """Tests the input/name of State."""
        self.assertEqual(self.state.name, "")

        self.state.name = "Nevada"
        self.assertEqual(self.state.name, "Nevada")


if __name__ == '__main__':
    unittest.main()
