import allure

from pages.base_page import BasePage
from locators import (
    LOGIN_ACCOUNT_BUTTON,
    PERSONAL_ACCOUNT_BUTTON,
    CONSTRUCTOR_BUTTON,
    ORDERS_FEED_BUTTON,
    STELLAR_BURGERS_LOGO,
    MODAL_LOADING
)


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self, url):
        self.open_url(url)

    @allure.step("Перейти к авторизации")
    def click_login_account(self):
        self.click(LOGIN_ACCOUNT_BUTTON)

    @allure.step("Перейти в личный кабинет")
    def click_personal_account(self):
        self.click(PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self.wait_invisibility(MODAL_LOADING)
        self.click(CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в ленту заказов")
    def click_orders_feed(self):
        self.wait_invisibility(MODAL_LOADING)
        self.click(ORDERS_FEED_BUTTON)

    @allure.step("Кликнуть по логотипу Stellar Burgers")
    def click_logo(self):
        self.click(STELLAR_BURGERS_LOGO)
