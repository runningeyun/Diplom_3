import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed import OrderFeed


class TestMainFunctionality:

    @allure.title('переход по клику на "Конструктор"')
    @allure.description('Проверка осуществления перехода на главную страницу при клике на кнопку "Конструктор" в шапке страницы')
    def test_click_on_constructor_opens_main_page(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        login_page.get_login_page()
        login_page.click_on_constructor_button()
        assert main_page.is_current_url_main_page()

    @allure.title('Переход по клику на "Лента заказов"')
    @allure.description('Проверка перехода на страницу с заказами при клике на кнопку "Лента заказов" в шапке страницы')
    def test_click_on_orders_feed_opens_orders_feed_page(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeed(driver)
        main_page.get_main_page()
        main_page.click_on_order_feed_button()
        assert order_feed.is_current_url_order_feed()

    @allure.title('Клик на ингредиент вызывает всплывающее окно с деталями ингредиента')
    def test_click_on_ingredient_opens_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_on_first_bun()
        assert main_page.is_ingredient_details_popup_show()

    @allure.title('Всплывающее окно с деталями ингредиента закрывается кликом по крестику')
    def test_click_x_on_ingredients_details_popup_closes_it(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_on_first_bun()
        main_page.is_ingredient_details_popup_show()
        main_page.click_close_popup_details()
        assert main_page.is_ingredients_details_popup_closes()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_when_ingredient_added_to_order_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        original_value = main_page.get_bun_counter_value()
        main_page.drag_and_drop_bun_into_constructor()
        new_value = main_page.get_bun_counter_value()
        assert main_page.is_ingredient_counter_increases(original_value, new_value)
