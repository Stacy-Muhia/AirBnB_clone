#!/usr/bin/python3
"""
    This module is defining the edge cases for place.py.
"""

import unittest
from models.place import Place
import models


class TestPlace(unittest.TestCase):
    """Class Test Place that will be testing cases in place.py."""

    def test_place_func(self):
        """Tests the class Place."""
        self.place = Place()

    def test_place_attributes_func(self):
        """Tests Place checking against the features/
        that will have the features of a place. """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, "")
        self.assertEqual(self.place.number_bathrooms, "")
        self.assertEqual(self.place.max_guest, "")
        self.assertEqual(self.place.latitude, "")
        self.assertEqual(self.place.longitude, "")
        self.assertEqual(self.place.price_by_night, "")
        self.assertEqual(self.place.amenity_ids, "")

    def test_placeinput_func(self):
        """Tests that the features of Place have been entered accordingly."""
        self.place.cityID = "051"
        self.place.userID = "007"
        self.place.name = "Diani Villas"
        self.place.description = "Beachfront"
        self.place.number_rooms = 5
        self.place.number_bathrooms = 3
        self.place.max_guest = 10
        self.place.price_by_night = 199
        self.place.latitude = 39.5947
        self.place.longitude = 4.2798
        self.place.amenity_ids = ["amen_01", "amen_02"]

        self.assertEqual(self.place.cityID, "051")
        self.assertEqual(self.place.userID, "007")
        self.assertEqual(self.place.name, "Diani Villas")
        self.assertEqual(self.place.description, "Beachfront")
        self.assertEqual(self.place.number_rooms, 5)
        self.assertEqual(self.place.number_bathrooms, 3)
        self.assertEqual(self.place.max_guest, 10)
        self.assertEqual(self.place.price_by_night, 199)
        self.assertEqual(self.place.longitude, 39.5947)
        self.assertEqual(self.place.latitude, 4.2798)
        self.assertEqual(self.place.amenity_ids, ["amen_01", "amen_02"])


if __name__ == '__main__':
    unittest.main()
