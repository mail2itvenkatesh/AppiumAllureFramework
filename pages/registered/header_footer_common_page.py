import logging
from utility.support.ui_helpers import UIHelpers
import utility.framework.logger_utility as log_utils
from locators.registered.header_footer_locators import HeaderFooterLocators,HeaderFooterLocatorsStaticText
from locators.common.welcome_page_locators import WelcomePageLocators,WelcomePageLocatorsStaticText
from utility.framework.data_reader_utility import DataReader
from locators.registered.signIn_page_locators import SignInPageLocators
from locators.common.page_title_info import FlowPageFlowTitle

class HeaderFooterCommonPage(UIHelpers):
    """This class defines the method and element identifications for Header Footer Locators validation."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.header_footer_locator = HeaderFooterLocators()
        self.header_footer_static_text = HeaderFooterLocatorsStaticText()
        self.data_reader = DataReader()
        self.sign_in_page_locator = SignInPageLocators()
        super(HeaderFooterCommonPage, self).__init__(driver)

    def verify_brand_logo_image(self):
        """
        Verify the brand Branding Logo/Image availability
        :return: True | False
        """
        result = True

        element_available = self.get_element(*self.header_footer_locator.brand_logo)

        if not element_available:
            self.log.error("Brand Logo/Icon is not available")
            result = False

        return result

    def verify_user_icon_image(self):
        """
        Verify the User Icon availability
        :return: True | False
        """
        result = True

        element_available = self.get_element(*self.header_footer_locator.user_icon_after_login)

        if not element_available:
            self.log.error("USer Icon is not available")
            result = False

        return result

    def verify_account_name_spinner(self, user_details):
        """
        Verify the Account Name availability
        :param user_details: user_details as a dict
        :return: True | False
        """
        result = True
        arrived_first_name = None

        element_available = self.wait_for_element_to_be_present(*self.header_footer_locator.username_info_text_locator)
        #element_available.click()
        self.wait_for_sync(5)

        if (not element_available):
            self.log.error("Account Name spinner are not available")
            result = False

        if len(user_details['first_name']) > 4:
            arrived_first_name = "{}...".format(user_details['first_name'][0:4])
        else:
            arrived_first_name = user_details['first_name']

        arrived_last_name = user_details['last_name'][0]

        #if element_available.text.strip()!= "Venk... K.".strip():
        if element_available.text.strip()!= "{} {}.".format(arrived_first_name,arrived_last_name):
            self.log.error("Username Framed is different compared with expected one - {}".format("{} {}.".format(arrived_first_name,arrived_last_name)))
            self.log.info("Username Framed is different compared with expected one and available username is {}".format(element_available.text.strip()))
            result = False

        return result

    def verify_account_name_spinner_selector_dropdown_availbility_and_its_options(self):
        """
        Verify the Account Name dropdown box availability and its options
        :return: True | False
        """
        result = True

        click_spinner_element = self.wait_for_element_to_be_clickable(*self.header_footer_locator.username_dropdown_displayed_after_login)
        if not click_spinner_element:
            self.log.error("Unable to click on Account Spinner Dropdown")

        click_spinner_element.click()

        appointments_element_available = self.wait_for_element_visible_located(*self.header_footer_locator.spinner_appointments_option)

        if appointments_element_available.text.strip() != self.header_footer_static_text.spinner_appointments_text.strip():
            self.log.info("Expected text is {}".format(self.header_footer_static_text.spinner_appointments_text))
            self.log.error("Actual text  is {}".format(appointments_element_available.text))
            result = False

        my_account_element_available = self.wait_for_element_visible_located(*self.header_footer_locator.spinner_my_account_option)

        if my_account_element_available.text.strip() != self.header_footer_static_text.spinner_my_account_option_text.strip():
            self.log.info("Expected text is {}".format(self.header_footer_static_text.spinner_my_account_option_text))
            self.log.error("Actual text  is {}".format(my_account_element_available.text))
            result = False

        spinner_recommendations_option_element_available = self.wait_for_element_visible_located(*self.header_footer_locator.spinner_recommendations_option)

        if spinner_recommendations_option_element_available.text.strip() != self.header_footer_static_text.spinner_recommendations_option_text.strip():
            self.log.info("Expected text is {}".format(self.header_footer_static_text.spinner_recommendations_option_text))
            self.log.error("Actual text  is {}".format(spinner_recommendations_option_element_available.text))
            result = False

        sign_out_element_available = self.wait_for_element_visible_located(*self.header_footer_locator.spinner_sign_out_option)

        if sign_out_element_available.text.strip() != self.header_footer_static_text.spinner_sign_out_option_text.strip():
            self.log.info("Expected text is {}".format(self.header_footer_static_text.spinner_sign_out_option_text))
            self.log.error("Actual text  is {}".format(sign_out_element_available.text))
            result = False

        #self.tap_on_element_with_coordinates_no_element()
        self.tap_on_element_with_coordinates_no_element(x_coordinates=100,y_coordinates=500)

        return result

    def verify_sign_out_functionality(self):
        """
        Verify the Sign Out functionality
        :return: True | False
        """
        result = True

        click_spinner_element = self.wait_for_element_to_be_clickable(*self.header_footer_locator.username_dropdown_displayed_after_login)
        if not click_spinner_element:
            self.log.error("Unable to click on Account Spinner Dropdown")

        click_spinner_element.click()

        sign_out_element_available = self.wait_for_element_visible_located(*self.header_footer_locator.spinner_sign_out_option)

        if not sign_out_element_available:
            self.log.error("Account Name Spinner Dropdown Box Sign Out option is not available")
            result = False

        sign_out_element_available.click()
        self.wait_for_sync(10)

        welcome_page_title_text = self.get_element_text(*WelcomePageLocators().welcome_title_text)

        if welcome_page_title_text.strip() != WelcomePageLocatorsStaticText().welcome_title_text.strip():
            self.log.info("Expected Page redirection and Page Title is {}".format(WelcomePageLocatorsStaticText().welcome_title_text))
            self.log.error("Actual Page redirection and Page Title is {}".format(welcome_page_title_text))
            result = False

        self.wait_for_sync(5)

        return result

    def click_account_option_from_dropdown(self):
        """
        Click on Account option from Dropdown box available
        :return: True | False
        """
        result = True

        click_spinner_element = self.wait_for_element_to_be_clickable(*self.header_footer_locator.username_dropdown_displayed_after_login)
        if not click_spinner_element:
            self.log.error("Unable to click on Account Spinner Dropdown")

        click_spinner_element.click()

        account_element_available = self.wait_for_element_visible_located(*self.header_footer_locator.spinner_my_account_option)

        if not account_element_available:
            self.log.error("Account Name Spinner Dropdown Box Account option is not available")
            result = False

        account_element_available.click()
        self.wait_for_sync(2)

        return result

    def click_recommendations_option_from_dropdown(self):
        """
        Click on Recommendations option from Dropdown box available
        :return: True | False
        """
        result = True

        click_spinner_element = self.wait_for_element_to_be_clickable(*self.header_footer_locator.username_dropdown_displayed_after_login)
        if not click_spinner_element:
            self.log.error("Unable to click on Account Spinner Dropdown")

        click_spinner_element.click()

        recommendations_element_available = self.wait_for_element_visible_located(*self.header_footer_locator.spinner_recommendations_option)

        if not recommendations_element_available:
            self.log.error("Recommendations Name Spinner Dropdown Box Account option is not available")
            result = False

        recommendations_element_available.click()
        self.wait_for_sync(2)

        return result

    def verify_navigate_to_welcome_page_in_case_of_sign_in_flow_failures(self):
        """
        Verify whether user is navigated to Welcome Page in case of Sign In Page failure
        :return: True | False
        """
        result = True

        element_text = self.get_element(*self.sign_in_page_locator.sign_in_page_title)

        if (element_text != None) and (element_text.text.strip() == FlowPageFlowTitle.sign_in_page_title.strip()):
            self.get_element(*self.sign_in_page_locator.sign_in_back_arrow_navigation).click()
            self.wait_for_sync(3)

            welcome_page_title_text = self.get_element_text(*WelcomePageLocators().welcome_title_text)

            if welcome_page_title_text.strip() != WelcomePageLocatorsStaticText().welcome_title_text.strip():
                self.log.info("Expected Page redirection and Page Title is {}".format(WelcomePageLocatorsStaticText().welcome_title_text))
                self.log.error("Actual Page redirection and Page Title is {}".format(welcome_page_title_text))
                result = False

        return result

