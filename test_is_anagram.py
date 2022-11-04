import unittest
from is_anagram import is_anagram


class TestCheckParenthesisConsistency(unittest.TestCase):
    def test_case_1(self):
        self.assertFalse(is_anagram("pouet", "prout"))

    def test_case_2(self):
        self.assertTrue(is_anagram("abc", "bca"))

    def test_case_3(self):
        self.assertTrue(is_anagram("abbc", "bcba"))

    def test_case_4(self):
        self.assertFalse(is_anagram("abbc", "cba"))

    def test_case_5(self):
        self.assertFalse(is_anagram("abbc", ""))

    def test_case_6(self):
        self.assertTrue(is_anagram("", ""))
