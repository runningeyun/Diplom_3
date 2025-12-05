import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed import OrderFeed


class TestOrderFeed:

    @allure.title('При создании нового заказа счётчики выполненных заказов увеличивается')
    @allure.description('Проверка увеличения счётчиков заказов при оформлении нового заказа авторизированным пользователем')
    @pytest.mark.parametrize('duration', ['total', 'today'])
    def test_when_create_new_order_total_order_count_increases(self, user_login, duration):
        main_page = MainPage(user_login)
        order_page = OrderFeed(user_login)
        main_page.click_on_order_feed_button()
        original_count = order_page.get_number_of_orders_created(duration)
        main_page.get_main_page()
        main_page.drag_and_drop_bun_into_constructor()
        main_page.click_on_create_order()
        order_page.get_order_feed_page()
        new_count = order_page.get_number_of_orders_created(duration)
        assert order_page.is_number_of_orders_increased(original_count, new_count), f'Было {original_count}, стало {new_count}'

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_in_progress_section(self, user_login):
        main_page = MainPage(user_login)
        order_page = OrderFeed(user_login)
        main_page.click_on_order_feed_button()
        original_orders = order_page.get_number_of_orders_in_progress()
        main_page.get_main_page()
        main_page.drag_and_drop_bun_into_constructor()
        main_page.click_on_create_order()
        order_page.get_order_feed_page()
        new_orders = order_page.get_number_of_orders_in_progress()
        assert order_page.is_new_order_add_to_progress(original_orders, new_orders)
