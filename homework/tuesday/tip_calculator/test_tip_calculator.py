from unittest import TestCase
from tip_calculator import dollars_to_float, percent_to_float

class TestTipCalculator(TestCase):
    def test_dollars_to_float(self):
        self.assertEqual(dollars_to_float("$39.99"), 39.99)
        self.assertEqual(dollars_to_float("$50.00"), 50.0)
        self.assertEqual(dollars_to_float("$4.67"), 4.67)

    def test_percent_to_float(self):
        self.assertEqual(percent_to_float("15%"), 0.15)
        self.assertEqual(percent_to_float("82.3%"), 0.823)
        self.assertEqual(percent_to_float("50%"), 0.5)
