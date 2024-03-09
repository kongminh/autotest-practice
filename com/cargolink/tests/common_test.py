# -*- coding: utf-8 -*-

'''
Common testing
'''

from seleniumbase import BaseCase
from config import Config
import pytest
from com.cargolink.test_cases.common_test_cases import CommonTestCases


@pytest.mark.skipif(Config.disable_common, reason="Config")
class CommonTests(CommonTestCases):

    # @pytest.mark.run(order=100)
    # def test_wait(self):
    #     self.wait(Config.wait_in_finish)

    @pytest.mark.run(order=100)
    def test_case01_08(self):
        self.RegisterCGL01_08()

    @pytest.mark.run(order=101)
    def test_case01_08_1(self):
        self.RegisterCGL01_08_01()

    @pytest.mark.run(order=102)
    def test_case01_09(self):
        self.RegisterCGL01_09()

    @pytest.mark.run(order=103)
    def test_case01_10(self):
        self.RegisterCGL01_10()

    @pytest.mark.run(order=104)
    def test_case01_11(self):
        self.RegisterCGL01_11()

    @pytest.mark.run(order=105)
    def test_case01_15(self):
        self.RegisterCGL01_15()

    @pytest.mark.run(order=106)
    def test_case01_16(self):
        self.RegisterCGL01_16()

    @pytest.mark.run(order=107)
    def test_case01_20(self):
        self.RegisterCGL01_20()

    @pytest.mark.run(order=108)
    def test_case01_21(self):
        self.RegisterCGL01_21()

    @pytest.mark.run(order=109)
    def test_case01_22(self):
        self.RegisterCGL01_22()

    @pytest.mark.run(order=110)
    def test_case01_23(self):
        self.RegisterCGL01_23()

    @pytest.mark.run(order=111)
    def test_case01_24(self):
        self.RegisterCGL01_24()

    @pytest.mark.run(order=112)
    def test_case01_25(self):
        self.RegisterCGL01_25()

    @pytest.mark.run(order=113)
    def test_case01_26(self):
        self.RegisterCGL01_26()

    @pytest.mark.run(order=114)
    def test_case01_27(self):
        self.RegisterCGL01_27()

