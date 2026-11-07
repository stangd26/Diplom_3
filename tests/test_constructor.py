import pytest
import allure

from data import BASE_URL
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.orders_page import OrdersPage


@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход в конструктор по кнопке Конструктор")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open(BASE_URL)

        main_page.click_orders_feed()
        main_page.click_constructor()

        assert constructor_page.is_constructor_displayed()

    @allure.title("Переход в ленту заказов")
    def test_click_orders_feed(self, driver):
        main_page = MainPage(driver)
        orders_page = OrdersPage(driver)

        main_page.open(BASE_URL)
        main_page.click_orders_feed()

        orders_page.wait_url_contains("/feed")

        assert orders_page.is_feed_opened()

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open(BASE_URL)
        
        constructor_page.open_ingredient_details()

        assert constructor_page.is_modal_displayed()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open(BASE_URL)

        constructor_page.open_ingredient_details()
        constructor_page.close_ingredient_modal()

        assert not constructor_page.is_modal_displayed()

    @allure.title("Увеличение счётчика после добавления ингредиента")
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        constructor_page = ConstructorPage(driver)
        initial_counter = constructor_page.get_ingredient_counter(0)
       
        constructor_page.add_ingredient(0)
        constructor_page.wait_for_ingredient_counter(0, initial_counter)
        new_counter = constructor_page.get_ingredient_counter(0)

        assert new_counter > initial_counter