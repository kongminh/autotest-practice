# -*- coding: utf-8 -*-

'''
Dxg test cases
'''

from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from com.impactlab.objects.common_objects import Common, Signup, Login, Fund
from selenium import webdriver
import pyperclip
import platform
import logging
import os


class CommonTestCases(BaseCase):

    def SignUpTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(Common.signup_btn)
        self.type(Signup.email_input, Signup.email_value)
        self.type(Signup.password_input, Signup.password_value)
        self.click(Signup.continue_btn)
        pass

    def LoginTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(Common.login_btn)
        self.type(Login.email_input, Login.email_value)
        self.click(Login.continue_btn)
        self.type(Login.password_input, Login.password_value)
        self.click(Login.continue_btn)
        self.wait_for_element_present(Login.profile_avatar_img)
        pass

    def FundListTest(self):
        self.LoginTest()
        self.click(Fund.fund_list_btn)
        self.wait(2)
        pass

    def SubscribeFundTest(self):
        self.FundListTest()
        self.wait_for_element_present(Fund.fund_1st_btn)
        self.click(Fund.donate_now_btn)
        # self.click(Fund.fund_1st_btn)
        # self.wait_for_element_present(Fund.donation_match_txt)
        # self.click(Fund.donate_btn)
        
        # self.type(Fund.add_tip_input, Fund.add_tip_value)
        # self.click(Fund.add_tip_btn)
        self.wait(5)
        pass
