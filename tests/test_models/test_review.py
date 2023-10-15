#!/usr/bin/python3
"""
    This module defines edge cases for review.py.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class Test Review."""

    def test_review_func(self):
        """Tests the class Review."""
        self.review = Review()

    def test_placeID_func(self):
        """Tests the placeID in the review."""
        self.assertEqual(self.review.placeID, "")

        self.review.placeID = "051"
        self.assertEqual(self.review.placeID, "051")

    def test_userID_func(self):
        """Tests the userID in the review."""
        self.assertEqual(self.review.userID, "")

        self.review.userID = "046"
        self.assertEqual(self.review.userID, "046")

    def test_textinput_func(self):
        """Tests whether input is text."""
        self.assertEqual(self.review.text, "")

        self.review.text = "Lovely place by the beach"
        self.assertEqual(self.review.text, "Lovely place by the beach)


if __name__ == '__main__':
    unittest.main()
