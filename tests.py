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

    def test_0(self):
        """ Partition testing -- Length: Under Fourteen,
        Expects False """

        testcase = '0'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_1(self):
        """ Partition testing -- Length: Under Fourteen,
        Checksum: Invalid, Expects False """

        testcase = '4567890'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_1a(self):
        """ Partition testing -- Length: Under Fourteen,
        Checksum: Valid, Expects False """

        testcase = '4567897'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_2(self):
        """ Partition testing -- Length: More Than Seventeen,
        Checksum: Invalid, Expects False """

        testcase = '515151515151515151515151'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_2a(self):
        """ Partition testing -- Length: More Than Seventeen,
        Checksum: Valid, Expects False """

        testcase = '515151515151515151515157'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_3(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: Less Than 2221, Checksum: Valid,
        Expects False """

        testcase = '111156785678984'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_4(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: Less Than 2221, Checksum: Not Valid,
        Expects False """

        testcase = '111156785678983'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_5(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 2221 to 2720, Checksum: Valid,
        Expects False """

        testcase = '223356785678548'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_6(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 2221 to 2720, Checksum: Invalid,
        Expects False """

        testcase = '223356785678547'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_7(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 2720 to 33, Checksum: Valid,
        Expects False """

        testcase = '287654321387647'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_8(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 2720 to 33, Checksum: Invalid,
        Expects False """

        testcase = '287654321387645'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_9(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 34, Checksum: Valid, Expects True """

        testcase = '345634563456342'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_10(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 34, Checksum: Invalid, Expects False """

        testcase = '345634563456340'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_11(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 35-36, Checksum: Valid, Expects False """

        testcase = '367836783678364'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_12(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 35-36, Checksum: Invalid, Expects False """

        testcase = '367836783678365'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_13(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 37, Checksum: Valid, Expects True """

        testcase = '374537453745373'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_14(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 37, Checksum: Invalid, Expects False """

        testcase = '374537453745374'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_15(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 38-39, Checksum: Valid, Expects False """

        testcase = '393939393939396'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_16(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 38-39, Checksum: Invalid, Expects False """

        testcase = '393939393939399'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_17(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 4, Checksum: Valid, Expects False """

        testcase = '411111111111116'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_18(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 4, Checksum: Invalid, Expects False """

        testcase = '411111111111111'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_19(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 50, Checksum: Valid, Expects False """

        testcase = '500010005000108'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_20(self):
        """ Partition testing -- Length: Fiftenn,
        Prefix: 50, Checksum: Invalid, Expects False """

        testcase = '500010005000100'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_21(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 51-55, Checksum: Valid, Expects False"""

        testcase = '523452345234521'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_22(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 51-55, Checksum: Invalid, Expects False """

        testcase = '523452345234522'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_23(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 56 or greater, Checksum: Valid,
        Expects False """

        testcase = '578957895789579'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_24(self):
        """ Partition testing -- Length: Fifteen,
        Prefix: 57 or greater, Checksum: Invalid,
        Expects False """

        testcase = '578957895789578'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_25(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: Less than 2221, Checksum: Valid,
        Expects False """

        testcase = '1234123412341238'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_26(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: Less than 2221, Checksum: Invalid,
        Expects False """

        testcase = '1234123412341239'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_27(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 2221 to 2270, Checksum: Valid, Expects True """

        testcase = '2231223122312239'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_28(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 2221 to 2720, Checksum: Invalid, Expects False """

        testcase = '2231223122312237'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_29(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 2720 to 33, Checksum: Valid, Expects False """

        testcase = '3131313131313135'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_30(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 2720 to 33, Checksum: Invalid, Expects False """

        testcase = '3131313131313131'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_31(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 34, Checksum: Valid, Expects False """

        testcase = '3421786534217863'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_32(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 34, Checksum: Invalid, Expects False """

        testcase = '3421786534217862'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_33(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 35-36, Checksum: Valid, Expects False """

        testcase = '3674367436743670'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_34(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 35-36, Checksum: Invalid, expects False """

        testcase = '3674367436743673'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_35(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 37, Checksum: Valid, Expects False """

        testcase = '3755555555555550'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_36(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 37, Checksum: Invalid, Expects False """

        testcase = '3755555555555552'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_37(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 38-39, Checksum: Valid, Expects False """

        testcase = '3999999999999998'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_38(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 38-39, Checksum: Invalid, Expects False """

        testcase = '3999999999999999'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_39(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 4, Checksum: Valid, Expects True """

        testcase = '4112411241124110'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_40(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 4, Checksum: Invalid, Expects False """

        testcase = '4112411241124112'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_41(self):
        """ Partitiont testing -- Length: Sixteen,
        Prefix: 50, Checksum: Valid, Expects False """

        testcase = '5066506650665066'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_42(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 50, Checksum: Invalid,
        Expects False """

        testcase = '5066506650665068'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_43(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 51-55, Checksum: Valid,
        Expects True """

        testcase = '5467556755675564'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_44(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 51-55, Checksum: Invalid,
        Expects False """

        testcase = '5467556755675566'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_45(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 56 or greater, Checksum: Valid,
        Expects False """

        testcase = '5667556755675562'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_46(self):
        """ Partition testing -- Length: Sixteen,
        Prefix: 56 or greater, Checksum: Invalid,
        Expects False """

        testcase = '5667556755675563'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_47(self):
        """ Error guessing - testing prefix only """

        testcase = '4'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_48(self):
        """ Error guessing - testing prefix only """

        testcase = '34'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_49(self):
        """ Error guessing - testing prefix only """

        testcase = '37'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_50(self):
        """ Error guessing - testing prefix only """

        testcase = "2221"
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_51(self):
        """ Error guessing - testing prefix only """

        testcase = '2720'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_52(self):
        """ Error guessing - testing prefix only """

        testcase = '51'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_53(self):
        """ Error guessing - testing prefix only """

        testcase = '55'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_54(self):
        """ Error guessing - testing empty string """

        testcase = ''
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_55(self):
        """ Edge case testing - prefix 2221, 
        checksum: valid, length: 16, expects True """

        testcase = '2221000000000009'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_56(self):
        """ Edge case testing - prefix 2720, 
        checksum: valid, length: 16, expects True """

        testcase = '2720000000000005'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_57(self):
        """ Edge case testing - prefix 51,
        checksum: valid, length: 16, expects True """

        testcase = '5151515151515155'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_58(self):
        """ Edge case testing - prefix 55, 
        checksum: valid, length: 16, expects True """

        testcase = '5599999999999997'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_59(self):
        """ Edge case testing - checksum with high values
        checksum: valid, lenght: 16, prefix: 4, expects: True """

        testcase = '4999999999999996'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_60(self):
        """ edge case testing - checksum with low values
        checksum: valid, length: 16, prefix: 4, expects: True """

        testcase = '4000000000000002'
        result = credit_card_validator(testcase)
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()
