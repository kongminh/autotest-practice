# -*- coding: utf-8 -*-

'''
Dxg test cases
'''

from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from com.new_project.objects.common_objects import Common, LoginPage, RegisterTestPage, InputAccountInforPage, HomePage
from selenium import webdriver
import pyperclip
import platform
import logging
import os


class CommonTestCases(BaseCase):
    def get_new_driver(self, *args, **kwargs):
      options = webdriver.ChromeOptions()
      options.set_capability('unhandledPromptBehavior', 'ignore')
      if self.headless:
            options.add_argument("--headless")
      return webdriver.Chrome(options=options)

    
    def SignUp_LoginTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage.signup_login_btn)
        pass

    def SignUp_InputNameAndEmailTest(self):
        self.type(RegisterTestPage.name_input, RegisterTestPage.name_value)
        self.type(RegisterTestPage.email_input, RegisterTestPage.email_value)
        self.click(RegisterTestPage.submit_btn)
        pass

    def SignUp_InputPersonalInforTest(self):
        self.click(InputAccountInforPage.mrs_radio)
        self.type(InputAccountInforPage.password_input, InputAccountInforPage.password_value)
        self.type(InputAccountInforPage.day_select, InputAccountInforPage.day_value)
        self.type(InputAccountInforPage.month_select, InputAccountInforPage.month_value)
        self.type(InputAccountInforPage.year_select, InputAccountInforPage.year_value)
        self.click(InputAccountInforPage.signup_checkbox)
        self.click(InputAccountInforPage.receive_checkbox)
        self.type(InputAccountInforPage.firstname_input, InputAccountInforPage.firstname_value)
        self.type(InputAccountInforPage.lastname_input, InputAccountInforPage.lastname_value)
        self.type(InputAccountInforPage.company_input, InputAccountInforPage.company_value)
        self.type(InputAccountInforPage.address1_input, InputAccountInforPage.address1_value)
        self.type(InputAccountInforPage.address2_input, InputAccountInforPage.address2_value)
        self.type(InputAccountInforPage.country_select, InputAccountInforPage.country_value)
        self.type(InputAccountInforPage.state_input, InputAccountInforPage.state_value)
        self.type(InputAccountInforPage.city_input, InputAccountInforPage.city_value)
        self.type(InputAccountInforPage.zipcode_input, InputAccountInforPage.zipcode_value)
        self.type(InputAccountInforPage.mobile_input, InputAccountInforPage.mobile_value)
        self.click(InputAccountInforPage.create_submit)
        pass

    
    def Login_InputEmailPasswordTest(self):
        self.type(LoginPage.email_input, LoginPage.email_value)
        self.type(LoginPage.password_input, LoginPage.password_value)
        self.click(LoginPage.login_btn)
        pass
    
   