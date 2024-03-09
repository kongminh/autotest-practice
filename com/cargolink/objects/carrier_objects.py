# -*- coding: utf-8 -*-

'''
Carrier page objects
'''

from com.cargolink.objects.shipper_objects import CreateOrderPage as COPage

class CreateQuotationPage(object):
    create_quotation_btn = '//span[contains(text(), "' + COPage.name_of_cargo_str + '")]/../../../..//a'
    quotation_btn = '//button//span[contains(text(), "Báo giá")]/../../..'
    fee_box = "//div[contains(@class, 'q-field__control-container')]//div[contains(text(), 'Phí vận chuyển')]/../input"
    valid_until_box = "//div[contains(@class, 'q-field__control-container')]//div[contains(text(), 'Có giá trị đến')]/../input"

    quote_price_value = 1000
    valid_util_time_str = '12-08-2020 01:00'
