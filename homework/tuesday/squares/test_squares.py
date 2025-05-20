from unittest import TestCase
from squares import squares

class TestSquares(TestCase):
    def test_cases(self):
        self.assertEqual(squares(2), 4)
        self.assertEqual(squares(50), 2500)
        self.assertEqual(squares(1), 1)

