import string
import random

import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver, base_url
from locators import *


class TestCreateAdvertisement:

    @allure.title("Создание объявления неавторизованным пользователем")
    def test_ad_creation_by_unauthorized_user(self, driver, base_url):
        driver.get(base_url)

        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_POST_AD)
        ).click()

        modal_title = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(CreateAdvertisement.MODAL_AUTH_TITLE)
        )

        expected_title_text = "Чтобы разместить объявление, авторизуйтесь"

        actual_title_text = modal_title.text

        assert modal_title.is_displayed(), "Модальное окно авторизации не отображается"
        assert actual_title_text == expected_title_text, (
            f"Ожидаемый результат: '{expected_title_text}', фактический результат: '{actual_title_text}'"
        )

    @allure.title("Создание объявления авторизованным пользователем")
    def test_create_advertisement(self, driver, base_url):
        email = "burdakovavi@mail.ru"
        password = "Btz9Yar29R!CCBx"

        driver.get(base_url)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_ENTER_REGISTER)
        ).click()

        login_email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(UserLogin.LOGIN_EMAIL_INPUT)
        )
        login_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(UserLogin.LOGIN_PASSWORD_INPUT)
        )

        login_email.send_keys(email)
        login_password.send_keys(password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_LOGIN)
        ).click()

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(MainPageLocators.BUTTON_POST_AD))
            driver.find_element(*MainPageLocators.BUTTON_POST_AD).click()
        except StaleElementReferenceException:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.BUTTON_POST_AD))
            driver.find_element(*MainPageLocators.BUTTON_POST_AD).click()

        title_text = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        description_text = ''.join(random.choices(string.ascii_letters + string.digits + ' ,.', k=50))
        price_value = random.randint(500000, 1000000)

        driver.find_element(*CreateAdvertisement.AD_TITLE_INPUT).send_keys(title_text)

        wait = WebDriverWait(driver, 10)
        ad_description_input = wait.until(
            EC.presence_of_element_located(CreateAdvertisement.AD_DESCRIPTION_INPUT)
        )
        ad_description_input.send_keys(description_text)

        driver.find_element(*CreateAdvertisement.AD_PRICE_INPUT).send_keys(price_value)

        driver.find_element(*CreateAdvertisement.CATEGORY_DROP_DOWN).click()
        driver.find_element(*CreateAdvertisement.CATEGORY_CAR).click()

        driver.find_element(*CreateAdvertisement.CITY_DROP_DOWN).click()
        driver.find_element(*CreateAdvertisement.CITY_NOVOSIBIRSK).click()

        driver.find_element(*CreateAdvertisement.CONDITION_RADIO_BUTTONS).click()

        driver.find_element(*MainPageLocators.BUTTON_PUBLISH).click()

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(MainPageLocators.PROFILE_AVATAR))
            driver.find_element(*MainPageLocators.PROFILE_AVATAR).click()
        except StaleElementReferenceException:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.PROFILE_AVATAR))
            driver.find_element(*MainPageLocators.PROFILE_AVATAR).click()

        wait = WebDriverWait(driver, 10)
        advertisement = wait.until(
            EC.visibility_of_element_located(MainPageLocators.BUTTON_MY_ADVERTISEMENT)
        )

        assert advertisement.is_displayed()

