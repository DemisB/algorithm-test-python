import unittest
from check_parenthesis_consistency import check_parenthesis_consistency


class TestCheckParenthesisConsistency(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(check_parenthesis_consistency("()"))

    def test_case_2(self):
        self.assertTrue(check_parenthesis_consistency("(())"))

    def test_case_3(self):
        self.assertTrue(check_parenthesis_consistency("()()"))

    def test_case_4(self):
        self.assertFalse(check_parenthesis_consistency("(()"))

    def test_case_5(self):
        self.assertFalse(check_parenthesis_consistency("())"))

    def test_case_6(self):
        self.assertFalse(check_parenthesis_consistency("((()"))

    def test_case_7(self):
        self.assertFalse(check_parenthesis_consistency("())))"))

    def test_case_8(self):
        self.assertFalse(check_parenthesis_consistency("()))((()"))

