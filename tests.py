"""
Name: Lia Launtz
Email: launtza@oregonstate.edu
Course: CS 362 - Software Engineering II
Assignment: Homework 1 - Black Box Testng
Due Date: October 20, 2025

"""
import unittest
from credit_card_validator import credit_card_validator


class BlackBoxTest(unittest.TestCase):
    """ Searching for errors in the implementation of credit card verification function """

    def test_01(self):
        """ Partition Test for strings of credit card numbers greater than 16 digits in length """

        testcase = '01234567890123456'
        result = credit_card_validator(testcase)
        self.assertEqual(result,False)


    def test_02(self):
        """ 
        Partition Test for strings of credit card numbers less than 15 digits in length
        Expects False
        """

        testcase = '01234567890123' 
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_03(self):
        """ Tests for 16-number credit card strings that do not start with 4, 51-55, or 2221-2720 inclusive """

        testcase = '7012345678902345'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_04(self):
        """ Tests for a 15-number credit card string that does not start with 34 or 37"""

        testcase = '012345678901234'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_05(self):
        """ Tests for a 15-digit number credit card string that starts with 3 but not with 34 or 37 """

        testcase = '301234567890123'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_06(self):
        """ Tests for a 16-digit number between 2221 and 2720 inclusive that fails the Luhn checksum test"""

        testcase = '222111111111111'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_07(self):
        """ Tests for each prefix range """

        testcase = "2222111111111163"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
