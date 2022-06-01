import logging
from utility.support.ui_helpers import UIHelpers
import utility.framework.logger_utility as log_utils
from locators.common.welcome_page_locators import WelcomePageLocators,WelcomePageLocatorsStaticText
from locators.common.admin_setup_page_locators import AdminSetUpPageLocators
from locators.common.page_title_info import FlowPageFlowTitle
from locators.registered.signIn_page_locators import SignInPageLocators
from selenium.common.exceptions import NoSuchElementException
from pages.common.admin_setup_screen import AdminSetUpPage
from pages.common.common_scan_photo_id_page import CommonScanPhotoIDPage

class GuestWelcomePage(UIHelpers):
    """This class defines the method and element identifications for Welcome Screen Page."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        #self.ui_helpers = UIHelpers(driver)
        self.locator = WelcomePageLocators()
        self.locator_page_static_text = WelcomePageLocatorsStaticText()
        self.admin_set_up_page = AdminSetUpPage(driver)
        self.scan_photo_id_page = CommonScanPhotoIDPage(driver)
        super(GuestWelcomePage, self).__init__(driver)

    def verify_welcome_page_title(self, admin_username, clinic_id, admin_pwd):
        """
        Verify Welcome Page Title and if access permission pop up shows then corresponding flow would happen.
        :return: True | False
        """
        result = True
        final_results_holder = []

        try:
            # if self.driver.find_element(*self.locator.access_photos_media_files_pkg_installater_pop_up).is_enabled():
            #
            #     access_photos_media_files_pkg_installater_pop_up_folder_icon_element = self.get_element(*self.locator.access_photos_media_files_pkg_installater_pop_up_folder_icon)
            #
            #     if not access_photos_media_files_pkg_installater_pop_up_folder_icon_element:
            #         self.log.info("Folder icon image is not available")
            #         result = False
            #
            #     access_photos_media_files_pkg_installater_pop_up_permission_msg_element = self.get_element_text(*self.locator.access_photos_media_files_pkg_installater_pop_up_permission_msg)
            #
            #     if access_photos_media_files_pkg_installater_pop_up_permission_msg_element.strip() != self.locator_page_static_text.access_photos_media_files_pkg_installater_pop_up_permission_msg_text.strip():
            #         self.log.info("Expected is {}".format(self.locator_page_static_text.access_photos_media_files_pkg_installater_pop_up_permission_msg_text))
            #         self.log.error("Result mismatched and actual result is  -- {}".format(access_photos_media_files_pkg_installater_pop_up_permission_msg_element))
            #         result = False
            #
            #     access_photos_media_files_pkg_installater_pop_up_deny_btn_element = self.get_element_text(*self.locator.access_photos_media_files_pkg_installater_pop_up_deny_btn)
            #
            #     if access_photos_media_files_pkg_installater_pop_up_deny_btn_element.strip() != self.locator_page_static_text.access_photos_media_files_pkg_installater_pop_up_deny_btn_text.strip():
            #         self.log.info("Expected is {}".format(self.locator_page_static_text.access_photos_media_files_pkg_installater_pop_up_deny_btn_text))
            #         self.log.error("Result mismatched and actual result is  -- {}".format(access_photos_media_files_pkg_installater_pop_up_deny_btn_element))
            #         result = False
            #
            #     access_photos_media_files_pkg_installater_pop_up_allow_btn_element = self.get_element_text(*self.locator.access_photos_media_files_pkg_installater_pop_up_allow_btn)
            #
            #     if access_photos_media_files_pkg_installater_pop_up_allow_btn_element.strip() != self.locator_page_static_text.access_photos_media_files_pkg_installater_pop_up_allow_btn_text.strip():
            #         self.log.info("Expected is {}".format(self.locator_page_static_text.access_photos_media_files_pkg_installater_pop_up_allow_btn_text))
            #         self.log.error("Result mismatched and actual result is  -- {}".format(access_photos_media_files_pkg_installater_pop_up_allow_btn_element))
            #         result = False
            #
            #     self.get_element(*self.locator.access_photos_media_files_pkg_installater_pop_up_allow_btn).click()

            if self.driver.find_element(*AdminSetUpPageLocators().enter_clinic_details_text).is_enabled():
                # Verify the static elements available
                self.log.info("Started entering the Admin Setup Screen")
                result1 = self.admin_set_up_page.verify_static_text_elements_available()
                final_results_holder.append(result1)

                # Enter the necessary details for identifying the clinic in case of any failure loading app or new installation of app
                result2 = self.admin_set_up_page.enter_details_connect_to_clinic(admin_username, clinic_id, admin_pwd)
                final_results_holder.append(result2)

        except (NoSuchElementException, Exception) as e:
            self.log.info("Exception occurred is {}".format(e))

        element_text = self.get_element_text(*self.locator.welcome_title_text)
        if element_text.strip() != WelcomePageLocatorsStaticText.welcome_title_text.strip():
            self.log.info("Expected is {}".format(WelcomePageLocatorsStaticText.welcome_title_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(element_text))
            result = False
            final_results_holder.append(result)

        return all(final_results_holder)

    def verify_welcome_page_title_common(self):
        """
        Verify Welcome Page Title
        :return: True | False
        """
        result = True

        element_text = self.get_element_text(*self.locator.welcome_title_text)

        if element_text.strip() != WelcomePageLocatorsStaticText.welcome_title_text.strip():
            self.log.info("Expected is {}".format(WelcomePageLocatorsStaticText.welcome_title_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(element_text))
            result = False

        return result

    def verify_welcome_to_medical_center_text(self, clinic_name):
        """
        Verify the text start with Welcome To {Clinic name}
        :param clinic_name: clinic_name as a string
        :return: True | False
        """
        result = True

        element_text = self.get_element_text(*self.locator.welcome_to_text_element)

        # clinic_name_actual = WelcomePageLocatorsStaticText.medical_center_name.strip()
        # clinic_name_actual = clinic_name_actual

        if element_text.strip() != WelcomePageLocatorsStaticText.welcome_to_text.strip():
            self.log.info("Expected is {}".format(WelcomePageLocatorsStaticText.welcome_to_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(element_text))
            result = False

        self.log.info("From welcome_page.py - Medical Center Name is {}".format(clinic_name))

        element_text1 = self.get_element_text(*self.locator.identify_medical_center_name(clinic_name))

        if element_text1.strip() != clinic_name:
            self.log.info("Expected is {}".format(clinic_name))
            self.log.error("Result mismatched and actual result is  -- {}".format(element_text1))
            result = False

        return result

    def verify_questions_about_your_health_text(self):
        """
        Verify Questions about your health?..... text available in welcome page
        :return: True | False
        """
        result = True

        element_text = self.get_element_text(*self.locator.questions_abt_medical_health)
        if element_text.strip() != WelcomePageLocatorsStaticText.questions_abt_medical_health_text.strip():
            self.log.info("Expected is {}".format(WelcomePageLocatorsStaticText.questions_abt_medical_health_text))
            self.log.error("Result mismatched and actual result is  -- {}".format(element_text))
            result = False

        return result

    def verify_availability_of_sign_in_or_register_button(self):
        """
        Verify the Sign In/Register Button availability
        :return: True | False
        """
        result = True
        element_available = self.get_element(*self.locator.sign_in_reg_button)

        if (not element_available) and (element_available.text.strip() != WelcomePageLocatorsStaticText.sign_in_reg_button.strip()):
            self.log.error("Element not available and button text is not matching")
            result = False

        if (not element_available) or (element_available.text.strip() != WelcomePageLocatorsStaticText.sign_in_reg_button.strip()):
            self.log.info("Expected Button text is {}".format(WelcomePageLocatorsStaticText.sign_in_reg_button))
            self.log.error("Element not available or button text is not matching and available text is {}".format(element_available.text))
            result = False

        return result

    def verify_availability_of_create_account_link_text(self):
        """
        Verify the Create Account availability
        :return: True | False
        """
        result = True

        element_available = self.get_element(*self.locator.create_account_link)

        if (not element_available) and (element_available.text.strip() != WelcomePageLocatorsStaticText.create_account_link_text.strip()):
            self.log.error("Element not available and button text is not matching")
            result = False

        if (not element_available) or (element_available.text.strip() != WelcomePageLocatorsStaticText.create_account_link_text.strip()):
            self.log.info("Expected Button text is {}".format(WelcomePageLocatorsStaticText.create_account_link_text))
            self.log.error("Element not available or button text is not matching and available text is {}".format(element_available.text))
            result = False

        return result

    def verify_language_selector_dropdown_availbility_and_its_options(self):
        """
        Verify the Language dropdown box availability and its options
        :return: True | False
        """
        result = True

        element_available = self.get_element(*self.locator.lang_dropdown_selector)
        element_available.click()
        self.wait_for_sync(10)

        english_element_available = self.wait_for_element_visible_located(*self.locator.lang_dropdown_selector_eng_option)
        spanish_element_available = self.wait_for_element_visible_located(*self.locator.lang_dropdown_selector_spa_option)

        if (not element_available) and (not english_element_available) and (not spanish_element_available):
            self.log.error("Language Dropdown Box and its options are not available")
            result = False

        if (not element_available) or (not english_element_available) or (not spanish_element_available):
            self.log.error("Language Dropdown Box and its options are not available")
            result = False

        return result

    def verify_language_selector_dropdown_availbility_and_by_selecting_english_option(self):
        """
        Verify the Language dropdown box availability and its options select as English
        :return: True | False
        """
        result = True
        self.wait_for_sync(8)

        english_element_available = self.wait_for_element_visible_located(*self.locator.lang_dropdown_selector_eng_option)
        english_element_available.click()

        if (not english_element_available):
            self.log.error("Language Dropdown Box and its options are not available")
            result = False

        return result

    def verify_sign_in_register_button_redirection(self):
        """
        Verify the Sign In / Register Button Redirection
        :return: True | False
        """
        result = True

        element_available = self.wait_for_element_to_be_clickable(*self.locator.sign_in_reg_button)
        element_available.click()
        self.wait_for_sync(10)

        if (not element_available):
            self.log.error("Sign In/Register button element is not clickable")
            result = False

        if self.get_element_text(*SignInPageLocators.sign_in_page_title).strip() != FlowPageFlowTitle.sign_in_page_title.strip():
            self.log.info("Expected Page redirection and Page Title is {}".format(FlowPageFlowTitle.sign_in_page_title))
            self.log.error("Actual Page redirection and Page Title is {}".format(self.get_element_text(*SignInPageLocators.sign_in_page_title).strip()))
            result = False

        self.log.info("Redirection page title is {}".format(self.get_element_text(*SignInPageLocators.sign_in_page_title)))
        self.verify_back_arrow_navigation()
        return result

    def sign_in_register_button_redirection(self):
        """
        Sign In / Register Button Redirection
        :return: True | False
        """
        result = True

        element_available = self.wait_for_element_visible_located(*self.locator.sign_in_reg_button,timeout=35)
        element_available.click()
        self.wait_for_sync(5)

        if (not element_available):
            self.log.error("Sign In/Register button element is not clickable")
            result = False

        return result

    def verify_back_arrow_navigation(self):
        """
        Verify the back arrow navigation
        :return: True | False
        """
        result = True

        element_available = self.get_element(*SignInPageLocators.sign_in_back_arrow_navigation)
        element_available.click()
        self.wait_for_sync(5)

        if not element_available:
            self.log.error("Back Arrow navigation is not done")
            result = False

        # if self.get_element_text(*self.locator.welcome_title_text).strip() != WelcomePageLocatorsStaticText.welcome_title_text.strip():
        #     self.log.info("Expected Page redirection and Page Title is {}".format(WelcomePageLocatorsStaticText.welcome_title_text))
        #     self.log.error("Actual Page redirection and Page Title is {}".format(self.get_element_text(*self.locator.welcome_title_text).strip()))
        #     result = False

        return result

    def verify_create_account_link_redirection(self):
        """
        Verify the Create Account link text Redirection
        :return: True | False
        """
        result = True

        element_available = self.wait_for_element_to_be_clickable(*self.locator.create_account_link)
        element_available.click()
        self.wait_for_sync(2)

        if (not element_available):
            self.log.error("Create Account link text is not clickable")
            result = False

        return result

    def create_account_link_redirection(self):
        """
        Verify the Create Account link text Redirection
        :return: NA
        """
        element_available = self.wait_for_element_to_be_clickable(*self.locator.create_account_link)
        element_available.click()
        self.wait_for_sync(2)
