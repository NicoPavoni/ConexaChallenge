import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.screens.bookstore_app.bookstore import Bookstore
from tests.screens.login.login import LoginPage


def test_login(browser):
    page = LoginPage(browser)
    page.get_username_input().send_keys('admin')
    page.get_password_input().send_keys('Admin.1234$')
    page.click_login_btn()
    time.sleep(5)


def test_add_book_to_collection(browser):
    page = Bookstore(browser)
    page.click_bookstore_side_btn()
    time.sleep(2)
    page.get_searchbar_input().send_keys('Learning JavaScript Design Patterns')
    page.get_book_id().click()
    page.click_add_to_collection_btn()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
    page.click_back_to_book_btn()
    time.sleep(5)


def test_delete_book_from_profile(browser):
    page = Bookstore(browser)
    page.click_profile_side_btn()
    time.sleep(2)
    page.click_delete_all_books_btn()
    page.click_ok_modal_btn()
    time.sleep(2)
    alert = browser.switch_to.alert
    alert.accept()
