from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import pytest
from locators.registration_locators import RegistrationLocators
from pages.registration_page import RegistrationPage


class TestRegistration:

    @allure.title("Регистрация с валидными данными")
    def test_successful_registration(self, driver, base_url, test_data):
        driver.get(f"{base_url}/register")
        registration_page = RegistrationPage(driver)

        registration_page.registration(
            test_data["reg_firstname"],
            test_data["reg_lastname"],
            test_data["reg_username"],
            test_data["reg_password"],
        )

        wait = WebDriverWait(driver, 5)

        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        expected_text = "User Registered Successfully."
        assert alert_text == expected_text
        alert.accept()

        wait.until(EC.url_to_be("https://demoqa.com/login"))
        assert driver.current_url == "https://demoqa.com/login"

    @allure.title("Регистрация с невалидными данными")
    @pytest.mark.parametrize(
        "firstname,lastname,username,password,expected_error",
        [
            (
                "invalid",
                "w",
                "1",
                "#",
                "IPasswords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.",
            ),
        ],
    )
    def test_registration_with_invalid_data(
        self, driver, base_url, firstname, lastname, username, password, expected_error
    ):
        driver.get(f"{base_url}/register")
        registration_page = RegistrationPage(driver)

        registration_page.registration(firstname, lastname, username, password)
        error = registration_page.get_error_message()

        assert expected_error in error

    @allure.title("Логин с пустыми данными")
    @pytest.mark.parametrize(
        "firstname,lastname,username,password",
        [
            ("", "", "", ""),
        ],
    )
    def test_registration_with_empty_data(
        self,
        driver,
        base_url,
        firstname,
        lastname,
        username,
        password,
    ):
        driver.get(f"{base_url}/register")
        registration_page = RegistrationPage(driver)

        registration_page.registration(firstname, lastname, username, password)

        input_f = registration_page.get_error_input(
            RegistrationLocators.FIRSTNAME_INPUT
        )
        input_l = registration_page.get_error_input(RegistrationLocators.LASTNAME_INPUT)
        input_n = registration_page.get_error_input(RegistrationLocators.USERNAME_INPUT)
        input_p = registration_page.get_error_input(RegistrationLocators.PASSWORD_INPUT)

        classes_f = input_f.get_attribute("class")
        classes_l = input_l.get_attribute("class")
        classes_n = input_n.get_attribute("class")
        classes_p = input_p.get_attribute("class")

        assert classes_f is not None and "is-invalid" in classes_f
        assert classes_l is not None and "is-invalid" in classes_l
        assert classes_n is not None and "is-invalid" in classes_n
        assert classes_p is not None and "is-invalid" in classes_p

    @allure.title("Переход на страницу логина по нажатию на кнопку 'Back to login'")
    def test_login_button(self, driver, base_url):
        driver.get(f"{base_url}/register")
        registration_page = RegistrationPage(driver)

        registration_page.click_login_button()

        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_to_be("https://demoqa.com/login"))

        assert driver.current_url == "https://demoqa.com/login"
