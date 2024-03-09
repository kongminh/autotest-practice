# -*- coding: utf-8 -*-

'''
Shipper testing
'''

from com.cargolink.test_cases.shipper_test_cases import ShipperTestCases
from config import Config
import pytest

@pytest.mark.skipif(Config.disable_shipper, reason="Config")
class ShipperTests(ShipperTestCases):

    @pytest.mark.run(order=100)
    def test_login(self):
        self.login()

    @pytest.mark.run(order=101)
    def test_create_order(self):
        self.create_order()

    @pytest.mark.run(order=300)
    def test_accept_quotation(self):
        self.login()
        self.accept_quotation()
