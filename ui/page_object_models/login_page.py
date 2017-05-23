"""
Page Object Model for Login Page
The login page handles logging into the application
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from ui.page_object_models.mobile_common import BaseMobilePage
from ui.selectors.login_page_selectors import USERNAME_FIELD, PASSWORD_FIELD, \
    SUBMIT_BUTTON, DATABASE_DROPDOWN


class LoginPage(BaseMobilePage):
    """
    Class that handles interaction with the Login Page on Mobile
    """

    def login(self, username, password, database='nhclinical'):
        """
        Fill out the login form and press the submit button
        
        :param username: Username to login with
        :param password: Password for the username supplied
        :param database: Name of the database to log into if the 
            database selection element is visible
        """
        username_e = self.driver.find_element(*USERNAME_FIELD)
        password_e = self.driver.find_element(*PASSWORD_FIELD)
        login_button = self.driver.find_element(*SUBMIT_BUTTON)
        try:
            database_selector = self.driver.find_element(
                *DATABASE_DROPDOWN
            )
            Select(database_selector).select_by_value(database)
        except NoSuchElementException:
            pass

        username_e.send_keys(username)
        password_e.send_keys(password)
        login_button.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(USERNAME_FIELD)
        )

    def is_login_page(self):
        """
        Verify that we are indeed on the login page
        
        :return: if current page is the login page
        """
        return '/mobile/login' in self.driver.current_url
