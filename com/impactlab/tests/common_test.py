# -*- coding: utf-8 -*-

'''
Common testing
'''

from seleniumbase import BaseCase
from com.impactlab.test_cases.common_test_cases import CommonTestCases
import logging
from config import Config
import pytest

@pytest.mark.skipif(Config.disable_doing, reason="Config")
class CommonTests(CommonTestCases):

    # @pytest.mark.run(order=100)
    # def test_case01(self):
    #     logging.info('Test Case 1: Register User')
    #     self.SignUpTest()

    # @pytest.mark.run(order=101)
    # def test_case02(self):
    #     logging.info('Test Case 2: Login')
    #     self.LoginTest()

    # @pytest.mark.run(order=102)
    # def test_case03(self):
    #     logging.info('Test Case 3: Fund list')
    #     self.FundListTest()

    @pytest.mark.run(order=103)
    def test_case04(self):
        logging.info('Test Case 4: Subscribe Fund')
        self.SubscribeFundTest()
