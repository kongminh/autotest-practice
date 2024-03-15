# -*- coding: utf-8 -*-

'''
Dxg test cases
'''

from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from com.practice.objects.common_objects import Common, LoginPage, PopupTestPage, RegisterTestPage, EnterAccountInforPage, AccountCreatedPage, HomePage, AccountDeletedPage, HomePage2, ContactUsPage
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
        self.click(RegisterTestPage.signup_btn)
        self.type(RegisterTestPage.name_input, RegisterTestPage.name_value)
        self.type(RegisterTestPage.email_input, RegisterTestPage.email_value)
        self.click(RegisterTestPage.submit_btn)
        self.click(EnterAccountInforPage.mrs_radio)
        self.type(EnterAccountInforPage.password_input, EnterAccountInforPage.password_value)
        self.click(EnterAccountInforPage.day_select, EnterAccountInforPage.day_value)
        self.click(EnterAccountInforPage.month_select, EnterAccountInforPage.month_value)
        self.click(EnterAccountInforPage.year_select, EnterAccountInforPage.year_value)
        self.click(EnterAccountInforPage.signup_checkbox)
        self.click(EnterAccountInforPage.receive_checkbox)
        self.type(EnterAccountInforPage.firstname_input, EnterAccountInforPage.firstname_value)
        self.type(EnterAccountInforPage.lastname_input, EnterAccountInforPage.lastname_value)
        self.type(EnterAccountInforPage.company_input, EnterAccountInforPage.company_value)
        self.type(EnterAccountInforPage.address1_input, EnterAccountInforPage.address1_value)
        self.type(EnterAccountInforPage.address2_input, EnterAccountInforPage.address2_value)
        self.click(EnterAccountInforPage.country_select, EnterAccountInforPage.country_value)
        self.type(EnterAccountInforPage.state_input, EnterAccountInforPage.state_value)
        self.type(EnterAccountInforPage.city_input, EnterAccountInforPage.city_value)
        self.type(EnterAccountInforPage.zipcode_input, EnterAccountInforPage.zipcode_value)
        self.type(EnterAccountInforPage.mobile_input, EnterAccountInforPage.mobile_value)
        self.click(EnterAccountInforPage.create_submit)
        self.click(AccountCreatedPage.continue_btn)
        self.click(HomePage.delete_btn)
        self.click(AccountDeletedPage.continue_btn)
        self.wait(10)
        pass
    
    def LoginTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(RegisterTestPage.signup_btn)
        self.type(LoginPage.email_input, LoginPage.email_value)
        self.type(LoginPage.password_input, LoginPage.password_value)
        self.click(LoginPage.login_btn)
        self.click(HomePage.delete_btn)
        self.click(AccountDeletedPage.continue_btn)
        self.wait(10)
        pass
    
    def LoginTest_fail(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(RegisterTestPage.signup_btn)
        self.type(LoginPage.email_input, LoginPage.email_value)
        self.type(LoginPage.password_input, LoginPage.password_value)
        self.click(LoginPage.login_btn)
        self.wait(10)
        pass
    
    def LogoutTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(RegisterTestPage.signup_btn)
        self.type(LoginPage.email_input, LoginPage.email_value)
        self.type(LoginPage.password_input, LoginPage.password_value)
        self.click(LoginPage.login_btn)
        self.click(LoginPage.logout_btn)
        self.wait(10)
        pass
    
    def RegisterFail(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(RegisterTestPage.signup_btn)
        self.type(RegisterTestPage.name_input, RegisterTestPage.name_value)
        self.type(RegisterTestPage.email_input, RegisterTestPage.email_value)
        self.click(RegisterTestPage.submit_btn)
        self.wait(10)
        pass
      
    def ContactUsTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.contact_btn)
        self.type(ContactUsPage.name_input, ContactUsPage.name_value)
        self.type(ContactUsPage.email_input, ContactUsPage.email_value)
        self.type(ContactUsPage.subject_input, ContactUsPage.subject_value)
        self.type(ContactUsPage.message_input, ContactUsPage.message_value)
        self.click(ContactUsPage.submit_btn)
        self.wait(10)
        pass
    
    def VerifyTestcasePageTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.testcase_header_btn)
        self.wait(10)
        pass