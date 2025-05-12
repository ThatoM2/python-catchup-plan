from unittest import TestCase
from messi import messi

class TestMessi(TestCase):
    def basic_test_cases(self):
        self.assertEqual(messi(2, 2, 5), 9)
        self.assertEqual(messi(50, 40, 13), 103)
        self.assertEqual(messi(1, 9, 7), 17)
