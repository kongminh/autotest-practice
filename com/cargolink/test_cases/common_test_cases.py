# -*- coding: utf-8 -*-

'''
Carrier test cases
'''

from seleniumbase import BaseCase
from com.cargolink.objects.common_objects import Common, LoginPage
from com.cargolink.objects.carrier_objects import CreateQuotationPage as QuotationPage

class CommonTestCases(BaseCase):
    def RegisterCGL01_08(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        # self.type(Common.Phonenumber,'')
        self.click(Common.btnNextForm)
        self.click(Common.validatePhonenumber)
        pass

    def RegisterCGL01_08_01(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.Phonenumber,'0969621348')
        self.click(Common.btnNextForm)
        self.click(Common.validatePhonenumber)
        pass

    def RegisterCGL01_09(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.Phonenumber, 'dgdgfdgf')
        self.click(Common.btnNextForm)
        self.click(Common.validatePhonenumber)
        pass

    def RegisterCGL01_10(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.Phonenumber, '56255')
        self.click(Common.btnNextForm)
        self.click(Common.validatePhonenumber)
        pass

    def RegisterCGL01_11(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.Phonenumber, '08652')
        self.click(Common.btnNextForm)
        self.click(Common.validatePhonenumber)
        pass


    # def RegisterCGL01_12(self):
    #     self.maximize_window()
    #     self.open(Common.login_url)
    #     self.click(Common.DangKy)
    #     self.click(Common.btnNext)
    #     self.type(Common.Phonenumber, '84928860338')
    #     self.click(Common.btnNextForm)
    #     pass

    # def RegisterCGL01_14(self):
    #     self.maximize_window()
    #     self.open(Common.login_url)
    #     self.click(Common.DangKy)
    #     self.click(Common.btnNext)
    #     self.type(Common.Phonenumber, '0928860338')
    #     self.click(Common.btnNextForm)

    #     pass

    def RegisterCGL01_15(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        # self.type(Common.Name, '0928860338')
        self.click(Common.btnNextForm)
        self.click(Common.validateName)
        pass

    def RegisterCGL01_16(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.Name, '$##$#$#')
        self.click(Common.btnNextForm)
        self.click(Common.validateName)
        pass

    def RegisterCGL01_20(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.MatKhau, 'Abcd123')
        self.click(Common.btnNextForm)
        self.click(Common.validateMatKhau)
        pass

    def RegisterCGL01_21(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.MatKhau, 'ABCD1234')
        self.click(Common.btnNextForm)
        self.click(Common.validateMatKhau)
        pass
    def RegisterCGL01_22(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.MatKhau, 'abcd1234')
        self.click(Common.btnNextForm)
        self.click(Common.validateMatKhau)
        pass

    def RegisterCGL01_23(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.MatKhau, '')
        self.click(Common.btnNextForm)
        self.click(Common.validateMatKhau)
        pass

    def RegisterCGL01_24(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.XacNhanMatKhau, '')
        self.click(Common.btnNextForm)
        self.click(Common.validateXacNhanMatKhau)
        pass

    def RegisterCGL01_25(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.XacNhanMatKhau, 'ABCD1234')
        self.click(Common.btnNextForm)
        self.click(Common.validateXacNhanMatKhau)
        pass

    def RegisterCGL01_26(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.Phonenumber, '0928860338')
        self.type(Common.Name, u'My Đỗ')
        self.type(Common.MatKhau, u'Abcd1234')
        self.type(Common.XacNhanMatKhau, u'Abcd1234')
        self.click(Common.CheckBoxToiDongY)
        self.click(Common.btnNextForm)

        pass

    def RegisterCGL01_27(self):
        self.maximize_window()
        self.open(Common.login_url)
        self.click(Common.DangKyLink)
        self.click(Common.ChuHangDangKy)
        self.click(Common.btnNext)
        self.type(Common.MatKhau, 'ABCD1234')
        self.click(Common.btnNextForm)
        self.click(Common.validateToiDongY)
        pass