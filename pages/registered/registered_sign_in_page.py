import logging
from utility.support.ui_helpers import UIHelpers
import utility.framework.logger_utility as log_utils
from locators.registered.signIn_page_locators import SignInPageLocators,SignInPageLocatorsStaticText
from locators.common.page_title_info import FlowPageFlowTitle
from locators.common.forgot_username_page_locators import ForgotUsernamePageLocators
from locators.common.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.common.scan_photo_id_page_locators import ScanPhotoIDPageLocators,ScanPhotoIDPageLocatorsStaticText

class RegisteredSignInPage(UIHelpers):
    """This class defines the method and element identifications for Sign In Screen."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        #self.ui_helpers = UIHelpers(driver)
        self.locator = SignInPageLocators()
        self.locator_page_static_text = SignInPageLocatorsStaticText()
        super(RegisteredSignInPage, self).__init__(driver)

    def verify_page_title(self):
        """
        Verify Sign In Page Title
        :return: True | False
        """
        result = True

        element_text = self.get_element_text(*self.locator.sign_in_page_title)

        if element_text.strip() != FlowPageFlowTitle.sign_in_page_title.strip():
            self.log.info("Expected is {}".format(FlowPageFlowTitle.sign_in_page_title))
            self.log.error("Result mismatched and actual result is  -- {}".format(element_text))
            result = False

        return result

    def verify_static_text_elements_available(self):
        """
        Verify Static Texts elements available in the page like "Not register yet?,Username,Password
        :return: True | False
        """

        result = True

        not_registered_create_account_yet_element = self.get_element_text(*self.locator.not_registered_create_account_text)
        username_label_element = self.get_element_text(*self.locator.username_label)
        password_label_element = self.get_element_text(*self.locator.password_label)

        if not_registered_create_account_yet_element.strip() != self.locator_page_static_text.not_registered_create_account.strip():
            self.log.info("Expected is {}".format(self.locator_page_static_text.not_registered_create_account))
            self.log.error("Result mismatched and actual result is  -- {}".format(not_registered_create_account_yet_element))
            result = False

        if username_label_element.strip() != self.locator_page_static_text.username_label_text.strip():
            self.log.info("Expected is {}".format(self.locator_page_static_text.username_label_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(username_label_element))
            result = False

        if password_label_element.strip() != self.locator_page_static_text.password_label_text.strip():
            self.log.info("Expected is {}".format(self.locator_page_static_text.password_label_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(password_label_element))
            result = False

        return result

    def verify_text_link_elements_available(self):
        """
        Verify texts available in link text elements available in the page like "Create an account?,Forgot your username?,Forgot your password?
        :return: True | False
        """
        result = True

        forgot_username_element = self.get_element_text(*self.locator.forgot_username_text_link)
        forgot_password = self.get_element_text(*self.locator.forgot_password_text_link)
        sign_in_button = self.get_element_text(*self.locator.sign_in_button)

        if forgot_username_element.strip() != self.locator_page_static_text.forgot_username_link_text.strip():
            self.log.info("Expected is {}".format(self.locator_page_static_text.forgot_username_link_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(forgot_username_element))
            result = False

        if forgot_password.strip() != self.locator_page_static_text.forgot_password_link_text.strip():
            self.log.info("Expected is {}".format(self.locator_page_static_text.forgot_password_link_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(forgot_password))
            result = False

        if sign_in_button.strip() != self.locator_page_static_text.sign_in_button_text.strip():
            self.log.info("Expected is {}".format(self.locator_page_static_text.sign_in_button_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(sign_in_button))
            result = False

        return result

    def verify_create_an_account_redirection(self):
        """
        Verify redirection to "Create an Account" screen while taping on Create an Account text link
        :return: True | False
        """
        result = True

        element_available = self.wait_for_element_to_be_clickable(*self.locator.not_registered_create_account_text)
        element_available.click()
        self.wait_for_sync(10)

        if (not element_available):
            self.log.error("Create an Account text link element is not clickable")
            result = False

        if self.get_element_text(*ScanPhotoIDPageLocators.scan_review_page_title).strip() != FlowPageFlowTitle.scan_photo_id_screen_title.strip():
            self.log.info("Expected Page redirection and Page Title is {}".format(FlowPageFlowTitle.scan_photo_id_screen_title))
            self.log.error("Actual Page redirection and Page Title is {}".format(self.get_element_text(*ScanPhotoIDPageLocators.scan_review_page_title).strip()))
            result = False

        return result

    def verify_forgot_username_redirection(self):
        """
        Verify redirection to "Forgot Username" screen while taping on Forgot your username? text link
        :return: True | False
        """
        result = True

        element_available = self.wait_for_element_to_be_clickable(*self.locator.forgot_username_text_link)
        element_available.click()
        self.wait_for_sync(10)

        if (not element_available):
            self.log.error("Forgot your username? text link element is not clickable")
            result = False

        if self.get_element_text(*ForgotUsernamePageLocators.forgot_username_page_title).strip() != FlowPageFlowTitle.forgot_username_page_title.strip():
            self.log.info("Expected Page redirection and Page Title is {}".format(FlowPageFlowTitle.forgot_username_page_title))
            self.log.error("Actual Page redirection and Page Title is {}".format(self.get_element_text(*ForgotUsernamePageLocators.forgot_username_page_title).strip()))
            result = False

        return result

    def verify_forgot_password_redirection(self):
        """
        Verify redirection to "Forgot Password" screen while taping on Forgot your password? text link
        :return: True | False
        """
        result = True

        element_available = self.wait_for_element_to_be_clickable(*self.locator.forgot_password_text_link)
        element_available.click()
        self.wait_for_sync(10)

        if (not element_available):
            self.log.error("Forgot your password? text link element is not clickable")
            result = False

        if self.get_element_text(*ForgotPasswordPageLocators.forgot_password_page_title).strip() != FlowPageFlowTitle.forgot_password_page_title.strip():
            self.log.info("Expected Page redirection and Page Title is {}".format(FlowPageFlowTitle.forgot_password_page_title))
            self.log.error("Actual Page redirection and Page Title is {}".format(self.get_element_text(*ForgotPasswordPageLocators.forgot_password_page_title).strip()))
            result = False

        return result

    def click_back_arrow_navigation(self):
        """
        Click  back arrow navigation
        :return: True | False
        """
        result = True

        element_available = self.get_element(*SignInPageLocators.sign_in_back_arrow_navigation)
        element_available.click()
        self.wait_for_sync(10)

    def verify_enter_login_credentials_redirection(self, login_data_record):
        """
        Verify redirection to Appointment Type screen once logged in with valid credentials
        :param login_data_record: login_data_record as json/dict
        :return: True | False
        """
        result = True

        self.get_element(*self.locator.username_input_field).clear()
        self.get_element(*self.locator.password_input_field).clear()

        self.get_element(*self.locator.username_input_field).send_keys(login_data_record['username'])
        self.get_element(*self.locator.password_input_field).send_keys(login_data_record['password'])

        element_available = self.wait_for_element_to_be_clickable(*self.locator.sign_in_button)

        if (not element_available):
            self.log.error("Sign In button element is not clickable")
            result = False

        element_available.click()
        self.wait_for_sync(20)

        return result

    def verify_enter_login_credentials_redirection_generic(self,user_category=None, user_name_type=None, brand_name=None):
        """
        Verify redirection to another screen once logged in with valid credentials without status return
        :return: NA
        """
        from utility.framework.data_reader_utility import DataReader

        login_data_record = DataReader().fetch_registered_user_data_from_json_file(user_category, user_name_type, brand_name)

        self.get_element(*self.locator.username_input_field).send_keys(login_data_record['username'])
        self.get_element(*self.locator.password_input_field).send_keys(login_data_record['password'])

        element_available = self.wait_for_element_to_be_clickable(*self.locator.sign_in_button)

        if (not element_available):
            self.log.error("Sign In button element is not clickable")

        element_available.click()
        self.wait_for_sync(20)







