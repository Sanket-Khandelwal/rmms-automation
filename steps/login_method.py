import time

from behave import *
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from yopmail import Yopmail


@given('open browser')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get('https://portal-dms-test.dish.com/')
    # context.browser.implicitly_wait(10)


@when('enter username and password')
def step_impl(context):
    context.browser.find_element(By.NAME, 'email').send_keys('superuser@yopmail.com')
    context.browser.find_element(By.NAME, 'password').send_keys('Icx@123456')
    context.browser.find_element(By.ID, 'login').click()
    # context.browser.implicitly_wait(200)


@then('verify auth page')
def step_impl(context):
    # context.browser.implicitly_wait(20)
    time.sleep(10)
    response = requests.get("https://yopmail.com/", verify=False)
    print(response)
    y = Yopmail('superuser@yopmail.com',proxies=None)
    mail_ids = y.get_mail_ids()
    for mail_id in mail_ids:
        print(mail_id)
    # context.browser.get('https://yopmail.com/', verify=False)
    print(context.browser.current_url)
    time.sleep(10)
    assert context.browser.current_url == 'https://portal-dms-test.dish.com/authenticate'
