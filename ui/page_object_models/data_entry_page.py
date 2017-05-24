"""
Page Object Model for Data Entry Page
The Data Entry Page allows the user to submit observations and escalation tasks
"""

import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ui.page_object_models.mobile_common import BaseMobilePage
from ui.selectors.form import PATIENT_INFO_BUTTON, FORM_CANCEL_BUTTON, \
    FORM_SUBMIT_BUTTON
from ui.selectors.data_entry_selectors import PATIENT_INFO_POPUP, \
    FULL_SCREEN_PATIENT_INFO_BUTTON, PATIENT_INFO_POPUP_CLOSE_BUTTON
from ui.selectors.modal import \
    FULLSCREEN_MODAL, FULLSCREEN_MODAL_BUTTON, MODAL_DIALOG


class DataEntryPage(BaseMobilePage):
    """
    Class that handles interacting with the data entry form
    """

    def open_patient_info(self):
        """
        Open the patient information popup in the floating header
        """
        patient_info_button = self.driver.find_element(*PATIENT_INFO_BUTTON)
        patient_info_button.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(PATIENT_INFO_POPUP)
        )

    def close_patient_info(self):
        """
        Close the patient information popup, opened by pressing the button in
        the floating header
        """
        close_button = \
            self.driver.find_element(*PATIENT_INFO_POPUP_CLOSE_BUTTON)
        close_button.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.invisibility_of_element_located(PATIENT_INFO_POPUP)
        )

    def open_full_patient_info(self):
        """
        Open the full screen patient information popup
        """
        full_info_button = \
            self.driver.find_element(*FULL_SCREEN_PATIENT_INFO_BUTTON)
        full_info_button.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(FULLSCREEN_MODAL)
        )

    def close_full_patient_info(self):
        """
        Close the full screen patient information popup
        """
        full_close_button = self.driver.find_element(*FULLSCREEN_MODAL_BUTTON)
        full_close_button.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.invisibility_of_element_located(FULLSCREEN_MODAL)
        )

    def submit_form(self):
        """
        Press the submit button on the form
        """
        form_submit_button = self.driver.find_element(FORM_SUBMIT_BUTTON)
        form_submit_button.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(MODAL_DIALOG)
        )

    def cancel_form(self):
        """
        Press the cancel button on the form (if present)
        """
        form_submit_button = self.driver.find_element(FORM_CANCEL_BUTTON)
        form_submit_button.click()
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.visibility_of_element_located(MODAL_DIALOG)
        )

    def fill_out_form(self, data):
        """
        Using the provided list fill out the form

        Expected Data Format:

        .. code-block:: python

            {
                'name': 'respiration_rate',
                'value': '18',
                'type': 'textbox'
            }


        :data: list of dictionaries that contain field names, value to enter
            and field type
        """
        for field in data:
            value = field.get('value')
            name = field.get('name')
            data_type = field.get('type')

            if data_type == 'select':
                select_field = self.driver.find_element_by_name(name)
                select_select = Select(select_field)
                select_select.select_by_visible_text(value)
                select_field.send_keys(Keys.TAB)
            else:
                input_field = self.driver.find_element_by_name(name)
                input_field.send_keys(value)
                input_field.send_keys(Keys.TAB)
