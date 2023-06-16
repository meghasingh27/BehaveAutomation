from seleniumCommonActions.basePage import BasePage
from utilities.customlogger import LogGen


class ProductDescriptionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    button_next_xpath = "//button[@id='next2']"
    link_asus_product_xpath = "//a[text()='ASUS Full HD']"
    text_product_store_xpath = "//a[text()=' PRODUCT STORE']"
    text_asus_product_xpath = "//h2[text()='ASUS Full HD']"
    text_asus_product_price_xpath = "//h3[text()='$230']"
    link_add_to_cart_xpath = "//a[text()='Add to cart']"

    logs = LogGen.loggen()

    def click_on_next_button(self):
        self.logs.info('----------------Clicked on next button-----------------')
        self.click_on_element("button_next_xpath", self.button_next_xpath)

    def click_on_asus_full_hd_product_button(self):
        self.logs.info('----------------Clicked on ASUS Full HD product-----------------')
        self.click_on_element("link_asus_product_xpath", self.link_asus_product_xpath)

    def check_product_store_page_text(self, expected_text):
        self.logs.info('----------------Checked product store page text-----------------')
        self.verify_page_header_text("text_product_store_xpath", self.text_product_store_xpath, expected_text)

    def check_asus_product_text(self, expected_text):
        self.logs.info('----------------Checked asus product text-----------------')
        self.verify_element_contains_text("text_asus_product_xpath", self.text_asus_product_xpath, expected_text)

    def check_asus_product_price_text(self, expected_text):
        self.logs.info('----------------Checked asus product price value-----------------')
        text = self.get_element_text("text_asus_product_price_xpath", self.text_asus_product_price_xpath)
        lst = text.split(" ")
        s = lst[0]
        s1 = s[1:]
        assert s1 == expected_text

    def click_on_add_to_cart(self):
        self.logs.info('----------------Clicked on add to cart-----------------')
        self.click_on_element("link_add_to_cart_xpath", self.link_add_to_cart_xpath)

    def check_alert_product_added(self, expected_text):
        self.logs.info('----------------Checked alert product_added-----------------')
        self.verify_alert_text(expected_text)
        self.accept_alert()
