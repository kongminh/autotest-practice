# -*- coding: utf-8 -*-

'''
Common page objects
'''
import os 

class Common(object):
    base_url = 'https://automationexercise.com/'
    login_url = base_url + 'login'

class LoginPage(object):
    username_input = '.login-page__username input'
    password_input = '.login-page__password input'
    login_btn = '.login-page__button-wrapper .btn--primary'

    username_value = ''
    password_value = ''

class PopupTestPage(object):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    popup_base_url = 'file:///' + dir_path + '/../../../mock_pages/index.html'

    popup1_btn = '//button[contains(text(), "Popup 1")]'
    popup2_btn = '//button[contains(text(), "Popup 2")]'
    popup3_btn = '//button[contains(text(), "Popup 3")]'

    popup_title = '//h1[contains(text(), "Đây là cửa sổ popup")]'
    text_input = '#fname'

class SignupPage(object):
    signup_btn = '//a[contains(@href, "/login")]'
