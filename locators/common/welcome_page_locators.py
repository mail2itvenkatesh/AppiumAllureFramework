class WelcomePageLocatorsStaticText(object):
    welcome_title_text = "Welcome!"
    sign_in_reg_button = "Sign In"
    # sign_in_as_guest_button = "Get Started"
    welcome_to_text = "Welcome to"
    create_account_link_text = "Create Account"
    questions_abt_medical_health_text = "Questions about your health? Explore our medical resources."
    access_photos_media_files_pkg_installater_pop_up_permission_msg_text = "Allow ClinicalX to access photos, media, and files on your device?"
    access_photos_media_files_pkg_installater_pop_up_deny_btn_text = "DENY"
    access_photos_media_files_pkg_installater_pop_up_allow_btn_text = "ALLOW"

class WelcomePageLocators(object):
    brand_logo = ('id', "com.hsp.clinicalX:id/logo_imageview")
    welcome_title_text = ('id', "com.hsp.clinicalX:id/title_text_view")  # exact match = //span[.="Health"]
    sign_in_reg_button = ('id', "com.hsp.clinicalX:id/btn_signorreg")
    create_account_link = ('xpath', "//android.widget.TextView[@resource-id='com.hsp.clinicalX:id/splash_activity_create_account_label']")
    # sign_in_as_guest_button = ('id', "com.hsp.clinicalX:id/guest")
    # lang_dropdown_selector = ('id', "com.hsp.clinicalX:id/spn_lan")
    # lang_dropdown_selector_eng_option = ('xpath', "//android.widget.ListView//android.widget.CheckedTextView[@text='English']")
    # lang_dropdown_selector_spa_option = ('xpath', "//android.widget.ListView//android.widget.CheckedTextView[@text='Spanish']")

    welcome_to_text_element = ('xpath', "//android.widget.TextView[contains(@text,'{}')]".format(WelcomePageLocatorsStaticText().welcome_to_text))
    identify_medical_center_name_element = ('xpath', "//android.widget.TextView[@resource-id='com.hsp.clinicalX:id/splash_activity_clinic_name_value']")
    access_photos_media_files_pkg_installater_pop_up = ('id', "com.android.packageinstaller:id/dialog_container")
    access_photos_media_files_pkg_installater_pop_up_folder_icon = ('id', "com.android.packageinstaller:id/permission_icon")
    access_photos_media_files_pkg_installater_pop_up_permission_msg = ('id', "com.android.packageinstaller:id/permission_message")
    access_photos_media_files_pkg_installater_pop_up_deny_btn = ('id', "com.android.packageinstaller:id/permission_deny_button")
    access_photos_media_files_pkg_installater_pop_up_allow_btn = ('id', "com.android.packageinstaller:id/permission_allow_button")

    def identify_medical_center_name(self, medical_center_name):
        """
        Fetch the Medical Center name element using Medical Center Name
        :param medical_center_name: medical_center_name as a string
        :return: Web Element
        """
        #return ('xpath', "//android.widget.TextView[contains(@text, '{}')]".format(medical_center_name))
        return ('xpath', "//android.widget.TextView[@resource-id='com.hsp.clinicalX:id/splash_activity_clinic_name_value' and @text='{}']".format(medical_center_name))

    suitcase_medical_image = ('xpath', "//android.widget.TextView[@resource-id='com.hsp.clinicalX:id/splash_activity_medical_resource_textview']/../descendant::android.widget.ImageView")
    questions_abt_medical_health = ('id', "com.hsp.clinicalX:id/splash_activity_medical_resource_textview")
