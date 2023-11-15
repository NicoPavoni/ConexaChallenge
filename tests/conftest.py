import pytest
from selenium import webdriver


@pytest.fixture(scope="module")  # Fixture para que los 3 tests compartan la instancia del navegador
def browser():
    browser = webdriver.Chrome()
    browser.get('https://demoqa.com/login')
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    yield browser
    browser.quit()
