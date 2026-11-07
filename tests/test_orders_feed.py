import pytest
import allure

from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.orders_page import OrdersPage


@allure.feature("Лента заказов")
class TestOrdersFeed:

    @allure.title(
        "Увеличение счётчика выполненных заказов за всё время"
    )
    def test_all_time_orders_counter_increases(self, driver, user):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        orders_page = OrdersPage(driver)

        main_page.click_orders_feed()

        initial_count = orders_page.get_all_time_counter()

        main_page.click_constructor()

        constructor_page.add_ingredient(0)
        constructor_page.create_order()

        constructor_page.wait_order_success()
        constructor_page.close_order_success_modal()
        main_page.click_orders_feed()

        orders_page.wait_all_time_counter_increases(initial_count)

        actual_count = orders_page.get_all_time_counter()

        assert actual_count > initial_count

    @allure.title(
        "Увеличение счётчика выполненных заказов за сегодня"
    )
    def test_today_orders_counter_increases(self, driver, user):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        orders_page = OrdersPage(driver)

        main_page.click_orders_feed()

        initial_count = orders_page.get_today_counter()

        main_page.click_constructor()

        constructor_page.add_ingredient(0)
        constructor_page.create_order()

        constructor_page.wait_order_success()
        constructor_page.close_order_success_modal()
        main_page.click_orders_feed()

        orders_page.wait_today_counter_increases(initial_count)

        actual_count = orders_page.get_today_counter()

        assert actual_count > initial_count

    @allure.title("Номер созданного заказа появляется в разделе В работе")
    def test_new_order_appears_in_progress(self, driver, user):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        orders_page = OrdersPage(driver)

        constructor_page.add_ingredient(0)
        constructor_page.create_order()
        
        constructor_page.wait_order_success()

        order_number = constructor_page.get_order_number()
        constructor_page.close_order_success_modal()
        main_page.click_orders_feed()
        
        assert orders_page.is_feed_opened()
        assert orders_page.is_order_in_progress(order_number)
