# -*- coding: utf-8 -*-

'''
Carrier testing
'''

from com.cargolink.test_cases.carrier_test_cases import CarrierTestCases
from com.cargolink.test_cases.carrier.create_freight_offer import CarrierCreateFreightOffer
from config import Config
import pytest


@pytest.mark.skipif(Config.disable_carrier, reason="Config")
class CarrierTests(CarrierTestCases):

    @pytest.mark.run(order=200)
    def test_login(self):
        self.login()

    @pytest.mark.run(order=201)
    def test_create_quotation(self):
        self.create_quotation()

@pytest.mark.skipif(Config.disable_carrier, reason="Config")
class CarrierCreateFreightOfferTest(CarrierCreateFreightOffer):

    @pytest.mark.run(order=400)
    def test_create_freight_offer(self):
        self.login()
        self.create_freight_offer()
