from seleniumCommonActions.basePage import BasePage
from utilities.customlogger import LogGen


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    link_login_xpath = "//li//a[text()='Log in']"
    text_home_page_username_xpath = "//li//a[@id='nameofuser']"
    link_contact_xpath = "//li//a[text()='Contact']"
    link_about_us_xpath = "//a[contains(text(),'About us')]"
    link_laptop_category_xpath = "//a[text()='Laptops']"
    link_cart_xpath = "//a[text()='Cart']"
    link_category_xapth = "//a[@id='cat']"

    logs = LogGen.loggen()

    def click_on_login_link(self):
        self.logs.info('----------------Clicked on the login link-----------------')
        self.click_on_element("link_login_xpath", self.link_login_xpath)

    def check_username_on_home_page_after_login(self, expected_text):
        self.logs.info('----------------Checked username on the home page after login-----------------')
        self.verify_element_contains_text("text_home_page_username_xpath", self.text_home_page_username_xpath, expected_text)

    def click_on_contact_link(self):
        self.logs.info('----------------Clicked on the contact link-----------------')
        self.click_on_element("link_contact_xpath", self.link_contact_xpath)

    def click_on_about_us_link(self):
        self.logs.info('----------------Clicked on the about us link-----------------')
        self.click_on_element("link_about_us_xpath", self.link_about_us_xpath)

    def check_home_page_title(self, expected_title):
        self.logs.info('----------------Verification of home page title-----------------')
        self.verify_page_title(expected_title)

    def click_on_laptop_category(self):
        self.logs.info('----------------Clicked on Laptop Category-----------------')
        self.click_on_element("link_laptop_category_xpath", self.link_laptop_category_xpath)

    def click_on_cart_link(self):
        self.logs.info('----------------Clicked on the cart link-----------------')
        self.click_on_element("link_cart_xpath", self.link_cart_xpath)

    def category_displayed_on_home_page(self, expected_text):
        self.logs.info('----------------Category displayed on home page-----------------')
        self.verify_page_header_text("link_category_xapth", self.link_category_xapth, expected_text)