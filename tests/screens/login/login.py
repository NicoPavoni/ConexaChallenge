from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME_INPUT = (By.ID, 'userName')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login')
    NEW_USER_BTN = (By.ID, 'newUser')

    def get_username_input(self):
        return self.driver.find_element(*self.USERNAME_INPUT)

    def get_password_input(self):
        return self.driver.find_element(*self.PASSWORD_INPUT)

    def get_login_btn(self):
        return self.driver.find_element(*self.LOGIN_BTN)

    def get_new_user_btn(self):
        return self.driver.find_element(*self.NEW_USER_BTN)

    def enter_text_username(self, user):
        username_input = self.get_username_input()
        username_input.send_keys(user)

    def enter_text_password(self, password):
        password_input = self.get_password_input()
        password_input.send_keys(password)

    def click_login_btn(self):
        self.get_login_btn().click()

    def click_new_user_btn(self):
        self.get_new_user_btn().click()
