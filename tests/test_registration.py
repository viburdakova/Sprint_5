import random
import string

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, base_url
from locators import *


def generate_unique_email():
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_str}@mail.com"

def generate_invalid_email():
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_str}123123"

class TestRegistration:

    @allure.title("Регистрация пользователя")
    def test_register_new_user(self, driver, base_url):
        email = generate_unique_email()
        driver.get(base_url)

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ENTER_REGISTER)
        ).click()

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_NO_ACCOUNT)
        ).click()

        email_input = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(UserRegistration.REG_EMAIL_INPUT)
        )
        email_input.send_keys(email)

        driver.find_element(*UserRegistration.REG_PASSWORD_INPUT).send_keys("Password123!")
        driver.find_element(*UserRegistration.REG_PASSWORD_REPEAT_INPUT).send_keys("Password123!")

        driver.find_element(*MainPageLocators.BUTTON_CREATE_ACCOUNT).click()

        wait = WebDriverWait(driver, 2)
        avatar_element = wait.until(
            EC.visibility_of_element_located(MainPageLocators.PROFILE_AVATAR)
        )

        assert avatar_element.is_displayed()

    @allure.title("Регистрация пользователя c email не по маске  *******@*******.***")
    def test_register_with_invalid_email_format(self, driver, base_url):
        invalid_email = generate_invalid_email()
        driver.get(base_url)

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ENTER_REGISTER)
        ).click()

        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_NO_ACCOUNT)
        ).click()

        email_input = driver.find_element(*UserRegistration.REG_EMAIL_INPUT)
        email_input.send_keys(invalid_email)
        driver.find_element(*UserRegistration.REG_PASSWORD_INPUT).send_keys("Password123!")
        driver.find_element(*UserRegistration.REG_PASSWORD_REPEAT_INPUT).send_keys("Password123!")

        driver.find_element(*MainPageLocators.BUTTON_CREATE_ACCOUNT).click()

        error_message_element = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(MainPageLocators.ERROR_FIELDS['email'])
        )

        actual_error_text = error_message_element.text

        expected_error_text = "Ошибка"

        assert actual_error_text == expected_error_text, \
            f"Expected error message '{expected_error_text}', but got '{actual_error_text}'"

    @allure.title("Регистрация уже существующего пользователя")
    def test_register_existing_user(self, driver, base_url):
        existing_email = "burdakovavi@mail.ru"
        driver.get(base_url)

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ENTER_REGISTER)
        ).click()

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_NO_ACCOUNT)
        ).click()

        email_input = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(UserRegistration.REG_EMAIL_INPUT)
        )
        email_input.send_keys(existing_email)

        driver.find_element(*UserRegistration.REG_PASSWORD_INPUT).send_keys("ExistingPassword!")
        driver.find_element(*UserRegistration.REG_PASSWORD_REPEAT_INPUT).send_keys("ExistingPassword!")

        driver.find_element(*MainPageLocators.BUTTON_CREATE_ACCOUNT).click()

        error_fields_present = False
        for key in ('email', 'password', 'password_repeat'):
            elems = WebDriverWait(driver, 2).until(
                EC.presence_of_all_elements_located(MainPageLocators.ERROR_FIELDS[key])
            )
            if elems and any(elem.is_displayed() for elem in elems):
                error_fields_present = True
                break

        assert error_fields_present
