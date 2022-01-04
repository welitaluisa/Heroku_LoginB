from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _submit_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _failure_message_error = {'by': By.CSS_SELECTOR, 'value': '.flash.error'}
    _failure_message_success = {'by': By.CSS_SELECTOR, 'value': '.flash.Success'}
    _login_form = {'by': By.ID, 'value': 'login'}
