import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import (
    ORDERS_FEED_TITLE,
    ALL_TIME_ORDERS_COUNTER,
    TODAY_ORDERS_COUNTER,
    IN_PROGRESS_SECTION,
    IN_PROGRESS_ORDERS
)


class OrdersPage(BasePage):

    @allure.step("Проверить открытие ленты заказов")
    def is_feed_opened(self):
        return self.is_displayed(ORDERS_FEED_TITLE)

    @allure.step("Дождаться увеличения счётчика заказов за всё время")
    def wait_all_time_counter_increases(self, initial_count):
        self.wait.until(
            lambda _: self.get_all_time_counter() > initial_count
        )


    @allure.step("Дождаться увеличения счётчика заказов за сегодня")
    def wait_today_counter_increases(self, initial_count):
        self.wait.until(
            lambda _: self.get_today_counter() > initial_count
        )

    @allure.step("Получить счётчик выполненных заказов за всё время")
    def get_all_time_counter(self):
        return int(self.get_text(ALL_TIME_ORDERS_COUNTER))

    @allure.step("Получить счётчик заказов за сегодня")
    def get_today_counter(self):
        return int(self.get_text(TODAY_ORDERS_COUNTER))

    @allure.step("Проверить наличие раздела В работе")
    def is_in_progress_displayed(self):
        return self.is_displayed(IN_PROGRESS_SECTION)

    @allure.step("Получить номера заказов в работе")
    def get_in_progress_orders(self):
        orders = self.driver.find_elements(*IN_PROGRESS_ORDERS)
        return [order.text.strip() for order in orders]

    @allure.step("Проверить наличие номера заказа в разделе В работе")
    def is_order_in_progress(self, order_number):
        expected = str(order_number).strip().lstrip("0")

        self.wait.until(
            lambda driver: any(
                number.lstrip("0") == expected
                for number in self.get_in_progress_orders()
            )
        )
        return True
