import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from data import BASE_URL, email, password
from locators import *


class TestLogin:

    @allure.title("Login пользователя")
    def test_login_user(self, driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ENTER_REGISTER)
        ).click()

        login_email_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(UserLogin.LOGIN_EMAIL_INPUT)
        )
        login_email_element.click()
        login_email_element.send_keys(email)

        login_password_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(UserLogin.LOGIN_PASSWORD_INPUT)
        )
        login_password_element.click()
        login_password_element.send_keys(password)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN)
        ).click()

        avatar_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PROFILE_AVATAR)
        )

        assert avatar_element.is_displayed()
