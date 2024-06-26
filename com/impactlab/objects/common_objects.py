# -*- coding: utf-8 -*-

'''
Common page objects
'''
import os 

class Common(object):
    base_url = 'https://devdev.impactlabs.org'
    login_btn = '//div[contains(@class, "hidden lg:flex")]//button[contains(text(), "Login")]'
    signup_btn = '//div[contains(@class, "hidden lg:flex")]//button[contains(text(), "Register")]'

class Signup(object):
    email_input = '//form//input[contains(@placeholder, "email")]'
    password_input = '//form//input[contains(@type, "password")]'
    continue_btn = '//form/button[contains(@type, "submit")]'
    email_value = 'minhtest22@yopmail.com'
    password_value = '12312345'

class Login(object):
    email_input = '//form//input[contains(@placeholder, "Enter email")]'
    password_input = '//form//input[contains(@type, "password")]'
    continue_btn = '//form/button[contains(@type, "submit")]'
    email_value = 'minhtest22@yopmail.com'
    password_value = '12312345'
    profile_avatar_img = '(//img[contains(@alt, "avatar")])[1]'

class Fund(object):
    fund_list_btn = '//a[contains(text(), "Funds")]'
    fund_1st_btn = '(//a[contains(@href, "/funds/")])[1]'
    donation_match_txt = '//p[contains(text(), "Donation Matching Live")]'
    donate_btn = '//button[contains(text(), "Donate")]'
    donate_now_btn = '//button[contains(text(), "Donate now")]'
    add_tip_input = '//input[contains(@type, "number")]'
    add_tip_value = 5
    add_tip_btn = '//button//span[contains(text(), "Add tip")]'
