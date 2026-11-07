import pytest
import allure

from selenium import webdriver

from data import (
    REGISTER_URL
)

from generators import generate_user

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера: chrome или firefox"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1440,1000")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1440")
        options.add_argument("--height=1000")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(
            f"Неизвестный браузер: {browser}"
        )

    driver.implicitly_wait(0)

    yield driver

    driver.quit()

# Создание и авторизация уникального пользователя
@pytest.fixture
def user(driver):
    user_data = generate_user()

    main_page = MainPage(driver)
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу регистрации"):
        main_page.open(REGISTER_URL)

    with allure.step("Зарегистрировать пользователя"):
        register_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )

    with allure.step("Дождаться страницы авторизации"):
        login_page.wait_url_contains("/login")

    with allure.step("Авторизовать пользователя"):
        login_page.login(
            user_data["email"],
            user_data["password"]
        )

    login_page.wait_url_contains("/")

    yield user_data

    with allure.step("Завершить пользовательскую сессию"):
        driver.delete_all_cookies()
