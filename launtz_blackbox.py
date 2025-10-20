"""
Name: Lia Launtz
Email: launtza@oregonstate.edu
Course: CS 362 - Software Engineering II
Assignment: Homework 1 - Black Box Testng
Due Date: October 20, 2025

"""
import unittest

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
        self.assertEqual(result,False)


if __name__ == '__main__':
    unittest.main()