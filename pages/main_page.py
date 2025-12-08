import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BaseLocators


class MainPage(BasePage):

    @allure.step('Открытие главной страницы')
    def get_main_page(self):
        self.get_page(BaseLocators.MAIN_PAGE_URL)
        self.wait_for_element_visible(MainPageLocators.INGREDIENTS_HEADER)

    @allure.step('Нажатие на первую булочку')
    def click_on_first_bun(self):
        self.click_on_button(MainPageLocators.FIRST_BUN)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_on_create_order(self):
        self.click_on_button(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверяем, что всплывающее окно с деталями появилось')
    def is_ingredient_details_popup_show(self):
        self.wait_for_element_visible(MainPageLocators.INGREDIENT_DETAILS_HEADER)
        return self.are_elements_displayed(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Нажатие на кнопку, закрывающую окно с деталями ингредиента')
    def click_close_popup_details(self):
        self.click_on_button(MainPageLocators.INGREDIENT_DETAILS_POPUP_CLOSE_BUTTON)

    @allure.step('Получение количества ингредиента')
    def get_bun_counter_value(self):
        value = self.get_text(MainPageLocators.FIRST_BUN_COUNTER)
        return int(value)

    @allure.step('Перетянуть булочку в конструктор')
    def drag_and_drop_bun_into_constructor(self):
        self.drag_and_drop_element(MainPageLocators.FIRST_BUN, MainPageLocators.CONSTRUCTOR_AREA)

    @allure.step('Проверка увеличения счетчика при добавлении ингредиента')
    def is_ingredient_counter_increases(self, old_value, new_value):
        self.wait_for_element_visible(MainPageLocators.FIRST_BUN_COUNTER)
        return new_value == old_value + 2

    @allure.step('Проверка закрытия окна с деталями ингредиентов')
    def is_ingredients_details_popup_closes(self):
        try:
            self.wait_until_element_disappears(MainPageLocators.INGREDIENT_DETAILS_HEADER)
            return True

        except Exception:
            return False

    @allure.step('Проверка, что переход на главную страницу произошел')
    def is_current_url_main_page(self):
        self.wait_for_element_visible(MainPageLocators.INGREDIENTS_HEADER)
        if self.get_url() == BaseLocators.MAIN_PAGE_URL:
            return True
