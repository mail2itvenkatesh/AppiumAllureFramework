import logging
import pytest
import allure
import sys
import unittest
import utility.framework.logger_utility as log_utils
from utility.framework.execution_status_utility import ExecutionStatus
from utility.framework.data_reader_utility import DataReader
from utility.framework.config_utility import ConfigUtility
from pages.registered.registered_sign_in_page import RegisteredSignInPage
from pages.common.welcome_page import GuestWelcomePage

"""
    TODO:: TestCases Pending
    1. Logo Image cross check/Image Validation
    2. To and back page navigation
    3. Header and Footer section Validation
    4. Fields exception message validations
"""
#unittest.defaultTestLoader.sortTestMethodsUsing = None

@allure.story('[XXXX Android App] - Automate the Login Screen Functionality')
@allure.feature('XXXX Android App - Login Screen Tests')
@pytest.mark.usefixtures("get_driver")
@pytest.mark.incremental
#class TestRegisteredSignInPage(unittest.TestCase):
class RegisteredSignInPageFlowTests(unittest.TestCase):
    """
    This class contains the executable test cases.
    """
    log = log_utils.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        self.data_reader = DataReader()
        self.config_util = ConfigUtility()
        self.reg_sign_in_page = RegisteredSignInPage(self.driver)
        self.welcome_page = GuestWelcomePage(self.driver)
        self.exe_status = ExecutionStatus(self.driver)
        self.prop = ConfigUtility()

    @pytest.fixture(autouse=True) # Fixture to get configuration items from command line
    def _request_get_config_params(self, get_config_params):
        self._config_params = get_config_params

    @allure.testcase("Verify Sign In Screen Elements and its functionality")
    @allure.id("TC_CX_AND_REG_SIGN_IN_SCREEN_001")
    @allure.severity(allure.severity_level.NORMAL)
    #@pytest.mark.run(order=1)
    def test_01_verify_sign_in_screen_elements_functionality(self):
        """
        This test is validating the presence of Sign In Screen Elements.
        :return: return test status
        """
        ## Determining the name of the Current Function
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step("Verify presence of Sign In Screen page title"):
            result = self.reg_sign_in_page.verify_page_title()
            self.exe_status.mark_final(test_step="Verify presence of Sign In Screen page title", result=result)

        with allure.step("Verify the presence of Static Texts elements available in the page like Not register yet?,Username,Password"):
            result = self.reg_sign_in_page.verify_static_text_elements_available()
            self.exe_status.mark_final(test_step="Verify the presence of Static Texts elements available in the page like Not register yet?,Username,Password", result=result)

        with allure.step("Verify the presence of texts available in link text elements available in the page like Create an account?,Forgot your username?,Forgot your password?"):
            result = self.reg_sign_in_page.verify_text_link_elements_available()
            self.exe_status.mark_final(test_step="Verify the presence of texts available in link text elements available in the page like Create an account?,Forgot your username?,Forgot your password?", result=result)

    @allure.testcase("Verify redirection to Create an Account screen while taping on Create an Account text link")
    @allure.id("TC_CX_AND_REG_SIGN_IN_SCREEN_002")
    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.run(order=2)
    def test_02_verify_redirection_create_an_account_link(self):
        """
        This test is to verify redirection to "Create an Account" screen while taping on Create an Account text link
        :return: return test status
        """
        ## Determining the name of the Current Function
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Verify the redirection to "Create an Account" screen while taping on Create an Account text link'):
            result = self.reg_sign_in_page.verify_create_an_account_redirection()
            self.exe_status.mark_final(test_step='Verify the redirection to "Create an Account" screen while taping on Create an Account text link', result=result)

            # UIHelpers(self.driver).page_back_navigation()
            self.reg_sign_in_page.click_back_arrow_navigation()

    @allure.testcase("Verify redirection to Forgot Username screen while taping on Forgot your username? text link")
    @allure.id("TC_CX_AND_REG_SIGN_IN_SCREEN_003")
    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.run(order=3)
    def test_03_verify_redirection_forgot_username_link(self):
        """
        This test is to Verify redirection to "Forgot Username" screen while taping on Forgot your username? text link
        :return: return test status
        """
        ## Determining the name of the Current Function
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Verify redirection to "Forgot Username" screen while taping on Forgot your username? text link'):
            self.welcome_page.sign_in_register_button_redirection()
            result = self.reg_sign_in_page.verify_forgot_username_redirection()
            self.exe_status.mark_final(test_step='Verify redirection to "Forgot Username" screen while taping on Forgot your username? text link', result=result)

            self.reg_sign_in_page.click_back_arrow_navigation()


    @allure.testcase("Verify redirection to Forgot Password screen while taping on Forgot your password? text link")
    @allure.id("TC_CX_AND_REG_SIGN_IN_SCREEN_004")
    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.run(order=4)
    def test_04_verify_redirection_forgot_password_link(self):
        """
        This test is to Verify redirection to "Forgot Password" screen while taping on Forgot your password? text link
        :return: return test status
        """
        ## Determining the name of the Current Function
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Verify redirection to "Forgot Password" screen while taping on Forgot your password? text link'):
            result = self.reg_sign_in_page.verify_forgot_password_redirection()
            self.exe_status.mark_final(test_step='Verify redirection to "Forgot Password" screen while taping on Forgot your password? text link', result=result)

            self.reg_sign_in_page.click_back_arrow_navigation()

    @allure.testcase("Verify redirection to Appointment Type screen once logged in with valid credentials")
    @allure.id("TC_CX_AND_REG_SIGN_IN_SCREEN_005")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    #@pytest.mark.run(order=4)
    def test_05_verify_sign_in_with_valid_credentials(self):
        """
        This test is to Verify redirection to Review Your Information screen once logged in with valid credentials
        :return: return test status
        """
        ## Determining the name of the Current Function
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Verify redirection to Review Your Information screen once logged in with valid credentials'):
            result = self.reg_sign_in_page.verify_enter_login_credentials_redirection(self.data_reader.fetch_registered_user_data_from_json_file(self._config_params['user'],'self',self._config_params['brand']))
            self.exe_status.mark_final(test_step='Verify redirection to Review Your Information screen once logged in with valid credentials', result=result)


