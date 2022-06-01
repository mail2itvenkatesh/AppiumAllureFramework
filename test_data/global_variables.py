##### Reference ######
# https://stackoverflow.com/questions/13034496/using-global-variables-between-files
# http://net-informations.com/python/iq/global.htm
# http://effbot.org/pyfaq/how-do-i-share-global-variables-across-modules.htm

# Global Variable to fetch the pytest command line arguments from conftest.py
service_brand = None
cmdline_apptmt_type = None
brand_apptmt_types = None # Fetch all appointment types available in Appointment Type Page. Here we are getting the API values using UI Screen elements available

does_apptmt_for_self = None
does_apptmt_for_dependent = None

apptmt_type = None
apptmt_booking_time = None
apptmt_booking_day = None
apptmt_booking_date = None
apptmt_booking_day_session = None # Morning / Afternoon / Evening

patient_name = None
dependent_name_choosed_for_apptmt = None  # It will have dependent full name as of latest version of code

medical_provider_name = None
medical_provider_practice = None # Family Practice
current_medical_center_address = None # This is to store the current clinic address before change in Clinic Locator
changed_medical_center_address = None # This is to store the changed clinic address after change in Clinic Locator

medical_center_name = None #Medical Center Name for default/recommended clinic center and it holds the value mostly as "At this clinic"
medical_center_name_default = None  #Default Medical Center Name fetched from Change Date and Time Screen
medical_center_name_fetched_from_clinic_locator = None
payment_type_choosed = None
pay_estimate_price = None

mobile_ph_no = None
comm_pref_info = None

apptmt_type_services_selected = []
main_symptoms_main_reason_for_appointment = None
special_accommodations = None

check_in_estimated_wait_time = None # Check In Flow validations

hold_previous_apptmt_time_slot = []

# Fetch the multiple appointment details to perform same or difference validation
fetched_apptmt_complete_details_list = []

advanced_search_filter_applied_count = 0
advanced_search_provider_gender_filter_applied_count = 0
advanced_search_lang_spoken_filter_applied_count = 0
advanced_search_area_focus_filter_applied_count = 0

# Create Account - Contact Information screen Flow Global Variables for Patient Info.
create_Account_flow_contact_info_records = {}

medical_resources_cat_lists = None


# For continuous appointment booking validation
forthcoming_apptmt_type = None
forthcoming_apptmt_booking_time = None
forthcoming_apptmt_booking_day = None
forthcoming_apptmt_booking_date = None

# Multiple Check In
fetched_patient_list = None