import allure
from api.base_api import BaseApi


class AccountApi(BaseApi):
    """
    API-объект для эндпоинтов из раздела Account в Swagger:
    POST /Account/v1/User, POST /Account/v1/GenerateToken и др.
    """

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.user_endpoint = "/Account/v1/User"
        self.token_endpoint = "/Account/v1/GenerateToken"
        self.authorized_endpoint = "/Account/v1/Authorized"

    @allure.step("Создать нового пользователя (POST /Account/v1/User)")
    def create_user(self, user_name: str, password: str):
        payload = {"userName": user_name, "password": password}
        response = self.post(self.user_endpoint, json=payload)

        return response.json()

    @allure.step("Сгенерировать токен для пользователя {user_name}")
    def generate_token(self, user_name: str, password: str):
        payload = {"userName": user_name, "password": password}
        response = self.post(self.token_endpoint, json=payload)
        return response.json()

    @allure.step("Проверить авторизацию пользователя {user_name}")
    def check_authorized(self, user_name: str, password: str):
        payload = {"userName": user_name, "password": password}

        response = self.post(self.authorized_endpoint, json=payload)
        return response.json()

    @allure.step("Получить данные пользователя по UUID: {user_uuid}")
    def get_user_info(self, user_uuid: str, token: str):
        """Требует токен"""
        self.set_auth_token(token)
        endpoint = f"{self.user_endpoint}/{user_uuid}"
        response = self.get(endpoint)
        return response.json()
