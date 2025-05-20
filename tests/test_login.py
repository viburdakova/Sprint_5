import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver, base_url
from locators import *


class TestLogin:

    @allure.title("Login пользователя")
    def test_login_user(self, driver, base_url):
        email = "burdakovavi@mail.ru"
        password = "Btz9Yar29R!CCBx"

        driver.get(base_url)

        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ENTER_REGISTER)
        ).click()

        login_email = driver.find_element(*UserLogin.LOGIN_EMAIL_INPUT)
        login_password = driver.find_element(*UserLogin.LOGIN_PASSWORD_INPUT)

        login_email.send_keys(email)
        login_password.send_keys(password)

        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN)
        ).click()

        wait = WebDriverWait(driver, 2)
        avatar_element = wait.until(
            EC.visibility_of_element_located(MainPageLocators.PROFILE_AVATAR)
        )

        assert avatar_element.is_displayed()
