# -*- coding: utf-8 -*-

'''
Carrier page objects
'''

from com.cargolink.objects.shipper_objects import CreateOrderPage as COPage

class CreateFreightOfferPage(object):
    create_offer_btn = "//*[@id='shippers']/div/header/div/div/a/button"
    truck_label_error = "//*[@id='new-shipment']//div[contains(@class, 'q-field__control-container')]//div[contains(text(), 'Đăng ký xe')]/../../../../../label[contains(@class, 'q-field--error')]"
