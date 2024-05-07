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
    email_input = '#mantine-huj7p3f5m'
    password_input = '#mantine-9n9f6nyey'
    continue_btn = '[type="submit"]'
    email_value = 'minhtest15@yopmail.com'
    password_value = 'Mm@11111'
    