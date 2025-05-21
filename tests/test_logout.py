import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from data import BASE_URL, email, password

from locators import *


class TestLogout:

    @allure.title("Logout пользователя")
    def test_logout_user(self, driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ENTER_REGISTER)
        ).click()

        login_email = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(UserLogin.LOGIN_EMAIL_INPUT)
        )
        login_password = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(UserLogin.LOGIN_PASSWORD_INPUT)
        )

        login_email.send_keys(email)
        login_password.send_keys(password)

        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN)
        ).click()

        logout_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGOUT)
        )
        logout_button.click()

        avatar_element = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(MainPageLocators.BUTTON_ENTER_REGISTER)
        )
        assert avatar_element.is_displayed()
