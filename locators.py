from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_ENTER_REGISTER = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    BUTTON_NO_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    BUTTON_POST_AD = (By.XPATH, "//button[@class='buttonPrimary inButtonText undefined inButtonText']")
    BUTTON_PUBLISH = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    BUTTON_MY_ADVERTISEMENT = (By.XPATH, "//div[@class='grid_threeColumns__ldn5D']")
    PROFILE_AVATAR = (By.CLASS_NAME, "svgSmall")
    ERROR_FIELDS = {
        'email': (By.CLASS_NAME, "input_span__yWPqB"),
        'password': (By.CLASS_NAME, "input_inputError__fLUP9"),
        'password_repeat': (By.CLASS_NAME, "input_inputError__fLUP9"),
    }

class UserRegistration:
    REG_EMAIL_INPUT = (By.NAME, "email")
    REG_PASSWORD_INPUT = (By.NAME, "password")
    REG_PASSWORD_REPEAT_INPUT = (By.NAME, "submitPassword")
    REG_NAME_INPUT = (By.NAME, "name")

class UserLogin:
    LOGIN_EMAIL_INPUT = (By.NAME, "email")
    LOGIN_PASSWORD_INPUT = (By.NAME, "password")

class CreateAdvertisement:
    AD_TITLE_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    AD_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    AD_PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROP_DOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CATEGORY_CAR = (By.XPATH, "//button[@class='dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP']")
    CITY_DROP_DOWN = (By.XPATH, "//input[@name='city']//following-sibling::button")
    CITY_NOVOSIBIRSK = (By.XPATH, "//span[contains(text(), 'Новосибирск')]")
    CONDITION_RADIO_BUTTONS = (By.CLASS_NAME,"radioUnput_inputActive__eC-HY")
    MODAL_AUTH_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление')]")
    AD_TITLE = (By.XPATH,"//div[@class='card']")
    AD_DESCRIPTION = (By.XPATH, "//div[@class='description']")


