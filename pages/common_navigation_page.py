import logging
from utility.support.ui_helpers import UIHelpers
import utility.framework.logger_utility as log_utils
from locators.common.welcome_page_locators import WelcomePageLocators
from locators.common.appointment_type_page_locators import AppintmentTypePageLocators
from locators.registered.patient_info_page_locators import PatientInfoPageLocators
from locators.common.next_available_page_locators import NextAvailablePageLocators
from locators.registered.signIn_page_locators import SignInPageLocators
from locators.common.your_appointments_page_locators import YourAppointmentsPageLocators

class NavigationPage(UIHelpers):

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.welcome_page_locator = WelcomePageLocators()
        self.patient_info_page_locator = PatientInfoPageLocators()
        self.apptmt_type_info_page_locator = AppintmentTypePageLocators()
        self.next_avail_page_locator = NextAvailablePageLocators()
        self.sign_in_page_locator = SignInPageLocators()
        self.your_appmt_page_locator = YourAppointmentsPageLocators()

    def click_on_sign_in_register_button(self):
        element_available = self.wait_for_element_to_be_clickable(*self.welcome_page_locator.sign_in_reg_button)
        element_available.click()
        self.wait_for_sync(8)

    def click_create_account_text_link(self):
        self.wait_for_element_to_be_clickable(*self.sign_in_page_locator.not_registered_create_account_text).click()
        self.wait_for_sync(6)

    def click_on_apptmt_info_btn(self):
        element_available = self.wait_for_element_to_be_clickable(*self.patient_info_page_locator.apptmt_info_button)
        element_available.click()
        self.wait_for_sync(10)

    def click_on_choose_another_appmnt(self):
        element_available = self.wait_for_element_to_be_clickable(*self.next_avail_page_locator.choose_another_appointment_btn)
        element_available.click()
        self.wait_for_sync(10)

    def click_on_choose_this_appmnt_btn(self):
        element_available = self.wait_for_element_to_be_clickable(*self.next_avail_page_locator.choose_this_appointment_btn)
        element_available.click()
        self.wait_for_sync(10)



