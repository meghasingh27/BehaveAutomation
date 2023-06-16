import time

from behave import *
from datetime import datetime
from pageObjects.contactPage import ContactPage
from pageObjects.homePage import HomePage
from utilities import commonmethods


@when(u'click on the contact button')
def step_impl(context):
    context.hp = HomePage(context.driver)
    context.hp.click_on_contact_link()
    time.sleep(3)


@then(u'contact pop up should display')
def step_impl(context):
    expected_header_text = "New message"
    #expected_header_text = "Xyz"
    context.cp = ContactPage(context.driver)
    context.cp.check_contact_page_header_text(expected_header_text)


@then(u'user enter all the details')
def step_impl(context):
    context.cp = ContactPage(context.driver)
    context.cp.enter_contact_email("User@yopmail.com")
    context.cp.enter_contact_name("UserDemo")
    context.cp.enter_message("Hi Blaze Store...")
    time.sleep(3)


@then(u'user enter all the below details')
def step_impl(context):
    for row in context.table:
        context.cp = ContactPage(context.driver)
        time_stamp = commonmethods.get_current_datetime()
        new_email = row["contact_email"] + time_stamp + "@yopmail.com"
        context.cp.enter_contact_email(new_email)
        context.cp.enter_contact_name(row["contact_name"])
        context.cp.enter_message(row["message"])
        time.sleep(3)


@then(u'click on the send message button')
def step_impl(context):
    context.cp = ContactPage(context.driver)
    context.cp.click_on_sendMessage_btn()
    time.sleep(3)


@then(u'thanks saying pop up should display')
def step_impl(context):
    expected_text = "Thanks You.."
    context.cp = ContactPage(context.driver)
    context.cp.check_alert_saying_thanks(expected_text)
