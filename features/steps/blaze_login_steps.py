import time
from behave import *

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.readproperties import ReadConfig

baseUrl = ReadConfig.getAppURL()
username = ReadConfig.getUserEmail()
password = ReadConfig.getPassword()


@given(u'open the blaze application url')
def step_impl(context):
    context.driver.get(baseUrl)
    time.sleep(3)
    assert context.driver.title == "STORE"


@when(u'click on the login button')
def step_impl(context):
    context.hp = HomePage(context.driver)
    context.hp.click_on_login_link()
    time.sleep(3)


@then(u'login pop up page should display')
def step_impl(context):
    context.lp = LoginPage(context.driver)
    expected_login_header_text = "Log in"
    context.lp.check_login_page_header_text(expected_login_header_text)


@when(u'user enter valid credentials')
def step_impl(context):
    context.lp = LoginPage(context.driver)
    context.lp.enter_username(username)
    context.lp.enter_password(password)
    time.sleep(3)


@when(u'user enter valid email as "{email}" and valid password as "{passwrd}"')
def step_impl(context, email, passwrd):
    context.lp = LoginPage(context.driver)
    context.lp.enter_username(email)
    context.lp.enter_password(passwrd)
    time.sleep(3)


@when(u'user enter valid email id as "{emailid}" and valid password as "{paswrd}"')
def step_impl(context, emailid, paswrd):
    context.lp = LoginPage(context.driver)
    context.lp.enter_username(emailid)
    context.lp.enter_password(paswrd)
    time.sleep(3)


@when(u'click on the login button present on login pop up')
def step_impl(context):
    context.lp = LoginPage(context.driver)
    context.lp.click_on_login_btn()
    time.sleep(5)


@then(u'user should logged in')
def step_impl(context):
    context.hp = HomePage(context.driver)
    expected_text = username
    context.hp.check_username_on_home_page_after_login(expected_text)


@when(u'user enter invalid credentials')
def step_impl(context):
    context.lp = LoginPage(context.driver)
    context.lp.enter_username("User12Demo")
    context.lp.enter_password("User@12")
    time.sleep(3)


@then(u'user should not be able to login')
def step_impl(context):
    context.lp = LoginPage(context.driver)
    expected_text = "User does not exist."
    context.lp.check_alert_that_does_not_allow_to_login(expected_text)
