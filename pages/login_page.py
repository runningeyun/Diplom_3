import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginLocators
from locators.base_page_locators import BaseLocators
from data import UserData


class LoginPage(BasePage):

    @allure.step('Открытие страницы авторизации')
    def get_login_page(self):
        self.get_page(BaseLocators.LOGIN_URL)
        self.wait_for_element_visible(LoginLocators.EMAIL_FIELD_INPUT)

    @allure.step('Вход в аккаунт')
    def login(self):
        self.fill_field(LoginLocators.EMAIL_FIELD_INPUT, UserData.EMAIL)
        self.fill_field(LoginLocators.PASSWORD_FIELD_INPUT, UserData.PASSWORD)
        self.click_on_button(LoginLocators.ENTER_BUTTON)
        self.wait_for_element_visible(MainPageLocators.INGREDIENTS_HEADER)
