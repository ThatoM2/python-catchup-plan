from unittest import TestCase
from messi import goals

class TestGoals(TestCase):
    def test_cases(self):
        self.assertEqual(goals(2, 2, 5), 9)
        self.assertEqual(goals(50, 40, 13), 103)
        self.assertEqual(goals(1, 9, 7), 17)
