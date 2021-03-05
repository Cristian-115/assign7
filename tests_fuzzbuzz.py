import unittest
import fuzzbuzz

class TestCase(unittest.TestCase):
    def test_Fizz(self):
        self.assertEqual(fuzzbuzz.Fuzzbuzz(), 1)
        