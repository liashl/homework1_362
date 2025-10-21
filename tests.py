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

    def test_55a(self):
        """ Edge case testing - prefix 2221,
        checksum: invalid, length: 16, expects False """

        testcase = '2221000000000007'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_55b(self):
        """ Edge case testing - prefix 2221,
        checksum: valid, length: 15, expects False """

        testcase = '222100000000000'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_56(self):
        """ Edge case testing - prefix 2720,
        checksum: valid, length: 16, expects True """

        testcase = '2720000000000005'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_56a(self):
        """ Edge case testing - prefix 2720,
        checksum: invalid, length: 16, expects False """

        testcase = '2720000000000003'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_56b(self):
        """ Edge case testing - prefix 2720,
        checksum: valid, length: 15, expects False """

        testcase = '272000000000001'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_57(self):
        """ Edge case testing - prefix 51,
        checksum: valid, length: 16, expects True """

        testcase = '5151515151515155'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_57a(self):
        """ Edge case testing - prefix 51,
        checksum: invalid, length: 16, expects False """

        testcase = '5151515151515153'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_57b(self):
        """ Edge case testing - prefix 51,
        checksum: valid, length: 15, expects False """

        testcase = '515151511515156'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_58(self):
        """ Edge case testing - prefix 55,
        checksum: valid, length: 16, expects True """

        testcase = '5599999999999997'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_58a(self):
        """ Edge case testing - prefix 55,
        checksum: invalid, length: 16, expects False """

        testcase = '5599999999999999'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_58b(self):
        """ Edge case testing - prefix 55,
        checksum: valid, length: 15, expects False """

        testcase = '559999999999996'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_59(self):
        """ Edge case testing - checksum with high values
        checksum: valid, length: 16, prefix: 4, expects: True """

        testcase = '4999999999999996'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_60(self):
        """ edge case testing - checksum with low values
        checksum: valid, length: 16, prefix: 4, expects: True """

        testcase = '4000000000000002'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    def test_61(self):
        """ Error guessing - two things should generate False,
        length: 16, prefix: 33, checksum: False """

        testcase = '3333333333333333'
        result = credit_card_validator(testcase)
        self.assertTrue(result)

    """ ---------- Extended testing ----------- """

    def test_62(self):
        """ Extended partition testing - Length: under 14,
        prefix: less than 2221, checksum: valid """

        testcase = '11121118'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_63(self):
        """ Extended partition testing - Length: under 14,
        prefix: less than 2221, checksum: invalid """

        testcase = '11121117'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_64(self):
        """" Extended partition testing - length: under 14,
        prefix: 2221 to 2720, checksum: valid """

        testcase = '2222222222'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_65(self):
        """ Extended partition testing - length: under 14,
        prefix: 2221 to 2720, checksum: invalid """

        testcase = '2222222225'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_66(self):
        """ Extedned partition testing - length: under 14,
        prefix: 2720 to 33, checksum: valid """

        testcase = '3111111187'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_67(self):
        """ Extended partition testing - length: under 14,
        prefix: 2720 to 33, checksum: invalid """

        testcase = '3111111188'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_68(self):
        """ Extended partition testing - length: under 14,
        prefix: 34, checksum: valid """

        testcase = '3467876326'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_69(self):
        """ Extended partition testing - length: under 14,
        prefix: 34, checksum: invalid """

        testcase = '3467876327'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_70(self):
        """ Extended partition testing - length: under 14
        prefix: 35-36, checksum: valid """

        testcase = '3535353530'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_71(self):
        """ Extended partition testing - length: under 14,
        prefix: 35-36, checksum: invalid """

        testcase = '3535353536'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_72(self):
        """ Extended partition testing - length: under 14,
        prefix: 37, checksum: valid """

        testcase = '3799999994'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_73(self):
        """ Extended partition testing - length: under 14,
        prefix: 37, checksum: invalid """

        testcase = '3799999999'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_74(self):
        """ Extended partition testing - length: under 14,
        prefix: 38-39, checksum: valid """

        testcase = '38888888880'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_75(self):
        """ Extended partition testing - length: under 14,
        prefix: 38-39, checksum: invalid """

        testcase = '38888888881'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_76(self):
        """ Extended partition testing - length: under 14,
        prefix: 4, checksum: valid """

        testcase = '444444444442'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_77(self):
        """ Extended partition testing - length: under 14,
        prefix: 4, checksum: invalid """

        testcase = '444444444444'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_78(self):
        """ Extended partition testing - length: under 14,
        prefix: 50, checksum: valid """

        testcase = '500000000009'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_79(self):
        """ Extended partition testing - length: under 14,
        prefix: 50, checksum: invalid """

        testcase = '500000000008'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_80(self):
        """ Extended partition testing - length: under 14,
        prefix: 51-55, checksum: valid """

        testcase = '5252525257'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_81(self):
        """ Extended partition testing - length: under 14,
        prefix: 51-55, checksum: invalid """

        testcase = '5252525258'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_82(self):
        """ Extended partition testing - length: under 14,
        prefix: over 56, checksum: valid """

        testcase = '889988998890'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_83(self):
        """ Extended partition testing - length: under 14,
        prefix: over 56, checksum: invalid """

        testcase = '889988998893'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_84(self):
        """ Edge case testing - length: 14,
        prefix: 34, checksum: valid """

        testcase = '34555555555559'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_85(self):
        """ Edge case testing - length: 14,
        prefix: 37, checksum: valid """

        testcase = '37893789378978'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_86(self):
        """ Extended partition testing - length: 17 or more,
        prefix: less than 2221, checksum: valid """

        testcase = '22202220222022208'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_87(self):
        """ Extended partition testing - length: 17 or more,
        prefix: less than 2221, checksum: invalid """

        testcase = '22202220222022209'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_88(self):
        """ Extended partition testing: length: 17 or more,
        Prefix: 2221 to 2720, checksum: valid """

        testcase = '22222222222222222'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_89(self):
        """ Extended partition testing: length: 17 or more,
        Prefix: 2221 to 2720, checksum: invalid """

        testcase = '22222222222222226'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_90(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 2720 to 33, checksum: valid """

        testcase = '27211111111111111'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_91(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 2720 to 33, checksum: invalid """

        testcase = '27211111111111114'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_92(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 34, checksum: valid """

        testcase = '34555555555555557'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_93(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 34, checksum: invalid """

        testcase = '34555555555555558'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_94(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 35-36, checksum: valid """

        testcase = '36563656365636564'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_95(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 35-36, checksum: invalid """

        testcase = '36563656365636567'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_96(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 37, checksum: valid """

        testcase = '37888888888888887'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_97(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 37, checksum: invalid """

        testcase = '37888888888888888'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_98(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 38-39, checksum: valid """

        testcase = '39999999999999992'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_99(self):
        """ Extended partition testing - length: 17 or more, 
        prefix: 38-39, checksum: invalild """

        testcase = '39999999999999995'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_100(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 4, checksum: valid """

        testcase = '44444444444444444'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_101(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 4, checksum: invalid """

        testcase = '44444444444444441'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_102(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 50, checksum: valid """

        testcase = '50015001500150012'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_103(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 51, checksum: invalid """

        testcase = '50015001500150015'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_104(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 51-55, checksum: valid """

        testcase = '52525252525252528'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_105(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 51-55, checksum: invalid """

        testcase = '52525252525252529'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_106(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 56 or more, checksum: valid """

        testcase = '89896666909077776'
        result = credit_card_validator(testcase)
        self.assertFalse(result)

    def test_107(self):
        """ Extended partition testing - length: 17 or more,
        prefix: 56 or more, checksum: invalid """

        testcase = '89896666909077778'
        result = credit_card_validator(testcase)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
