import time

from behave import *
from pageObjects.homePage import HomePage
from pageObjects.productdescriptionPage import ProductDescriptionPage
from pageObjects.cartPage import CartPage
from pageObjects.placeorderPage import PlaceOrderPage


@when(u'click on laptop category')
def step_impl(context):
    context.hp = HomePage(context.driver)
    context.hp.click_on_laptop_category()
    time.sleep(3)


@when(u'click on next button')
def step_impl(context):
    context.pd = ProductDescriptionPage(context.driver)
    context.pd.click_on_next_button()
    time.sleep(3)


@then(u'click on ASUS Full HD item')
def step_impl(context):
    context.pd = ProductDescriptionPage(context.driver)
    context.pd.click_on_asus_full_hd_product_button()
    time.sleep(3)


@then(u'product description page should display')
def step_impl(context):
    expected_text = "PRODUCT STORE"
    context.pd = ProductDescriptionPage(context.driver)
    context.pd.check_product_store_page_text(expected_text)


@then(u'check product description as per requirement')
def step_impl(context):
    expected_text_item = "ASUS"
    expected_text_price = "230"
    context.pd = ProductDescriptionPage(context.driver)
    context.pd.check_asus_product_text(expected_text_item)
    context.pd.check_asus_product_price_text(expected_text_price)


@then(u'click on add to cart')
def step_impl(context):
    context.pd = ProductDescriptionPage(context.driver)
    context.pd.click_on_add_to_cart()
    time.sleep(3)


@then(u'product added pop page should display product text')
def step_impl(context):
    expected_text = "Product added"
    context.pd = ProductDescriptionPage(context.driver)
    context.pd.check_alert_product_added(expected_text)


@when(u'product added click on cart page')
def step_impl(context):
    context.hp = HomePage(context.driver)
    context.hp.click_on_cart_link()
    time.sleep(3)


@then(u'check asus item description on cart page')
def step_impl(context):
    expected_text_item = "ASUS"
    expected_text_price = "230"
    context.cp = CartPage(context.driver)
    context.cp.check_asus_item_text(expected_text_item)
    context.cp.check_asus_item_price_text(expected_text_price)


@when(u'click on cart page')
def step_impl(context):
    context.hp = HomePage(context.driver)
    context.hp.click_on_cart_link()
    time.sleep(3)


@then(u'verify that delete button is visible on the page')
def step_impl(context):
    context.cp = CartPage(context.driver)
    context.cp.check_delete_button_present()
    time.sleep(3)


@when(u'delete button is visible click on place order')
def step_impl(context):
    context.cp = CartPage(context.driver)
    context.cp.click_on_place_order_button()
    time.sleep(3)


@then(u'verify place order page')
def step_impl(context):
    expected_text = "Place order"
    context.po = PlaceOrderPage(context.driver)
    context.po.check_place_order_page_text(expected_text)


@when(u'user enter valid credentials to place order')
def step_impl(context):
    context.po = PlaceOrderPage(context.driver)
    context.po.enter_name("Tannu")
    context.po.enter_country("India")
    context.po.enter_city("Kolkata")
    context.po.enter_credit_card_number("1111222233334444")
    context.po.enter_month("09")
    context.po.enter_year("2028")
    time.sleep(3)


@then(u'click on purchase button')
def step_impl(context):
    context.po = PlaceOrderPage(context.driver)
    context.po.click_on_purchase_btn()
    time.sleep(3)


@then(u'verify that thank you pop is displayed')
def step_impl(context):
    expected_text = "Thank you"
    context.po = PlaceOrderPage(context.driver)
    context.po.check_thank_you_displayed(expected_text)
    time.sleep(3)


@then(u'print the order id and click on ok button')
def step_impl(context):
    context.po = PlaceOrderPage(context.driver)
    context.po.display_order_id()
    context.po.click_on_ok_btn()
    time.sleep(3)


@then(u'user should direct back to main page')
def step_impl(context):
    expected_text = "CATEGORIES"
    context.hp = HomePage(context.driver)
    context.hp.category_displayed_on_home_page(expected_text)
    time.sleep(3)

