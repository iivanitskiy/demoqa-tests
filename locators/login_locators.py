from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    REGISTRATION_BUTTON = (By.ID, "newUser")
    ERROR_MESSAGE = (By.ID, "name")
    SUCCESS_ELEMENT = (By.ID, "userName")

