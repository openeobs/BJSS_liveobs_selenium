"""
Common Functionality for Mobile
This class contains common functionality for the mobile frontend such as:
- navigating to a particular URL
"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from ui.selectors.menu_selectors import TASK_ITEM, PATIENT_ITEM, LOGOUT_BUTTON
from ui.selectors.list import LIST_CONTAINER


class BaseMobilePage(object):
    """
        Base class to initialise the base page
        that will be called from all pages
    """
    def __init__(self, driver):
        self.driver = driver
        self.default_wait = 20

    def go_to_task_list(self):
        """
            Navigate to the task list
        """
        task_list_item = self.driver.find_element(*TASK_ITEM)
        task_list_item.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(LIST_CONTAINER)
        )

    def go_to_patient_list(self):
        """
            Navigate to the patient list
        """
        patient_list_item = \
            self.driver.find_element(*PATIENT_ITEM)
        patient_list_item.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(LIST_CONTAINER)
        )

    def logout(self):
        """
            Log out of the app
        """
        logout = self.driver.find_element(*LOGOUT_BUTTON)
        logout.click()
