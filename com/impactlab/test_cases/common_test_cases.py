# -*- coding: utf-8 -*-

'''
Dxg test cases
'''

from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from com.impactlab.objects.common_objects import Common, Signup
from selenium import webdriver
import pyperclip
import platform
import logging
import os


class CommonTestCases(BaseCase):
    # # upload file 
    # def get_new_driver(self, *args, **kwargs):
    #   options = webdriver.ChromeOptions()
    #   options.set_capability('unhandledPromptBehavior', 'ignore')
    #   if self.headless:
    #         options.add_argument("--headless")
    #   return webdriver.Chrome(options=options)

    
    def SignUpTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(Common.signup_btn)
        self.type(Signup.email_input, Signup.email_value)
        self.type(Signup.password_input, Signup.password_value)
        self.click(Signup.continue_btn)
        pass

    