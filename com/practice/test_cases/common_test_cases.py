# -*- coding: utf-8 -*-

'''
Dxg test cases
'''

from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from com.practice.objects.common_objects import Common, LoginPage, PopupTestPage, RegisterTestPage, EnterAccountInforPage, AccountCreatedPage, HomePage, AccountDeletedPage, HomePage2, ContactUsPage, ProductsPage, CartPage, PopupAdded,DetailPage, PopupCheckout, AddressDetailsPage, PaymentPage
import pyperclip
import platform
import logging
import os


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
        self.click(HomePage2.signup_login_btn)
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
        self.click(HomePage2.signup_login_btn)
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
        self.click(HomePage2.signup_login_btn)
        self.type(LoginPage.email_input, LoginPage.email_value)
        self.type(LoginPage.password_input, LoginPage.password_value)
        self.click(LoginPage.login_btn)
        self.wait(10)
        pass
    
    def LogoutTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.signup_login_btn)
        self.type(LoginPage.email_input, LoginPage.email_value)
        self.type(LoginPage.password_input, LoginPage.password_value)
        self.click(LoginPage.login_btn)
        self.click(LoginPage.logout_btn)
        self.wait(10)
        pass
    
    def RegisterFail(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.signup_login_btn)
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
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = dir_path + '/../../../mock_pages/index.html'
        self.choose_file(ContactUsPage.file_input, file_path)
        self.click(ContactUsPage.submit_btn)
        self.switch_to_alert()
        self.accept_alert()
        self.wait(10)
        pass
    
    def VerifyTestcasePageTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.testcase_header_btn)
        self.wait(10)
        pass
    
    def ViewProductTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.product_btn)
        self.click(ProductsPage.viewproduct_btn)
        self.wait(10)
        pass
    
    def SearchProductTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.product_btn)
        self.type(ProductsPage.search_input, ProductsPage.search_value)
        self.click(ProductsPage.search_btn)
        self.wait(10)
        pass
    
    def SubscribeTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.scroll_to_bottom()
        self.type(HomePage2.subscription_input, HomePage2.subscription_value)
        self.click(HomePage2.subsciption_btn)
        self.wait(10)
        pass
    
    def SubscribeCartTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.cart_btn)
        self.scroll_to_bottom()
        self.type(CartPage.subscription_input, CartPage.subscription_value)
        self.click(CartPage.subsciption_btn)
        self.wait(10)
        pass
    
    def AddProductTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.product_btn)
        self.hover(ProductsPage.product1_hover)
        self.wait(1)
        self.click(ProductsPage.addproduct1_hover_btn)
        self.click(PopupAdded.countinue_btn)
        self.hover(ProductsPage.product2_hover)
        self.wait(1)
        self.click(ProductsPage.addproduct2_hover_btn)
        self.click(PopupAdded.viewcart_btn)
        self.wait(10)
        pass
    
    def VerifyProductQuantityInCartTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.viewproduct_btn)
        self.type(DetailPage.quantity_input, DetailPage.quantity_value)
        self.click(DetailPage.add_btn)
        self.click(PopupAdded.viewcart_btn)
        self.wait(10)
        pass
    
    def PlaceOrderRegisterWhileCheckoutTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(ProductsPage.addproduct1_hover_btn)
        self.click(PopupAdded.countinue_btn)
        self.click(HomePage2.cart_btn)
        self.click(CartPage.proceed_btn)
        self.click(PopupCheckout.register_textlink)
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
        self.click(HomePage2.cart_btn)
        self.click(CartPage.proceed_btn)
        self.type(AddressDetailsPage.comment_input, AddressDetailsPage.comment_value)
        self.click(AddressDetailsPage.payment_btn)
        self.type(PaymentPage.namecard_input, PaymentPage.namecard_value)
        self.type(PaymentPage.numbercard_input, PaymentPage.numbercard_value)
        self.type(PaymentPage.cvc_input, PaymentPage.cvc_value)
        self.type(PaymentPage.expirymonth_input, PaymentPage.expirymonth_value)
        self.type(PaymentPage.expiryyear_input, PaymentPage.expiryyear_value)
        self.click(PaymentPage.pay_btn)
        self.click(HomePage.delete_btn)
        self.click(AccountDeletedPage.continue_btn)
        self.wait(10)
        pass
    
    def PlaceOrderRegisterBeforeCheckoutTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.signup_login_btn)
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
        self.click(ProductsPage.addproduct1_hover_btn)
        self.click(HomePage2.cart_btn)
        self.click(CartPage.proceed_btn)
        self.type(AddressDetailsPage.comment_input, AddressDetailsPage.comment_value)
        self.click(AddressDetailsPage.payment_btn)
        self.type(PaymentPage.namecard_input, PaymentPage.namecard_value)
        self.type(PaymentPage.numbercard_input, PaymentPage.numbercard_value)
        self.type(PaymentPage.cvc_input, PaymentPage.cvc_value)
        self.type(PaymentPage.expirymonth_input, PaymentPage.expirymonth_value)
        self.type(PaymentPage.expiryyear_input, PaymentPage.expiryyear_value)
        self.click(PaymentPage.pay_btn)
        self.click(HomePage.delete_btn)
        self.click(AccountDeletedPage.continue_btn)
        self.wait(10)
        pass
    
    def PlaceOrderLoginBeforeCheckoutTest1(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(HomePage2.signup_login_btn)
        self.type(LoginPage.email_input, LoginPage.email_value)
        self.type(LoginPage.password_input, LoginPage.password_value)
        self.click(LoginPage.login_btn)
        self.click(ProductsPage.addproduct1_hover_btn)
        self.click(HomePage2.cart_btn)
        self.click(CartPage.proceed_btn)
        self.type(AddressDetailsPage.comment_input, AddressDetailsPage.comment_value)
        self.click(AddressDetailsPage.payment_btn)
        pass

    def PlaceOrderLoginBeforeCheckoutTest2(self):
        self.type(PaymentPage.namecard_input, PaymentPage.namecard_value)
        self.type(PaymentPage.numbercard_input, PaymentPage.numbercard_value)
        self.type(PaymentPage.cvc_input, PaymentPage.cvc_value)
        self.type(PaymentPage.expirymonth_input, PaymentPage.expirymonth_value)
        self.type(PaymentPage.expiryyear_input, PaymentPage.expiryyear_value)
        self.click(PaymentPage.pay_btn)
        self.click(HomePage.delete_btn)
        self.click(AccountDeletedPage.continue_btn)
        self.wait(10)
        pass
    
    def RemoveProductsFromCartTest(self):
        self.switch_to_default_window()
        self.open(Common.base_url)
        self.click(ProductsPage.addproduct1_hover_btn)
        self.click(PopupAdded.countinue_btn)
        self.click(HomePage2.cart_btn)
        self.click(CartPage.delete_btn)
        self.wait(10)
        pass
    
     
 