
# =========================
# Главная страница
# =========================
MODAL_LOADING = (
    "css selector",
    "img[class*='Modal_modal__loading']"
)

LOGIN_ACCOUNT_BUTTON = (
    "xpath",
    "//button[contains(., 'Войти в аккаунт')]"
)

PERSONAL_ACCOUNT_BUTTON = (
    "xpath",
    "//a[contains(@href, '/account')]"
)

CONSTRUCTOR_BUTTON = (
    "xpath",
    "//a[.//p[normalize-space()='Конструктор']]"
)

ORDERS_FEED_BUTTON = (
    "xpath",
    "//a[.//p[normalize-space()='Лента Заказов']]"
)

STELLAR_BURGERS_LOGO = (
    "xpath",
    "//header//a[@href='/']"
)


# =========================
# Регистрация
# =========================

NAME_INPUT = (
    "xpath",
    "(//input[@name='name'])[1]"
)

REGISTER_EMAIL_INPUT = (
    "xpath",
    "(//input[@name='name' and @type='text'])[last()]"
)

REGISTER_PASSWORD_INPUT = (
    "xpath",
    "//input[@name='Пароль']"
)

REGISTER_BUTTON = (
    "xpath",
    "//button[contains(., 'Зарегистрироваться')]"
)

LOGIN_FROM_REGISTER_BUTTON = (
    "xpath",
    "//a[contains(., 'Войти')]"
)

PASSWORD_ERROR = (
    "xpath",
    "//*[contains(text(), 'Некорректный пароль')]"
)


# =========================
# Восстановление пароля
# =========================

LOGIN_FROM_FORGOT_BUTTON = (
    "xpath",
    "//a[contains(., 'Войти')]"
)


# =========================
# Авторизация
# =========================

LOGIN_TITLE = (
    "xpath",
    "//h2[normalize-space()='Вход']"
)

LOGIN_EMAIL_INPUT = (
    "xpath",
    "//h2[normalize-space()='Вход']"
    "/following::input[@type='text' and @name='name'][1]"
)

LOGIN_PASSWORD_INPUT = (
    "xpath",
    "//h2[normalize-space()='Вход']"
    "/following::input[@type='password' and @name='Пароль'][1]"
)

LOGIN_BUTTON = (
    "xpath",
    "//h2[normalize-space()='Вход']"
    "/following::button[normalize-space()='Войти'][1]"
)

REGISTER_FROM_LOGIN_BUTTON = (
    "xpath",
    "//a[contains(., 'Зарегистрироваться')]"
)

FORGOT_PASSWORD_BUTTON = (
    "xpath",
    "//a[contains(., 'Восстановить пароль')]"
)


# =========================
# Личный кабинет
# =========================

LOGOUT_BUTTON = (
    "xpath",
    "//button[@type='button' and normalize-space()='Выход']"
)


# =========================
# Конструктор
# =========================

CONSTRUCTOR_TITLE = (
    "xpath",
    "//h1[normalize-space()='Соберите бургер']"
)

BUNS_TAB = (
    "xpath",
    "//span[contains(text(), 'Булки')]/.."
)

SAUCES_TAB = (
    "xpath",
    "//span[contains(text(), 'Соусы')]/.."
)

FILLINGS_TAB = (
    "xpath",
    "//span[contains(text(), 'Начинки')]/.."
)

INGREDIENT_CARDS = (
    "css selector",
    "a[class*='BurgerIngredient_ingredient']"
)

INGREDIENT_NAME = (
    "xpath",
    ".//*[contains(@class, 'text_type_main-default')]"
)

INGREDIENT_PRICE = (
    "xpath",
    ".//*[contains(@class, 'price')]"
)

INGREDIENT_COUNTER = (
    "css selector",
    "div[class*='counter_counter__']"
)

INGREDIENT_COUNTER_NUMBER = (
    "css selector",
    "p[class*='counter_counter__num__']"
)

INGREDIENT_ADD_BUTTON = (
    "xpath",
    ".//button[contains(., 'Добавить')]"
)

MODAL_WINDOW = (
    "css selector",
    "div.Modal_modal__container__Wo2l_"
)

MODAL_CLOSE_BUTTON = (
    "css selector",
    "button.Modal_modal__close__TnseK"
)

MODAL_TITLE = (
    "css selector",
    "[class*='Modal_header']"
)

MODAL_INGREDIENT_DETAILS = (
    "css selector",
    "[class*='ingredient-details']"
)

ORDER_BUTTON = (
    "xpath",
    "//button[contains(., 'Оформить заказ')]"
)

ORDER_NUMBER = (
    "css selector",
    "h2[class*='Modal_modal__title__']"
)

ORDER_SUCCESS_MODAL = (
    "css selector",
    "[class*='Modal_modal']"
)

MODAL_OVERLAY = (
    "css selector",
    "div[class*='Modal_modal_overlay']"
)

BURGER_CONSTRUCTOR = (
    "css selector",
    "ul[class*='BurgerConstructor_basket__list']"
)

# =========================
# Лента заказов
# =========================

ORDERS_FEED_TITLE = (
    "xpath",
    "//h1[contains(., 'Лента заказов')]"
)

ALL_TIME_ORDERS_COUNTER = (
    "xpath",
    "//p[normalize-space()='Выполнено за все время:']"
    "/following-sibling::p"
)

TODAY_ORDERS_COUNTER = (
    "xpath",
    "//p[normalize-space()='Выполнено за сегодня:']"
    "/following-sibling::p"
)

IN_PROGRESS_SECTION = (
    "xpath",
    "//p[normalize-space()='В работе:']"
)

IN_PROGRESS_ORDERS = (
    "css selector",
    "ul[class*='OrderFeed_orderListReady'] li"
)

MODAL_LOADING_WINDOW = (
    "css selector",
    "div.Modal_modal__P3_V5"
)