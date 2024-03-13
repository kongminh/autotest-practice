# -*- coding: utf-8 -*-

'''
Common testing
'''

from seleniumbase import BaseCase
from com.practice.test_cases.common_test_cases import CommonTestCases
import logging
from config import Config
import pytest

@pytest.mark.skipif(Config.disable_doing, reason="Config")
class CommonTests(CommonTestCases):

    # @pytest.mark.run(order=100)
    # def test_case01(self):
    #     logging.info('test_case01 started')
    #     self.Login()

    # @pytest.mark.run(order=1000)
    # def test_case03(self):
    #     logging.info('test_case03 started')
    #     self.PopupTest()

    # @pytest.mark.run(order=100)
    # def test_case01(self):
    #     logging.info('test_case01 started')
    #     self.SignupTest()
    @pytest.mark.run(order=100)
    def test_case01(self):
        logging.info('test_case01 started')
        self.LoginTest()