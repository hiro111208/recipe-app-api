"""
Sample test cases for the app
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)
