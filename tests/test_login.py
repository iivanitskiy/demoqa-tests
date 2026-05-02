import allure
import pytest
from locators.login_locators import LoginLocators
from pages.login_page import LoginPage

class TestLogin:

    @allure.step("Логин с валидными данными")
    def test_successful_login(self, driver, base_url, test_data):
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)

        login_page.login(test_data["username"], test_data["password"])

        assert login_page.is_login_successful(), "Login failed"

    @allure.step("Логин с невалидными данными")
    @pytest.mark.parametrize(
        "username,password,expected_error",
        [
            ("invalid", "wrong", "Invalid username or password!"),
        ],
    )
    def test_login_with_invalid_data(
        self, driver, base_url, username, password, expected_error
    ):
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)

        login_page.login(username, password)
        error = login_page.get_error_message()

        assert expected_error in error

    @allure.step("Логин с пустыми данными")
    @pytest.mark.parametrize(
        "username,password,expected_error",
        [
            ("", "pass", "Username is required"),
            ("user", "", "Password is required"),
            ("", "", "Username and password are required"),
        ],
    )
    def test_login_with_empty_data(
        self, driver, base_url, username, password, expected_error
    ):
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)

        login_page.login(username, password)

        input_n = login_page.get_error_input(LoginLocators.USERNAME_INPUT)
        input_p = login_page.get_error_input(LoginLocators.PASSWORD_INPUT)

        classes_n = input_n.get_attribute("class")
        classes_p = input_p.get_attribute("class")

        if expected_error == "Username is required":
            assert (
                classes_n is not None and "is-invalid" in classes_n
            ), "Error class not added to username input"
        elif expected_error == "Password is required":
            assert (
                classes_p is not None and "is-invalid" in classes_p
            ), "Error class not added to password input"
        elif expected_error == "Username and password are required":
            assert (
                classes_n is not None
                and "is-invalid" in classes_n
                and classes_p is not None
                and "is-invalid" in classes_p
            ), "Error class not added to username & password inputs"
