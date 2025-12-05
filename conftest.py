import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    browser = request.param
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
@allure.step('Авторизация пользователя')
def user_login(driver):
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.login()
    return driver
