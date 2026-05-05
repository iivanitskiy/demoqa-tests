from selenium.webdriver.common.by import By

class RegistrationLocators:
    FIRSTNAME_INPUT = (By.ID, "firstname")
    LASTNAME_INPUT = (By.ID, "lastname")
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    REGISTRATION_BUTTON = (By.ID, "register")
    LOGIN_BUTTON = (By.ID, "gotologin")
    ERROR_MESSAGE = (By.ID, "name")
