import logging
import pytest
import allure
import sys
import unittest
import utility.framework.logger_utility as log_utils
from utility.framework.execution_status_utility import ExecutionStatus
from utility.framework.data_reader_utility import DataReader
from utility.framework.config_utility import ConfigUtility
from pages.common.welcome_page import GuestWelcomePage
from pages.registered.header_footer_common_page import HeaderFooterCommonPage

"""
    TODO:: TestCases Pending
    1. Logo Image cross check/Image Validation
    2. Localization change settings to english and spanish
    3. To and back page navigation
    4. Header and Footer section Validation
"""

#unittest.defaultTestLoader.sortTestMethodsUsing = None

@allure.story('[XXXX Android App] - Automate the Welcome Screen Functionality for Registered Users')
@allure.feature('XXXX Android App - Welcome Screen Tests for Registered Users')
@pytest.mark.usefixtures("get_driver")
@pytest.mark.incremental
#class TestWelcomePageForRegistered(unittest.TestCase):
class RegisteredWelcomePageTests(unittest.TestCase):
    """
    This class contains the executable test cases.
    """
    log = log_utils.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        self.data_reader = DataReader()
        self.config_util = ConfigUtility()
        self.welcome_page = GuestWelcomePage(self.driver)
        self.header_footer_page = HeaderFooterCommonPage(self.driver)
        self.exe_status = ExecutionStatus(self.driver)
        self.prop = ConfigUtility()

    @pytest.fixture(autouse=True) # Fixture to get configuration items from command line
    def _request_get_config_params(self, get_config_params):
        self._config_params = get_config_params

    @allure.testcase("Verify Welcome Screen Elements and its functionality")
    @allure.id("TC_CX_AND_REG_WELCOME_SCREEN_001")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login
    #@pytest.mark.run(order=1)
    def test_01_verify_welcome_screen_elements_functionality(self):
        """
        This test is validating the presence of Welcome Screen Elements.
        :return: return test status
        """
        ## Determining the name of the Current Function
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        self.log.info("Config Parameters fetched is {}".format(self._config_params))
        fetched_brand = self.data_reader.fetch_clinic_details(self._config_params['brand'])
        admin_cred = self.data_reader.load_general_info_json()

        with allure.step("Verify presence of Welcome Screen title and admin page navigation if access permission pop up is displayed for clinic selection"):
            result = self.welcome_page.verify_welcome_page_title(admin_username = admin_cred['admin_credentials']['username'], clinic_id = fetched_brand['clinic_id'], admin_pwd = admin_cred['admin_credentials']['password'])
            self.exe_status.mark_final(test_step="Verify presence of Welcome Screen title and admin page navigation if access permission pop up is displayed for clinic selection", result=result)

        with allure.step("Verify the presence of {} Brand Logo/Icon".format(self._config_params['brand'])):
            result = self.header_footer_page.verify_brand_logo_image()
            self.exe_status.mark_final(test_step="Verify the presence of {} Brand Logo/Icon".format(self._config_params['brand']),result=result)

        with allure.step("Verify presence of welcome to medical center name text"):

            result = self.welcome_page.verify_welcome_to_medical_center_text(clinic_name = fetched_brand['medical_center_name'])
            self.log.info("Medical Center Name is {}".format(fetched_brand['medical_center_name']))
            self.exe_status.mark_final(test_step="Verify presence of welcome to medical center name text", result=result)

        with allure.step("Verify presence of Questions about your health.. text"):
            result = self.welcome_page.verify_questions_about_your_health_text()
            self.exe_status.mark_final(test_step="Verify presence of Questions about your health.. text", result=result)

        with allure.step("Verify the presence of Sign In/Register button available and its text"):
            result = self.welcome_page.verify_availability_of_sign_in_or_register_button()
            self.exe_status.mark_final(test_step="Verify the presence of Sign In/Register button available and its text", result=result)

        with allure.step("Verify the presence of Create Account link text available and its text"):
            result = self.welcome_page.verify_availability_of_create_account_link_text()
            self.exe_status.mark_final(test_step="Verify the presence of Create Account link text available and its text", result=result)

        # with allure.step("Verify the presence of Language/Localization dropdown box and its options available"):
        #     result = self.welcome_page.verify_language_selector_dropdown_availbility_and_its_options()
        #     self.exe_status.mark_final(test_step="Verify the presence of Language/Localization dropdown box and its options available", result=result)
        #
        # with allure.step("Verify the presence of Language/Localization dropdown box's English option available and verify its behavior"):
        #     result = self.welcome_page.verify_language_selector_dropdown_availbility_and_by_selecting_english_option()
        #     self.exe_status.mark_final(test_step="Verify the presence of Language/Localization dropdown box's English option available and verify its behavior",result=result)

    @allure.testcase("Verify the redirection to Sign In screen upon clicking Sign In / Register button")
    @allure.id("TC_CX_AND_REG_WELCOME_SCREEN_002")
    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.run(order=2)
    def test_02_verify_sign_in_reg_button_redirection(self):
        """
            This test is to validate the redirection of Sign In screen while clicking on Sign In / Register Button
            :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step("Verify whether user is redirected to Sign In Screen"):
            result = self.welcome_page.verify_sign_in_register_button_redirection()
            self.exe_status.mark_final(test_step="Verify whether user is redirected to Sign In Screen", result=result)

    @allure.testcase("Verify the redirection to Sign In screen for Sign In process flow")
    @allure.id("TC_CX_AND_REG_WELCOME_SCREEN_003")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login
    #@pytest.mark.run(order=3)
    def test_03_verify_sign_in_or_register_button_redirection_for_continuous_flow(self):
        """
            This test is for redirection of Sign In screen while clicking on Sign In/Register Button
            :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step("Verify the redirection to Sign In screen for Sign In process flow and user is in Sign In Screen"):
            result = self.welcome_page.sign_in_register_button_redirection()
            self.exe_status.mark_final(test_step="Verify the redirection to Sign In screen for Sign In process flow and user is in Sign In Screen", result=result)

    # @allure.testcase("Verify timezone")
    # @allure.id("TC_CX_AND_REG_WELCOME_SCREEN_004")
    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.timezone_test
    # def test_04_verify_timezone(self):
    #     with allure.step("Verify the timezone"):
    #         self.log.info(UIHelpers(self.driver).get_device_time_info())
    #         self.exe_status.mark_final(
    #             test_step="Verify the timezone",
    #             result=True)