import uuid

import pytest
import allure
from api.account_api import AccountApi


@allure.feature("Account API")
@allure.story("Регистрация и авторизация")
class TestAccountApi:
    @allure.title("Создание нового пользователя")
    def test_create_user(self, base_url):

        account_api = AccountApi(base_url)
        unique_id = str(uuid.uuid4())[:8]
        user_name = f"testuser_{unique_id}"
        password = "Test@Password123!"

        user_data = account_api.create_user(user_name, password)

        assert user_data.get("username") == user_name
        assert user_data.get("userID") is not None
        assert user_data.get("books") == []

    @allure.title("Генерация токена для существующего пользователя")
    def test_generate_token(self, base_url, registered_user):
        user_name, password, user_uuid = registered_user
        account_api = AccountApi(base_url)

        token_data = account_api.generate_token(user_name, password)

        assert token_data["status"] == "Success"
        assert token_data["result"] == "User authorized successfully."
        assert token_data["token"] is not None
        assert token_data["expires"] is not None
