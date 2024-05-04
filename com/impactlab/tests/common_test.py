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

        
    @pytest.mark.run(order=100)
    def test_case01(self):
        logging.info('Test Case 1: Register User')
        self.SignUpTest()
     
    

    # @pytest.mark.run(order=100)
    # def test_case02(self):
        # logging.info('Test Case 2: Login User with correct email and password')
        # self.SignUp_LoginTest()
        # self.Login_InputEmailPasswordTest()
        # self.DeleteAccTest()
      
    # @pytest.mark.run(order=100)
    # def test_case03(self):
        # logging.info('Test Case 3: Login User with incorrect email and password')
        # self.SignUp_LoginTest()
        # self.Login_InputEmailPasswordTest()
    
    # @pytest.mark.run(order=100)
    # def test_case04(self):
        # logging.info('Test Case 4: Logout User')
        # self.SignUp_LoginTest()
        # self.Login_InputEmailPasswordTest()
        # self.LogoutTest()

    # @pytest.mark.run(order=100)
    # def test_case05(self):     
        # logging.info('Test Case 5: Register User with existing email')
        # self.SignUp_LoginTest()
        # self.SignUp_InputNameAndEmailTest()
      
    