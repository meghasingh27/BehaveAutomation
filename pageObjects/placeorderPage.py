from seleniumCommonActions.basePage import BasePage
from utilities.customlogger import LogGen


class PlaceOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    text_place_order_xpath = "//h5[@id='orderModalLabel']"
    text_name_xpath = "//input[@id='name']"
    text_country_xpath = "//input[@id='country']"
    text_city_xpath = "//input[@id='city']"
    text_credit_card_xpath = "//input[@id='card']"
    text_month_xpath = "//input[@id='month']"
    text_year_xpath = "//input[@id='year']"
    button_purchase_xpath = "//button[text()='Purchase']"
    text_thank_you_xpath = "//h2[text()='Thank you for your purchase!']"
    text_order_id_xpath = "//p[@class='lead text-muted ']"
    button_ok_xpath = "//button[text()='OK']"

    logs = LogGen.loggen()

    def check_place_order_page_text(self, expected_text):
        self.logs.info('----------------Checked place order page text-----------------')
        self.verify_page_header_text("text_place_order_xpath", self.text_place_order_xpath, expected_text)

    def enter_name(self, name):
        self.logs.info('----------------Entered name-----------------')
        self.enter_text_into_element("text_name_xpath", self.text_name_xpath, name)

    def enter_country(self, country):
        self.logs.info('----------------Entered country-----------------')
        self.enter_text_into_element("text_country_xpath", self.text_country_xpath, country)

    def enter_city(self, city):
        self.logs.info('----------------Entered city-----------------')
        self.enter_text_into_element("text_city_xpath", self.text_city_xpath, city)

    def enter_credit_card_number(self, credit_card):
        self.logs.info('----------------Entered credit card number-----------------')
        self.enter_text_into_element("text_credit_card_xpath", self.text_credit_card_xpath, credit_card)

    def enter_month(self, month):
        self.logs.info('----------------Entered month-----------------')
        self.enter_text_into_element("text_month_xpath", self.text_month_xpath, month)

    def enter_year(self, year):
        self.logs.info('----------------Entered year-----------------')
        self.enter_text_into_element("text_year_xpath", self.text_year_xpath, year)

    def click_on_purchase_btn(self):
        self.logs.info('----------------Clicked on purchase button-----------------')
        self.click_on_element("button_purchase_xpath", self.button_purchase_xpath)

    def check_thank_you_displayed(self, expected_text):
        self.logs.info('----------------Checked thank you text is displayed-----------------')
        self.verify_element_contains_text("text_thank_you_xpath", self.text_thank_you_xpath, expected_text)

    def display_order_id(self):
        self.logs.info('----------------Order ID is Printed -----------------')
        x = self.get_element_text("text_order_id_xpath", self.text_order_id_xpath)
        print(x)

    def click_on_ok_btn(self):
        self.logs.info('----------------Ok Button is Clicked-----------------')
        self.click_on_element("button_ok_xpath", self.button_ok_xpath)
