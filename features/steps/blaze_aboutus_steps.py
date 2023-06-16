import time

from behave import *

from pageObjects.aboutusPage import AboutUsPage
from pageObjects.homePage import HomePage


@when(u'click on about us link present in home page')
def step_impl(context):
    context.hp = HomePage(context.driver)
    context.hp.click_on_about_us_link()
    time.sleep(3)


@then(u'about us page should display')
def step_impl(context):
    expected_text = "About us"
    context.au = AboutUsPage(context.driver)
    context.au.check_about_us_text(expected_text)


@then(u'click on close button present in about us page')
def step_impl(context):
    context.au = AboutUsPage(context.driver)
    context.au.click_on_close_button()
    time.sleep(3)


@then(u'user should direct back to home page')
def step_impl(context):
    expected_title = "E12243544"
    context.hp = HomePage(context.driver)
    context.hp.check_home_page_title(expected_title)
