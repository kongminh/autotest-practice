# -*- coding: utf-8 -*-

'''
Dxg test cases
'''

from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from com.practice.objects.common_objects import Common, LoginPage, PopupTestPage, SignupPage
import pyperclip
import platform
import logging


class CommonTestCases(BaseCase):

    def Login(self):
        self.switch_to_default_window()
        # self.open(Common.login_url)
        # self.type(LoginPage.username_box, LoginPage.username_input)
        # self.type(LoginPage.password_box, LoginPage.password_input)
        # self.click(LoginPage.login_btn)
        self.wait(1)
        pass

    def PopupTest(self):
        self.switch_to_default_window()
        self.open(PopupTestPage.popup_base_url)
        self.click(PopupTestPage.popup3_btn)
        self.switch_to_default_window()
        self.click(PopupTestPage.popup1_btn)
        self.switch_to_default_window()
        self.click(PopupTestPage.popup2_btn)
        for window in self.driver.window_handles:
            if window != self.driver.window_handles[0]:
                self.switch_to_window(window)
                title = self.get_text(PopupTestPage.popup_title)
                popup_id = title[-1]
                self.type(PopupTestPage.text_input, 'Nội dung cho popup ' + popup_id)
                #self.driver.close()
        self.wait(10)
        pass
    
    def SignupTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(SignupPage.signup_btn)
        self.wait(5)
        pass