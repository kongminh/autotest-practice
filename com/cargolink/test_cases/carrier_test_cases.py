# -*- coding: utf-8 -*-

'''
Carrier test cases
'''

from seleniumbase import BaseCase
from com.cargolink.objects.common_objects import Common, LoginPage
from com.cargolink.objects.carrier_objects import CreateQuotationPage as QuotationPage

class CarrierTestCases(BaseCase):

    def login(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.type(LoginPage.tel_box, LoginPage.tel_input)
        self.type(LoginPage.pass_box, LoginPage.pass_input)
        self.click(LoginPage.carrier_radio_btn)
        self.click(LoginPage.login_btn)
        pass

    def create_quotation(self):
        self.click(QuotationPage.create_quotation_btn)
        Common.wait_loading(self)
        self.click(QuotationPage.quotation_btn)
        self.type(QuotationPage.fee_box, QuotationPage.quote_price_value)
        self.type(QuotationPage.valid_until_box, QuotationPage.valid_util_time_str)
        self.click(Common.send_btn)
        pass
