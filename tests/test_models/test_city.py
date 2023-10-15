#!/usr/bin/python3
"""
    This module defines the edge cases of city.py.
"""

import unittest
from models.city import City
from models.base_model import BaseModel
import models


class TestCity(unittest.TestCase):
    """Tests the class City."""

    def test_city_func(self):
        """Tests the City."""
        self.city = City()

    def test_stateID_func(self):
        """Tests the state for which the city is situate."""
        self.assertEqual(self.city.state_id, "")

        self.city.stateID = "007"
        self.assertEqual(self.city.stateID, "007")

    def test_city_func(self):
        """Tests the input that is the name of the city."""
        self.assertEqual(self.city.name, "")

        self.city.name = "Paris"
        self.assertEqual(self.city.name, "Paris")


if __name__ == '__main__':
    unittest.main()
