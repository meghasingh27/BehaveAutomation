from seleniumCommonActions.basePage import BasePage
from utilities.customlogger import LogGen


class AboutUsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    text_about_us_xpath = "//h5[contains(text(),'About us')]"
    button_close_xpath = "(//button[contains(text(),'Close')])[4]"

    logs = LogGen.loggen()

    def check_about_us_text(self, expected_text):
        self.logs.info('----------------Checked about us text-----------------')
        self.verify_page_header_text("text_about_us_xpath", self.text_about_us_xpath, expected_text)

    def click_on_close_button(self):
        self.logs.info('----------------Clicked on close button-----------------')
        self.click_on_element("button_close_xpath", self.button_close_xpath)
