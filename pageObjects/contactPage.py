from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumCommonActions.basePage import BasePage
from utilities.customlogger import LogGen


class ContactPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    text_contact_page_xpath = "//h5[@id='exampleModalLabel']"
    textbox_contact_email_xpath = "//input[@id='recipient-email']"
    textbox_contact_name_xpath = "//input[@id='recipient-name']"
    textbox_message_xpath = "//textarea[@id='message-text']"
    button_send_message_xpath = "//button[text()='Send message']"

    logs = LogGen.loggen()

    def check_contact_page_header_text(self, expected_header_text):
        self.logs.info('----------------Checked contact page header text-----------------')
        self.verify_page_header_text("text_contact_page_xpath", self.text_contact_page_xpath, expected_header_text)

    def enter_contact_email(self, contact_email):
        self.logs.info('----------------Entered contact email-----------------')
        self.enter_text_into_element("textbox_contact_email_xpath", self.textbox_contact_email_xpath, contact_email)

    def enter_contact_name(self, contact_name):
        self.logs.info('----------------Entered contact name-----------------')
        self.enter_text_into_element("textbox_contact_name_xpath", self.textbox_contact_name_xpath, contact_name)

    def enter_message(self, message):
        self.logs.info('----------------Entered message-----------------')
        self.enter_text_into_element("textbox_message_xpath", self.textbox_message_xpath, message)

    def click_on_sendMessage_btn(self):
        self.logs.info('----------------Clicked on sendMessage button-----------------')
        self.click_on_element("button_send_message_xpath", self.button_send_message_xpath)

    def check_alert_saying_thanks(self, expected_text):
        self.logs.info('----------------Checked alert saying thanks text-----------------')
        self.verify_alert_text(expected_text)
        self.accept_alert()