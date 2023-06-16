from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumCommonActions.basePage import BasePage
from utilities.customlogger import LogGen


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    text_login_page_xpath = "//h5[@id='logInModalLabel']"
    textbox_username_xpath = "//input[@id='loginusername']"
    textbox_password_xpath = "//input[@id='loginpassword']"
    button_login_xpath = "//button[text()='Log in']"

    logs = LogGen.loggen()

    def check_login_page_header_text(self, expected_header_text):
        self.logs.info('----------------Checked login page header text-----------------')
        self.verify_page_header_text("text_login_page_xpath", self.text_login_page_xpath, expected_header_text)

    def enter_username(self, username):
        self.logs.info('----------------Entered username-----------------')
        self.enter_text_into_element("textbox_username_xpath", self.textbox_username_xpath, username)

    def enter_password(self, password):
        self.logs.info('----------------Entered password-----------------')
        self.enter_text_into_element("textbox_password_xpath", self.textbox_password_xpath, password)

    def click_on_login_btn(self):
        self.logs.info('----------------Clicked on login button-----------------')
        self.click_on_element("button_login_xpath", self.button_login_xpath)

    def check_alert_that_does_not_allow_to_login(self, expected_text):
        self.logs.info('----------------Checked alert that does not allowed to login-----------------')
        self.verify_alert_text(expected_text)
        self.accept_alert()
