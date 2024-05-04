# -*- coding: utf-8 -*-

'''
Common page objects
'''
import os 

class Common(object):
    base_url = 'https://impactlabs.kaz.wiki/en'
    login_btn = '(//a[@href="/auth/log-in"])[1]'
    signup_btn = '[style="--button-color:var(--mantine-color-white);border:1px solid black;background:#FAC91B;color:#000000"]'
   
class Signup(object):
    email_input = '#mantine-eveu7qtlo'
    password_input = '#mantine-h2020wka5'
    continue_btn = '[type="submit"]'
    email_value = 'minhtest14@yopmail.com'
    password_value = '1'
    