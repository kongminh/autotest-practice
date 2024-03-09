# -*- coding: utf-8 -*-

'''
Common page objects
'''

class Common(object):
    login_url = 'https://dev.dev.cargolink.vn/login'
    login_str = 'Đăng nhập'
    create_order_str = 'Tạo yêu cầu vận chuyển'
    loading_status = '//div[contains(@class, "q-loading")]'
    animate_scale = '//div[contains(@class, "q-animate--scale")]'
    send_btn = '//button//span[contains(text(), "Gửi")]/../../..'
    ok_dialog_btn = '/html/body/div[contains(@class, "q-dialog")]//span[contains(text(), "OK")]'

    @staticmethod
    def wait_loading_show(self):
        self.wait_for_element_present(Common.loading_status)

    @staticmethod
    def wait_loading(self):
        self.wait_for_element_not_present(Common.loading_status)

    @staticmethod
    def wait_animate(self):
        self.wait_for_element_not_present(Common.animate_scale)


    DangKyLink='#login-layout > div.inner div:nth-child(2) > div.col-lg-12.col-md-12.col-xs-12 > div > a'
    ChuHangDangKy='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div:nth-child(1)'
    ChuXeDangKy='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div:nth-child(2)'
    btnNext='#login-layout div.bottom-register button'
    CheckBoxDoanhNghiep='#choose-role div.cursor-pointer:nth-child(1)> div:nth-child(1)'
    CheckBoxCaNhanNghiep='#choose-role div.cursor-pointer:nth-child(2)> div:nth-child(1)'
    Phonenumber='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div > div:nth-child(2) input'
    Name=' #login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div > div:nth-child(3) input'
    NguoiLienLac='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div > div:nth-child(4) input'
    DiaChiDangky='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div > div:nth-child(5) input'
    SoDangKyKinhDoanh='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div > div:nth-child(6) input'
    MatKhau='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div.col-lg-6.col-md-6.col-xs-12.q-pl-md > div:nth-child(2) input'
    XacNhanMatKhau='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div.col-lg-6.col-md-6.col-xs-12.q-pl-md > div:nth-child(3) input'
    CheckBoxToiDongY='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div:nth-child(5) > div > div'

    btnNextForm='#login-layout > div.inner.q-card > div.fixed-center > div button.bg-primary'
    btnPreForm='#login-layout > div.inner.q-card > div.fixed-center > div button.bg-blue-15'
    validatePhonenumber='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div > div:nth-child(2) label div:nth-child(2)> div'
    validateName=' #login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div > div:nth-child(3) label div:nth-child(2)> div'
    validateMatKhau='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div.col-lg-6.col-md-6.col-xs-12 > div:nth-child(2) label div:nth-child(2)>div'
    validateXacNhanMatKhau='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div.col-lg-6.col-md-6.col-xs-12 > div:nth-child(3) label div:nth-child(2)> div'
    validateToiDongY='#login-layout > div.inner.q-card > div.fixed-center > div > div:nth-child(2) > div > div > div:nth-child(5) div:nth-child(2)> div'

class LoginPage(object):
    tel_box = 'input[type="tel"]'
    pass_box = 'input[type="password"]'
    shipper_radio_btn = '//div[@role="radio"][1]'
    carrier_radio_btn = '//div[@role="radio"][2]'
    login_btn = '//button//span[contains(text(), "Đăng nhập")]/../../..'

    tel_input = '983974528'
    pass_input = 'Admin123'
