import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from utilities.readproperties import ReadConfig

browser = ReadConfig.getBrowser()


# before all
def before_all(context):
    print('Before all executed')


# # before feature
# def before_feature(context, feature):
#     print('Before every feature')


# before every scenario
def before_scenario(context, driver):
    if browser == "chrome":
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == "firefox":
        context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser == "edge":
        context.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    context.driver.maximize_window()
    context.driver.implicitly_wait(45)


# # before every step
# def before_step(context, step):
#     print('Before every step')


# # before every tag
# def before_tag(context, tag):
#     print('Before every tag')


# # after every tag
# def after_tag(context, tag):
#     print('after every tag')


# after every step
def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="failed_screenshot",
                      attachment_type=AttachmentType.PNG)


# after every scenario
def after_scenario(context, driver):
    context.driver.quit()


# # after every feature
# def after_feature(context, feature):
#     print('After every feature')


# after all
def after_all(context):
    print('After all executed')
