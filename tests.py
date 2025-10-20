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

    def test_01a(self):
        """ Tests very short invalid number """

        testcase = '000'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_01b(self): 
        """ Test very long invalid number """

        testcase = '11111111111111111111111111111111111111111111111111'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_01(self):
        """ Test for otherwise valid number greater than 16 digits in length. Expects False """

        testcase = '01234567890123452'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_02(self):
        """ Test for otherwise valid number less than 15 digits in length. Expects False """

        testcase = '01234567890128'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_03(self):
        """ Tests for otherwise valid 16-digit number with prefix > 55. Expects False """

        testcase = '7012345678902347'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_04(self):
        """ Tests for an otherwise valid 15-digit string that does not start with a 3. Expects False """

        testcase = '012345678901237'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_05(self):
        """ Tests for otherwise valid 15-digit string that starts with 3 but not with 34 or 37. Expects False """

        testcase = '301234567890125'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_06(self):
        """ Tests for invalid 16-digit number with prefix between 2221 and 2720 inclusive """

        testcase = '222111111111111'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_07(self):
        """ Tests for valid 16-digit numbers with prefix between [2221-2720] inclusive """

        testcase = "2222111111111160"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_08_a(self):
        """ Tests for invalid 16-digit number beginning with a 4"""

        testcase = "4111111111111116"
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)


    def test_08(self):
        """ Tests for valid 16-digit numbers beginning with 4 """

        testcase = "4111111111111111"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_09(self):
        """ Tests for an invalid 16-digit number beginning with prefix [51-55] inclusive. Expects False """

        testcase = "5201234567890127"
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_10(self):
        """ Tests for valid 16-digit numbers beginning with prefix [51-55] inclusive """

        testcase = "5201234567890125"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_11_a(self):
        """ Tests for an invalid 15-digit number that begins with the prefix 34. Expects False"""

        testcase = "340123456789012"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_11(self):
        """ Tests for a valid 15-digit number that begins with the prefix 34 """

        testcase = "340123456789014"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_12_a(self):
        """ Tests for an invalid 15-digit number that begins with the prefix 37. Expects False """

        testcase = "370123456789016"
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_12(self):
        """ Tests for a valid 15-digit number that begins with the prefix 37 """

        testcase = "370123456789017"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_13_a(self):
        """ Edge case testing for an invalid 16-digit number beginning with the prefix 2221. Expects False """

        testcase = "2221012301230129"
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_13(self):
        """ Edge case testing for valid 16-digit number beginning with the prefix 2221 """

        testcase = "2221012301230128"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_14_a(self):
        """ Edge case testing for invalid 16-digit number beginning with the prefix 2720. Expects False """

        testcase = "2720012301230128"
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_14(self):
        """ Edge case testing for valid 16-digit number beginning with the prefix 2720 """

        testcase = "2720012301230124"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_15(self):
        """ Test for valid prefix with incorrect length (4, 15 digits) """

        testcase = "411111111111116"
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_16(self):
        """ Test for valid prefix with incorrect length [51, 55] inclusive, 15 digits"""

        testcase = '511111111111115'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_17(self):
        """ Test for valid prefix with incorrect length [2221-2720] inclusive, 15 digits """

        testcase = '222201230123016'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_19(self):
        """ Test for valid prefix 4 with invalid Luhn checksum (should be 0) """

        testcase = '4125687345680096'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
