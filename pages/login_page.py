import allure

from pages.base_page import BasePage
from locators import (
    LOGIN_TITLE,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON,
    REGISTER_FROM_LOGIN_BUTTON,
    FORGOT_PASSWORD_BUTTON
)


class LoginPage(BasePage):

    @allure.step("Проверить отображение формы входа")
    def is_login_page_displayed(self):
        return self.is_displayed(LOGIN_TITLE)

    @allure.step("Авторизоваться пользователем")
    def login(self, email, password):
        self.send_keys(LOGIN_EMAIL_INPUT, email)
        self.send_keys(LOGIN_PASSWORD_INPUT, password)
        self.click(LOGIN_BUTTON)

    @allure.step("Перейти на страницу регистрации")
    def click_register(self):
        self.click(REGISTER_FROM_LOGIN_BUTTON)

    @allure.step("Перейти к восстановлению пароля")
    def click_forgot_password(self):
        self.click(FORGOT_PASSWORD_BUTTON)
