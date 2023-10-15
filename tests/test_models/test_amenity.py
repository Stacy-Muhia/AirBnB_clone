#!/usr/bin/python3
"""
    This module defines the edge cases for amenity.py.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class testing class Amenity."""

    def test_amenities_func(self):
        """Tests the amenities."""
        self.amenity = Amenity()

    def test_input_func(self):
        """Tests the inputs for amenities."""
        pass


if __name__ == '__main__':
    unittest.main()
