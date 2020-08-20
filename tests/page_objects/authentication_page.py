from selenium.webdriver.common.by import By
from .helper import wait_visible


class Authentication:
    """Class that defines the `Authentication` objects and methods."""

    def __init__(self, driver):
        """ Web Elements."""
        self._driver = driver
        self._user_input = (By.CSS_SELECTOR, 'input:not([type="password"])')
        self._password_input = (By.CSS_SELECTOR, 'input[type="password"]')
        self._login_button = (By.XPATH, '//div[contains(text(),"Login")]')
        self._body = (By.CSS_SELECTOR, 'body')


    def login(self, user_name, password):
        wait_visible(self._driver, self._user_input)
        user_field = self._driver.find_element(*self._user_input)
        password_field = self._driver.find_element(*self._password_input)
        login_button = self._driver.find_element(*self._login_button)
        user_field.send_keys(user_name)
        password_field.send_keys(password)
        login_button.click()
        wait_visible(self._driver, self._body)
