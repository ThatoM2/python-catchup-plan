from unittest import TestCase
from indoor import indoor

class TestIndoor(TestCase):
    def basic_test_cases(self):
        self.assertEqual(indoor("HEY!!"), "hey!!")
        self.assertEqual(indoor("Hey, How is it going?"), "hey, how is it going?")
        self.assertEqual(indoor("STOP"), "stop")
