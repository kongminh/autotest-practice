# -*- coding: utf-8 -*-

'''
Common page objects
'''
import os 

class Common(object):
    base_url = 'https://automationexercise.com/'
    login_url = base_url + 'login'
   
class HomePage(object):
      signup_login_btn = '[href="/login"]'

class LoginPage(object):
    email_input = '[data-qa="login-email"]'
    password_input = '[type="password"]'
    login_btn = '[data-qa="login-button"]'
    logout_btn = '[href="/logout"]'
    email_value = '6969@yopmail.com'
    password_value = 'mm1111'      

class RegisterTestPage(object):
    login_btn = '[data-qa="login-button"]'
    name_input = '[data-qa="signup-name"]'
    email_input = '[data-qa="signup-email"]'
    submit_btn = '[data-qa="signup-button"]'
    name_value = 'channg8788'
    email_value = '67998@yopmail.com'
  
   

class InputAccountInforPage(object):
    mrs_radio = '#id_gender2'
    name_input = '#name'
    email_input = '#email'
    password_input = '#password'
    day_select = '#days'
    # day_select = '//*[@id="days"]'
    month_select = '#months'
    year_select = '#years'
    signup_checkbox = '#newsletter'
    receive_checkbox = '#optin'
    firstname_input = '[data-qa="first_name"]'
    lastname_input = '[data-qa="last_name"]'
    company_input = '#company'
    address1_input = '#address1'
    address2_input = '#address2'
    country_select = '#country'
    state_input = '#state'
    city_input = '#city'
    zipcode_input = '#zipcode'
    mobile_input = '#mobile_number'
    create_submit = '[data-qa="create-account"]'
    day_value = '1'
    month_value = 'May'
    year_value = '1988'
    password_value = 'mm1111'
    firstname_value = 'Trang'
    lastname_value = 'Luong Thi Thu'
    company_value = 'ABC'
    address1_value = 'CDE'
    address2_value = 'DFJ'
    state_value = '10000'
    city_value = '10000'
    zipcode_value = '10000'
    mobile_value = '10000'
    country_value = 'Canada'

    