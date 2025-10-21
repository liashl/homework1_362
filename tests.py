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

    def test_001(self):
        """ Partition Testing: variable 'length': L < 10. Expects False """

        testcase = '760'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_002(self):
        """ Partition Testing: variable 'length': L > 19. Expects False. """

        testcase = '11111111111111111111111111111111111111111111111118'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_003(self):
        """ Partition Testing: variable 'length': 16 < L < 19. Expects False """

        testcase = '45674567456745676'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_004(self):
        """ Partition Testing: variable 'length': 10 < L < 15. Expects False """

        testcase = "3456345634563"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_005(self):
        """ Partition Testing: variable 'length': L = 15.
        Valid Checksum. Valid prefix. Expects True """

        testcase = "378937893789377"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_006(self):
        """ Partition Testing: variable 'length': L = 16. Valid Checksum.
        Valid prefix (4). Expects True """

        testcase = "4123412341234129"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_007(self):
        """ Partition Testing: variable 'length': L = 16
        Valid Checksum. Valid prefix (2222). Expects True """

        testcase = "2222222222222224"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_008(self):
        """ Partition Testing: variable 'length': L = 16
        Valid checksum. Valid prefix (53). Expects True """

        testcase = "5314531453145314"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_010(self):
        """ Partition Testing / Boundary case. Variable 'length':
        L = 16. Valid Checksum. Valid prefix (2221). Expects True """

        testcase = "2221987798769870"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_011(self):
        """ Partition testing / Boundary case. Variable 'length':
        L = 16. Valid checksum. Valid prefix (2720). Expects True """

        testcase = "2720887887887003"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_012(self):
        """ Partition testing / Boundary case. Variable 'length':
        L = 16. Valid checksum. Valid prefix (51). Expects True """

        testcase = "5151515151515155"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_013(self):
        """ Partition testing / Boundary case. Variable 'length':
        L = 16. Valid checksum. Valid prefix (55). Expects True """

        testcase = "5543554355435545"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_014(self):
        """ Partition testing / Boundary case. Variable 'length':
        L = 16. Invalid checksum. Valid prefix (55). Expects False """

        testcase = "5543554355435547"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_015(self):
        """ Partition testing: variable 'length': L = 15. variable 'prefix': 0 < P < 30.
        Expects False """

        testcase = '012345678901237'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_016(self):
        """ Partition Testing: variable 'length': L = 15. variable 'prefix': 30 < P < 34.
        Expects False """

        testcase = '301234567890125'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_017(self):
        """ Partition testing: variable 'length': L = 15. variable 'prefix': P = 34.
        Expects True """

        testcase = "345634563456342"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_018(self):
        """ Partition testing: variable 'length': L = 15. variable 'prefix': P = 37.
        Expects True """

        testcase = "372537253725379"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_019(self):
        """ Partition testing: variable 'length': L = 15. variable 'prefix': 34 < P < 37.
        Expects False """

        testcase = "367836783678364"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_020(self):
        """ Partition testing: variable 'length': L = 15. variable 'prefix': 37 < P < 40.
        Expects False """

        testcase = "389389389389386"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_021(self):
        """ Partition testing: variable 'length': L = 15. variable 'prefix': P > 40.
        Expects False """

        testcase = "999899989998990"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_022(self):
        """ Partition testing: variable 'length': L = 16.
            variable 'prefix': 2221 <= P <= 2720.
            Variable validity: V = False
            Expects False """

        testcase = '2221111111111111'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_023(self):
        """ Partition testing: variable 'length': L = 16
            variable 'prefix': 2221 <= P <= 2720.
            variable 'validity': V = True
            Expects True """

        testcase = "2222111111111160"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_024(self):
        """ Partition testing: variable 'length': L = 16
            variable 'prefix': P = 4
            variable 'validity': V = False
            Expects False """

        testcase = "4111111111111116"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_025(self):
        """ Partition testing: variable 'length': L = 16
            variable 'prefix': P = 4
            variable 'validity': V = True
            Expects True """

        testcase = "4111111111111111"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_026(self):
        """ Partition testing. variable 'validity': V = False.
            Variable 'length': L = 16.
            Variable 'prefix': 51 <= P <= 55.
            Expects False """

        testcase = "5201234567890127"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_027(self):
        """ Partition testing: variable 'length': L = 16.
            Variable 'prefix': 51 <= P <= 55.
            Expects True """

        testcase = "5201234567890125"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_028(self):
        """ Partition testing: variable 'length': L = 16.
            variable 'prefix': P > 55.
            Expects False """

        testcase = '7012345678902347'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_029(self):
        """ Partiion testing: variable 'length': L = 16. Variable 'prefix': P < 2221.
        Expects False """

        testcase = '1234123412341238'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_030(self):
        """ Partition testing: variable 'length': L = 16. Variable 'prefix': 2720 < P < 4.
        Expects False """

        testcase = '3579357935793579'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_031(self):
        """ Partition testing. variable 'length': L = 16.
            Variable 'prefix': 4 < P < 51
            variable 'validity': V = True.
            Expects False """

        testcase = '5012501250125012'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_032(self):
        """ Partition testing variable 'length': L = 16
            variable 'prefix': P > 55
            Expects False """

        testcase = '7891789178917899'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_033(self):
        """ Partition testing. Tests for an invalid 15-digit number that
        begins with the prefix 34. Expects False"""

        testcase = "340123456789012"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_034(self):
        """ Partition testing. Tests for a valid 15-digit number that begins with the prefix 34 """

        testcase = "340123456789014"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_035(self):
        """ Partition testing. Tests for an invalid 15-digit number that
        begins with the prefix 37. Expects False """

        testcase = "370123456789016"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_036(self):
        """ Partition testing. Tests for a valid 15-digit number that begins with the prefix 37 """

        testcase = "370123456789017"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_037(self):
        """ Edge case testing for an invalid 16-digit number beginning with the prefix 2221.
        Expects False """

        testcase = "2221012301230129"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_038(self):
        """ Edge case testing for valid 16-digit number beginning with the prefix 2221 """

        testcase = "2221012301230128"
        result = credit_card_validator(testcase)
        self.assertEqual(result, True)

    def test_039(self):
        """ Edge case testing for invalid 16-digit number beginning with the prefix 2720.
        Expects False """

        testcase = "2720012301230128"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_040(self):
        """ Edge case testing for valid 16-digit number beginning with the prefix 2720 """

        testcase = "2720012301230124"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_041(self):
        """ Test for valid prefix with incorrect length (4, 15 digits) """

        testcase = "411111111111116"
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_042(self):
        """ Test for valid prefix with incorrect length [51, 55] inclusive, 15 digits """

        testcase = '511111111111115'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_043(self):
        """ Test for valid prefix with incorrect length [2221-2720] inclusive, 15 digits """

        testcase = '222201230123016'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_044(self):
        """ Test for valid prefix 4 with invalid Luhn checksum (should be 0) """

        testcase = '4125687345680096'
        result = credit_card_validator(testcase)
        self.assertEqual(result, False)

    def test_045(self):
        """ Length == 15. Tests otherwise valid number with prefix less than 34.
        Expects False """

        testcase = '234523452345233'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_046(self):
        """ Length == 15. Tests otherwise valid number with prefix between 34 and 37 exclusive.
        Expects false """

        testcase = '357935793579356'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_047(self):
        """ Length == 15. Tests otherwise valid number with prefix greater than 37.
        Expects False. """

        testcase = '456745674567457'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_048(self):
        """ Length == 16. Prefix == 4. Luhn Sum == 0 """

        testcase = "4112411241124110"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_049(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 1 """

        testcase = "4235423542354231"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_050(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 2 """

        testcase = "4678432746784782"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_051(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 3 """

        testcase = "4367436743674363"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_052(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 4 """

        testcase = "4567198744277764"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_054(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 5 """

        testcase = "4789478947894785"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_055(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 6 """

        testcase = "4990499049904996"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_056(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 7 """

        testcase = "4321432143214327"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_057(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 8 """

        testcase = "4777777777777778"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_058(self):
        """ Tests Length == 16. Prefix == 4. Luhn Sum == 9 """

        testcase = "4204482779974829"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_059(self):
        """ tests Length == 16. Prefix == 4. Luhn Sum is invalid """

        testcase = "4204482779974828"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_060(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 0 """

        testcase = "5136666612384440"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_061(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 1 """

        testcase = "5100512513277121"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_062(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 2 """

        testcase = "5111111331111112"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_063(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 3 """

        testcase = "5177891729994853"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_064(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 4 """

        testcase = "5110085331119914"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_065(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 5 """

        testcase = "5100000000110005"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_066(self):
        """ Tests Length == 16. Prefix == 52. Luhn Sum is 6 """

        testcase = "5131166612384446"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_067(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 7 """

        testcase = "5123512351235127"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_068(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 8 """

        testcase = "5178517851785178"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_069(self):
        """ Tests Length == 16. Prefix == 51. Luhn Sum is 9 """

        testcase = "5199519951995199"
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_070(self):
        """ tests Length == 16. Prefix == 51. Luhn Sum is invalid. Expects False """

        testcase = "5199519951995190"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_071(self):
        """ Boundary testing. Lenght == 15. Prefix is 35. Checksum is Invalid """

        testcase = "356735673567356"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_072(self):
        """ Testing Length == 15. Prefix is 35. Checksum is valid """

        testcase = "356735673567351"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_073(self):
        """ Testing Length == 15. Prefix is 2720. Checksum is valid.
        Expects False because wrong prefix """

        testcase = "272056785678569"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_074(self):
        """ Testing Length == 15. Prefix is 51. Checksum is valid.
        Expects False because wrong prefix """

        testcase = "516751675167519"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_075(self):
        """ Testing Length == 15. Prefix is 4. Checksum is valid.
        Expects False because wrong prefix """

        testcase = "415641564156412"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_076(self):
        """ Testing Length == 15. Prefix is 55. Checksum is valid.
        Expects False because wrong prefix """

        testcase = "556755675567553"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_077(self):
        """ Testing Length = 16. Prefix is 34. Checksum is valid.
        Expects False because wrong prefix """

        testcase = "3456345634563458"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_078(self):
        """ Testing Length == 16. Prefix is 37. Checksum is valid.
        Expects False because wrong prefix """

        testcase = "3745374537453741"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_079(self):
        """ Error guessing: invalid checksum with valid prefix & length: visa """

        testcase = "4567456745674567"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_080(self):
        """ Error guessing: invalid checksum with valid prefix & length: mastercard (a) """

        testcase = "2221567856789876"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_081(self):
        """ Error guessing: invalid checksum with valid prefix and length: mastercard (b) """

        testcase = "5478547854785478"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_082(self):
        """ Error guessing: invalid checksum with valid prefix and length: amex (a) """

        testcase = "341111441155223"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_083(self):
        """ Error guessing: invalid checksum with valid prefix and length: amex (b) """

        testcase = "374537999999764"
        result = credit_card_validator(testcase)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
