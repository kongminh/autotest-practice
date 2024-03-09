# -*- coding: utf-8 -*-

'''
CarrierCreateFreightOffer test cases
'''

from selenium.webdriver.common.by import By
from com.cargolink.objects.common_objects import Common
from com.cargolink.objects.carrier.create_fo_objects import CreateFreightOfferPage as OfferPage
from com.cargolink.test_cases.carrier_test_cases import CarrierTestCases

class CarrierCreateFreightOffer(CarrierTestCases):

    def create_freight_offer(self):
        Common.wait_loading_show(self)
        Common.wait_loading(self)
        self.click('//*[@id="carriers"]//span[contains(text(), "Tạo xe tìm hàng")]')
        Common.wait_loading(self)
        self.click(Common.send_btn)
        # self.click("(//*[@id='new-shipment']//div[contains(@class, 'q-field__control-container')])[1]/..")
        # self.assert_element("(//*[@id='new-shipment']//div[contains(@class, 'q-field__control-container')])[1]/div")

        self.assert_element(".inner-newrequest > div > div:nth-child(1) > div:nth-child(1) .q-field--error", timeout=1)
        self.assert_text_visible(u"Đề nghị nhập Số đăng ký xe",
                                 selector=".inner-newrequest > div > div:nth-child(1) > div:nth-child(1) .q-field__messages",
                                 timeout=1)
        # self.assert_element("div:has(> input[tabindex='2']) nth-child(2)")
        # self.assert_element("input")

        # self.assert_element('div', timeout=1)
        # self.assert_element('.q-field--error[2]', timeout=1)
        # self.assert_element('//*[@id="new-shipment"]/div[1]/div[2]/div/div/div[1]/div[1]/label/div/div[2]/div', timeout=1)
        # self.assert_text_visible("Đề nghị nhập Số đăng ký xe", '//*[@id="new-shipment"]/div[1]/div[2]/div/div/div[1]/div[1]/label/div/div[2]/div', timeout=1)

        # elem = self.find_element('//*[@id="new-shipment"]/div[1]/div[2]/div/div/div[1]/div[1]/label/div/div[2]/div')
        # assert elem.text == u"Đề nghị nhập  Số đăng ký xe"


        # self.find_element()
        # elem = self.get_element("(//*[@id='new-shipment']//div[contains(@class, 'q-field__control-container')])[1]")
        # self.highlight("(//*[@id='new-shipment']//div[contains(@class, 'q-field__control-container')])[1]/../../../../label[contains(@class, 'q-field--error')]")
        # self.assert_element(OfferPage.truck_label_error, timeout=1)
        self.wait(1)
        pass
