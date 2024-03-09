# -*- coding: utf-8 -*-

'''
Shipper test cases
'''

from seleniumbase import BaseCase
from com.cargolink.objects.common_objects import Common, LoginPage
from com.cargolink.objects.shipper_objects import CreateOrderPage as COPage,\
    ShipperMenuPage as ShipperMenu,\
    QuotationPage

class ShipperTestCases(BaseCase):

    def login(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.type(LoginPage.tel_box, LoginPage.tel_input)
        self.type(LoginPage.pass_box, LoginPage.pass_input)
        self.click(LoginPage.shipper_radio_btn)
        self.click(LoginPage.login_btn)
        pass

    def create_order(self):
        self.click(COPage.create_order_btn)
        Common.wait_loading(self)
        self.type(COPage.name_of_cargo, COPage.name_of_cargo_str)
        self.click(COPage.type_of_cargo)
        self.click(COPage.choose_cargo_type)
        self.type(COPage.amount_box, 5)
        self.click(COPage.type_of_truck)
        self.click(COPage.choose_truck_type)
        self.type(COPage.weight_box, 5)
        self.type(COPage.volume_box_6, 2)
        self.type(COPage.volume_box_7, 2)
        self.type(COPage.volume_box_8, 2)
        self.click(COPage.truck_not_share)
        self.click(COPage.button_1)

        self.type(COPage.load_location, COPage.load_location_str)
        self.click(COPage.choose_load_location)

        self.type(COPage.load_time, COPage.load_time_str)
        self.type(COPage.load_contact_name, COPage.load_contact_name_str)
        self.type(COPage.load_contact_mobile, COPage.load_contact_mobile_str)

        self.click(COPage.button_3)

        self.type(COPage.delivery_location, COPage.delivery_location_str)
        self.click(COPage.choose_delivery_location)

        self.type(COPage.delivery_contact_name, COPage.delivery_contact_name_str)
        self.type(COPage.delivery_contact_mobile, COPage.delivery_contact_mobile_str)

        #Save delivery info
        self.click(COPage.button_3)
        self.wait(1)

        self.type(COPage.valid_util_time, COPage.valid_util_time_str)
        self.type(COPage.expect_price, COPage.expect_price_value)

        self.click(COPage.send_btn)
        self.wait(1)
        pass

    def accept_quotation(self):
        self.click(ShipperMenu.transport_request_menu)
        Common.wait_loading(self)
        self.click(QuotationPage.quotation_tag)
        self.click(QuotationPage.first_quotation)
        Common.wait_loading(self)
        self.click(QuotationPage.accept_btn)
        Common.wait_animate(self)
        self.click(Common.ok_dialog_btn)
        pass
