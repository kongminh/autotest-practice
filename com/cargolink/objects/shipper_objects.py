# -*- coding: utf-8 -*-

'''
Shipper page objects
'''

class ShipperMenuPage(object):
    transport_request_menu = '//*[@id="shippers"]//div[contains(text(), "Hàng tìm xe")]'

class CreateOrderPage(object):
    create_order_btn = "//*[@id='shippers']/div/header/div/div/a/button"
    name_of_cargo = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[1]//input"
    type_of_cargo = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[2]"
    choose_cargo_type = "//div[@class='q-virtual-scroll__content']//div[@class='q-item__label'][contains(text(), 'nông')]"
    amount_box = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[3]//input"
    type_of_truck = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[4]"
    choose_truck_type = "//div[@class='q-virtual-scroll__content']//div[@class='q-item__label'][contains(text(), 'Bao')]"
    weight_box = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[5]//input"
    volume_box_6 = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[6]//input"
    volume_box_7 = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[7]//input"
    volume_box_8 = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[8]//input"
    truck_share = "(//div[contains(@class, 'q-radio__label')])[1]"
    truck_not_share = "(//div[contains(@class, 'q-radio__label')])[2]"
    button_1 = '(//*[@id="new-request-steps"]//button)[1]'
    button_2 = '(//*[@id="new-request-steps"]//button)[2]'
    button_3 = '(//*[@id="new-request-steps"]//button)[3]'
    send_btn = '//*[@id="new-request-steps"]//button//span[contains(text(), "Gửi")]/../../..'

    load_location = '//*[@id="origin"]'
    choose_load_location = '//div[contains(@class, "pac-container")]//span[contains(text(), "Hanoi")][1]'
    load_time = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[3]//input"
    load_contact_name = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[4]//input"
    load_contact_mobile = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[5]//input"
    delivery_location = '//*[@id="destination"]'
    choose_delivery_location = '//div[contains(@class, "pac-container")]//span[contains(text(), "Hải Dương")][1]'
    delivery_contact_name = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[4]//input"
    delivery_contact_mobile = "(//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')])[5]//input"
    valid_util_time = "//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')]//div[contains(text(), 'Có giá trị đến')]/../input"
    expect_price = "//*[@id='new-request-steps']//div[contains(@class, 'q-field__control-container')]//div[contains(text(), 'Giá mong muốn (bao gồm VAT)')]/../input"

    name_of_cargo_str = u"Gạo 08091341"
    load_location_str = u'Hà Nội'
    load_time_str = '12-08-2020 05:05'
    load_contact_name_str = '1'
    load_contact_mobile_str = '1234567890'
    delivery_contact_name_str = '2'
    delivery_contact_mobile_str = '2345678901'
    delivery_location_str = u'Hải Dương'
    valid_util_time_str = '12-08-2020 02:02'
    expect_price_value = 1000

class QuotationPage(object):
    quotation_tag = '//*[@id="shipper-request-list"]//span[contains(text(), "Đã báo giá")]'
    first_quotation = '//*[@id="shipper-request-list"]//table//tr[1]//button'
    accept_btn = '//*[@id="quoted-request"]//span[contains(text(), "Chấp nhận")]'