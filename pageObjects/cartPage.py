from seleniumCommonActions.basePage import BasePage
from utilities.customlogger import LogGen


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    text_asus_item_xpath = "//td[text()='ASUS Full HD']"
    text_asus_item_price_xpath = "//td[text()='230']"
    link_delete_xpath = "//a[text()='Delete']"
    button_place_order_xpath = "//button[text()='Place Order']"

    logs = LogGen.loggen()

    def check_asus_item_text(self, expected_text):
        self.logs.info('----------------Checked asus item text-----------------')
        self.verify_element_contains_text("text_asus_item_xpath", self.text_asus_item_xpath, expected_text)

    def check_asus_item_price_text(self, expected_text):
        self.logs.info('----------------Checked asus item price value-----------------')
        self.verify_element_contains_text("text_asus_item_price_xpath", self.text_asus_item_price_xpath, expected_text)

    def check_delete_button_present(self):
        self.logs.info('----------------Checked delete button is present-----------------')
        self.element_is_displayed("link_delete_xpath", self.link_delete_xpath)

    def click_on_place_order_button(self):
        self.logs.info('----------------Clicked on place order button-----------------')
        self.click_on_element("button_place_order_xpath", self.button_place_order_xpath)
