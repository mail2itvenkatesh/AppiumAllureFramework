import logging
import utility.framework.logger_utility as log_utils
import datetime
import os
import traceback
import pyexcel as exc
import json
from collections import OrderedDict

class DataReader:
    """
    This class includes basic reusable data helpers.
    """
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.file_path = os.path.join(self.cur_path, r"../../test_data/TestData.xlsx")
        self.json_file_path = os.path.join(self.cur_path, r"../../test_data/user_info.json")
        self.general_data_json_file_path = os.path.join(self.cur_path, r"../../test_data/general_info.json")

    def load_excel_data(self):
        """
        This methods is used for loading excel file data
        :return: it returns excel records
        """
        records = None

        # noinspection PyBroadException

        try:
            if self.file_path is not None:
                records = exc.iget_records(file_name=self.file_path)
        except Exception as ex:
            traceback.print_exc(ex)

        return records

    def get_data(self, tc_name, column_name):
        """
        This method is used for returning column data specific to test case name
        :param tc_name: it takes test case name as input parameter
        :param column_name: it takes the name of the column for which value has to be returned
        :return:
        """
        value = None
        excel_records = self.load_excel_data()

        # noinspection PyBroadException

        try:
            if excel_records is not None:
                for record in excel_records:
                    if record['TC_Name'] == tc_name:
                        value = record[column_name]
                        break
                    else:
                        continue

        except Exception as ex:
            traceback.print_exc(ex)

        return value

    def load_general_info_json(self):
        """
        This method is used for loading json file data. Through this we can modify the json file also
        :return: it returns json records
        # https://stackoverflow.com/questions/44587621/how-to-make-python-write-json-read-and-write-same-file-for-each-cicle
        """
        records = None

        # noinspection PyBroadException

        try:
            if self.general_data_json_file_path is not None:
                with open(self.general_data_json_file_path,'r') as json_file:
                    records = json.load(json_file)
        except Exception as ex:
            traceback.print_exc(ex)

        return records

    def load_json(self):
        """
        This method is used for loading json file data. Through this we can modify the json file also
        :return: it returns json records
        # https://stackoverflow.com/questions/44587621/how-to-make-python-write-json-read-and-write-same-file-for-each-cicle
        """
        records = None

        # noinspection PyBroadException

        try:
            if self.json_file_path is not None:
                #records = exc.iget_records(file_name=self.file_path)
                with open(self.json_file_path,'r+') as json_file:
                    # I use OrderedDict to keep the same order of key/values in the source file
                    records = json.load(json_file,object_pairs_hook=OrderedDict)
        except Exception as ex:
            traceback.print_exc(ex)

        return records

    def fetch_load_brand_test_data_json(self, brand_name):
        """
        This method is used to fetch and retrieve the information from {brand}_medical_center_test_data.json
        :param brand_name: brand_name as a string
        :return: it returns json records
        """
        records = None

        # noinspection PyBroadException

        try:
            self.brand_test_data_path = os.path.join(self.cur_path, r"../../test_data/brands_test_data/{}_medical_center_test_data.json".format(brand_name))

            if self.brand_test_data_path is not None:
                with open(self.brand_test_data_path,'r+') as json_file:
                    # I use OrderedDict to keep the same order of key/values in the source file
                    records = json.load(json_file,object_pairs_hook=OrderedDict)

            # with open("C:\Venkatesh\gitlab_push\clinical-experience-app-android\/appium_tests\clinicalX_android_mobile_automation\/test_data\/medical_center_brands_test_data\irvine_rosslyn_medical_center_test_data.json",'r+') as json_file:
            #     records = json.load(json_file)

        except Exception as ex:
            traceback.print_exc(ex)

        return records

    def fetch_appointment_type_info_list_category(self, apptment_type, brand_name):
        """
        This method is used to fetch the Appointment Type Category's all information
        :param apptment_type: apptment_type as a string
        :param brand_name: brand_name as a string
        :return: appointment type neccessary info as list
        """

        fetched_record = None

        json_loaded = self.fetch_load_brand_test_data_json(brand_name)

        for index, element in enumerate(json_loaded["apptmt_info_data"]['appointment_type_info_list']):
            if apptment_type == json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_type']:
                fetched_record = json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]
                break
        return fetched_record

    def fetch_clinic_details(self, brand_name):
        """
        THis method is used to fetch the clinic details available for appointment booking
        :param medical_center_name: brand_name as a string (say irvine)
        :return: medical center all informations
        """

        fetched_record = None

        self.log.info("Medical Center Name passed is {}".format(brand_name))
        json_loaded = self.fetch_load_brand_test_data_json(brand_name)

        if json_loaded['clinic_provider_details']:
            fetched_record = json_loaded['clinic_provider_details']

        return fetched_record

    def generalized_fetch_clinic_details(self, medical_center_name,apptmt_type, apptmt_type_list_fetched_from_brand_on_ui_load = None):
        """
        THis method is used to fetch the clinic apptmt_type details available for appointment booking generally
        :param medical_center_name: medical_center_name as a string
        :param apptmt_type: apptmt_type as a string
        :param apptmt_type_list_fetched_from_brand_on_ui_load: apptmt_type_list_fetched_from_brand_on_ui_load as a list
        :return: medical appointment type info
        """
        apptmt_type_needed = None

        if apptmt_type in self.fetch_clinic_details(medical_center_name)['apptmt_types']:
            apptmt_type_needed = apptmt_type

        if apptmt_type not in self.fetch_clinic_details(medical_center_name)['apptmt_types']:
            if (apptmt_type_list_fetched_from_brand_on_ui_load != None) and (len(apptmt_type_list_fetched_from_brand_on_ui_load) != 0):
                apptmt_type_needed = apptmt_type_list_fetched_from_brand_on_ui_load[0]

        return apptmt_type_needed

    def fetch_appointment_type_info_list_category_bulk_records(self, brand_name):
        """
        This method is used to fetch the Appointment Type Category's all information(bulk)
        :param brand_name: brand_name as a string
        :return: all appointment type category info as list
        """
        json_loaded = self.fetch_load_brand_test_data_json(brand_name)
        return json_loaded

    def fetch_current_year(self):
        """
        Fetch the current year for appointment booking
        :return: current year
        """
        now = datetime.datetime.now()
        return now.year

    def fetch_partner_brands_list(self):
        """
        Fetch the partner brands from test_data.json file
        :return: partner brands
        """
        json_loaded = self.load_general_info_json()
        return json_loaded['partners']

    def fetch_apptmt_type_provider_time_slot_info(self, session_name):
        """
        Fetch the session_name from general_info.json file
        :param session_name: session_name as a string
        :return: session slot info list
        """
        json_loaded = self.load_general_info_json()
        fetched_info = None

        if session_name == "Morning":
            fetched_info = json_loaded['morning_time_slots']

        elif session_name == "Afternoon":
            fetched_info = json_loaded['afternoon_time_slots']

        elif session_name == "Evening":
            fetched_info = json_loaded['evening_time_slots']

        else:
            fetched_info = None

        return fetched_info

    def fetch_24_hr_to_12_hr_conversion_time_slot(self, time_slot):
        """
        Fetch the time_slot from general_info.json file
        :param time_slot: time_slot as a string
        :return: time_slot info
        """
        json_loaded = self.load_general_info_json()
        fetched_info = None

        for key,value in json_loaded['24_hr_12_hr_time_slot_conversion'].items():
            if key == time_slot:
                fetched_info = value
                break

        return fetched_info

    def fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(self, time_slot):
        """
        Fetch the time_slot from general_info.json file
        :param time_slot: time_slot as a string
        :return: time_slot info
        """
        json_loaded = self.load_general_info_json()
        fetched_info = None

        for key,value in json_loaded['24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion'].items():
            if value == time_slot:
                fetched_info = key
                break

        return fetched_info

    def fetch_12_hr_with_AM_PM_am_pm_time_slot_conversion(self, time_slot):
        """
        Fetch the time_slot from general_info.json file
        :param time_slot: time_slot as a string
        :return: time_slot info
        """
        json_loaded = self.load_general_info_json()
        fetched_info = None

        for key,value in json_loaded['12_hr_with_AM_PM_am_pm_time_slot_conversion'].items():
            if value == time_slot:
                fetched_info = key
                break

        return fetched_info

    def fetch_24_hr_to_12_hr_conversion_time_slot_retrieve_keys(self):
        """
        Fetch the time_slot keys from general_info.json file
        :return: keys info list
        """
        json_loaded = self.load_general_info_json()
        return list(json_loaded['24_hr_12_hr_time_slot_conversion'].keys())

    def fetch_apptmt_type_provider_speciality_conversion_info(self, apptmnt_type):
        """
        Fetch the partner brands from test_data.json file
        :param apptmnt_type: apptmnt_type as a string
        :return: Speciality Name for the apptment_type provided
        """
        json_loaded = self.load_general_info_json()
        return json_loaded['apptmt_type_provider_speciality_conversion'][apptmnt_type]

    def fetch_registered_user_data_from_json_file(self, user_category=None, user_name_type=None, brand_name=None):
        """
        This method is used to fetch the registered self and dependent user details
        :param user_category: user_category as a string and it would hold details like mfa_disabled, mfa_enabled,etc
        :param user_name_type:  user_name_type as a string and it would hold details like self,dependent
        :param brand_name:  brand_name as a string
        :return: self user related info
        """
        fetched_record = None

        json_loaded = self.load_json()
        self.log.info("Length of the retrieved user details list is {}".format(len(json_loaded['brand_name_user']['registered'][user_category])))
        for i in range(len(json_loaded['brand_name_user']['registered'][user_category])):
            if user_name_type in json_loaded['brand_name_user']['registered'][user_category][i]:
                fetched_record = json_loaded['brand_name_user']['registered'][user_category][i][user_name_type]
                break

        return fetched_record

    def fetch_medication_history_by_med_name(self,med_name,med_his_list):
        """
        This method is to fetch the specific medication history records based upon the med name provided
        :param med_name: med_name as string
        :param med_his_list: med_his_list as list
        :return: medication record as dict
        """
        fetched_dict = None
        # med_his_list = self.fetch_registered_user_data_from_json_file(user_category="mfa_disabled", user_name_type="self", brand_name="irvine")['medication_history']
        # print(med_his_list)
        for his_ind in range(len(med_his_list)):
            # print(med_his_list[his_ind]['history']['medication_otc_drug_supplement'])
            if med_name == med_his_list[his_ind]['history']['medication_otc_drug_supplement']:
                fetched_dict = {'drug_name': med_his_list[his_ind]['history']['medication_otc_drug_supplement'],
                                'strength': med_his_list[his_ind]['history']['strength'],
                                'dose': med_his_list[his_ind]['history']['dose'],
                                'frequency': med_his_list[his_ind]['history']['frequency'],
                                'prescription_date': med_his_list[his_ind]['history']['prescription_date'],
                                'start_date': med_his_list[his_ind]['history']['start_date'],
                                'end_date': med_his_list[his_ind]['history']['end_date'],
                                'taking_status': med_his_list[his_ind]['history']['taking_status'],
                                'notes': med_his_list[his_ind]['history']['notes']
                                }
                break
        return fetched_dict

    def fetch_allergy_history_by_allergy_name(self,allergy_name,allergy_his_list):
        """
        This method is to fetch the specific allergy history records based upon the med name provided
        :param allergy_name: allergy_name as string
        :param allergy_his_list: allergy_his_list as list
        :return: allergy record as dict
        """
        fetched_dict = None
        for his_ind in range(len(allergy_his_list)):
            if allergy_name == allergy_his_list[his_ind]['history']['allergy_info']:
                fetched_dict = {'allergy_info': allergy_his_list[his_ind]['history']['allergy_info'],
                                'reactions': allergy_his_list[his_ind]['history']['reactions'],
                                'notes': allergy_his_list[his_ind]['history']['notes']
                                }
                break
        return fetched_dict

    def fetch_observation_history_by_obs_name(self,obs_name,obs_his_list):
        """
        This method is to fetch the specific observation history records based upon the obs name provided
        :param obs_name: obs_name as string
        :param obs_his_list: obs_his_list as list
        :return: observation record as dict
        """
        fetched_dict = None
        for his_ind in range(len(obs_his_list)):
            if obs_name == obs_his_list[his_ind]['history']['test_name']:
                fetched_dict = {'test_name': obs_his_list[his_ind]['history']['test_name'],
                                'result_value': obs_his_list[his_ind]['history']['result_value'],
                                'units': obs_his_list[his_ind]['history']['units'],
                                'test_date': obs_his_list[his_ind]['history']['test_date'],
                                'result_date': obs_his_list[his_ind]['history']['result_date'],
                                'notes': obs_his_list[his_ind]['history']['notes']
                                }
                break
        self.log.info("fetched_dict value is {}".format(fetched_dict))
        return fetched_dict

    def fetch_registered_user_dependent_from_json_file_using_dependent_name(self, user_category=None, dependent_name=None, brand_name=None):
        """
        This method is used to fetch the Patient's dependent details
        :param user_category: user_category as a string and it would hold details like mfa_disabled, mfa_enabled,etc
        :param dependent_name:  dependent_name as a string and it would hold details like Sara
        :param brand_name:  brand_name as a string
        :return: relevant all dependent details
        """
        fetched_record = None

        json_loaded = self.load_json()
        self.log.info("Length of the retrieved user details list is {}".format(len(json_loaded['brand_name_user']['registered'][user_category])))
        for i in range(len(json_loaded['brand_name_user']['registered'][user_category])):
            if 'dependent' in json_loaded['brand_name_user']['registered'][user_category][i]:
                for j in range(len(json_loaded['brand_name_user']['registered'][user_category][i]['dependent'])):
                    if json_loaded['brand_name_user']['registered'][user_category][i]['dependent'][j]['first_name'] == dependent_name:
                        fetched_record = json_loaded['brand_name_user']['registered'][user_category][i]['dependent'][j]
                        break

        return fetched_record

    def fetch_new_user_data_from_json_file(self, user_name_type=None, brand_name=None):
        """
        This method is used to fetch the new user details for the specified brand
        :param user_name_type:  user_name_type as a string and it would hold details like self,dependent
        :param brand_name:  brand_name as a string
        :return: Returnn the new user details for brand
        """
        fetched_record = None

        json_loaded = self.load_json()
        self.log.info("Length of the retrieved user details list is {}".format(len(json_loaded['brand_name_user']['new_user_register'])))
        for i in range(len(json_loaded['brand_name_user']['new_user_register'])):
            if user_name_type in json_loaded['brand_name_user']['new_user_register'][i]:
                fetched_record = json_loaded['brand_name_user']['new_user_register'][i][user_name_type]
                break

        return fetched_record

    def fetch_guest_flow_user_details(self, user_name_type=None, brand_name=None):
        """
        This method is used to fetch the guest user details for the specified brand
        :param user_name_type:  user_name_type as a string and it would hold details like self,dependent
        :param brand_name:  brand_name as a string
        :return: Returnn the new user details for brand
        """
        fetched_records = None
        json_loaded = self.load_json()

        for i in range(len(json_loaded['brand_name_user']['guest'])):
            if user_name_type in json_loaded['brand_name_user']['guest'][i]:
                fetched_records = json_loaded['brand_name_user']['guest'][i][user_name_type]
                break

        return fetched_records

    def fetch_single_insurance_details_from_json_file_using_user_category(self, user_category=None, insurance_name = None, brand_name=None):
        """
        This method is used to fetch the Patient's insurance info details
        :param user_category: user_category as a string
        :param insurance_name: insurance_name as a string
        :param brand_name: brand_name as a string
        :return: particular insurance details
        """
        fetched_record = None

        json_loaded = self.load_json()
        self.log.info("Length of the retrieved insurance details list is {}".format(len(json_loaded['brand_name_user']['registered'][user_category])))
        for i in range(len(json_loaded['brand_name_user']['registered'][user_category])):
            if 'self' in json_loaded['brand_name_user']['registered'][user_category][i]:
                for j in range(len(json_loaded['brand_name_user']['registered'][user_category][i]['self']['insurance_card_info'])):
                    if insurance_name  == json_loaded['brand_name_user']['registered'][user_category][i]['self']['insurance_card_info'][j]['insurance']['org_name']:
                        fetched_record = json_loaded['brand_name_user']['registered'][user_category][i]['self']['insurance_card_info'][j]['insurance']
                        break
        return fetched_record

    def fetch_bulk_insurance_details_from_json_file_using_user_category(self, user_category=None, brand_name=None):
        """
        This method is used to fetch the bulk insurance info details
        :param user_category: user_category as a string
        :param brand_name: brand_name as a string
        :return: particular insurance details
        """
        fetched_record = None

        json_loaded = self.load_json()
        self.log.info("Length of the retrieved insurance details list is {}".format(len(json_loaded['brand_name_user']['registered'][user_category])))
        for i in range(len(json_loaded['brand_name_user']['registered'][user_category])):
            if 'self' in json_loaded['brand_name_user']['registered'][user_category][i]:
                fetched_record = json_loaded['brand_name_user']['registered'][user_category][i]['self']['insurance_card_info']
                break

        return fetched_record

    def fetch_appointment_type_timeslot_info(self, apptment_type, brand_name, day, session):
        """
        This method is used to fetch the Appointment Type timeslot information for booking an appointment
        :param apptment_type: apptment_type as a string
        :param brand_name: brand_name as a string
        :param day: day as a string
        :param session: session as a string
        :param time: time as a string
        :return: appointment type timeslot neccessary info
        """

        fetched_record = None

        json_loaded = self.fetch_load_brand_test_data_json(brand_name)
        self.log.info("Values passed for apptment_type, brand_name, day, session is {},{},{},{}".format(apptment_type, brand_name, day, session))
        for index, element in enumerate(json_loaded["apptmt_info_data"]['appointment_type_info_list']):
            if apptment_type == json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_type']:
                for a in range(len(json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_book_details'])):
                    for b in range(len(json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_book_details'][a]['details'])):
                        if json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_book_details'][a]['day'] == day and \
                            json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_book_details'][a]['details'][b]['session'] == session:
                            fetched_record = {
                                "day": json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_book_details'][a]['day'],
                                "session": json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_book_details'][a]['details'][b]['session'],
                                "time": json_loaded["apptmt_info_data"]['appointment_type_info_list'][index]['apptmt_book_details'][a]['details'][b]['time_slot']
                            }

                            break
                # break

        return fetched_record

    def fetch_clinic_details_by_medical_center_name(self, brand, medical_center_name):
        """
        THis method is used to fetch the clinic details available for appointment booking
        :param medical_center_name: brand_name as a string (say irvine)
        :return: medical center all informations
        """

        fetched_record = None

        self.log.info("Medical Center Name passed is {}".format(medical_center_name))
        json_loaded = self.fetch_load_brand_test_data_json(brand)

        if json_loaded['clinic_provider_details']['medical_center_name'] == medical_center_name:
            fetched_record = json_loaded['clinic_provider_details']

        return fetched_record


    def provide_collision_up_check_details(self, fetched_apptmt_info_list):
        """
        This method is used to fetch the collision pop up details
        :param fetched_apptmt_info_list: fetched_apptmt_info_list
        :return: list of dict
        """

        # fetched_apptmt_info_list = [{'patient_name': "Black Pandey", 'apptmt_for': "self",
        #        'apptmt_type': "Dental", 'day': "Today", 'date': "10-Oct", 'time': "8:30am"},
        #
        #       {'patient_name': "White Pandey", 'apptmt_for': "dependent",
        #        'apptmt_type': "Dental", 'day': "Today", 'date': "10-Oct", 'time': "8:30pm"}
        #       ]
        fetched_record = []
        if len(fetched_apptmt_info_list) != 0:
            self.log.info("fetched_apptmt_info_list available is {}".format(fetched_apptmt_info_list))

            for a, list_el in enumerate(fetched_apptmt_info_list):
                if list_el['apptmt_for'] == "dependent":
                    # sd = list_el['time'].replace('am', ' AM') if 'am' in list_el['time'] else list_el['time']
                    if 'am' in list_el['time']:
                        # dependent_flow_time = list_el['time'].replace('am', ' AM')
                        # fetched_record.append({"dependent_flow_time":self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})
                        fetched_record.append({"dependent_flow_time":list_el['time'].replace('am', 'AM')})

                    if 'pm' in list_el['time']:
                        # dependent_flow_time = list_el['time'].replace('pm', ' PM')
                        fetched_record.append({"dependent_flow_time": list_el['time'].replace('pm', 'PM')})
                        # fetched_record.append({"dependent_flow_time": self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})

                if list_el['apptmt_for'] == "self":
                    if 'am' in list_el['time']:
                        # self_flow_time = list_el['time'].replace('am', ' AM')
                        # fetched_record.append({"self_flow_time": list_el['time'].replace('am', 'AM')})
                        fetched_record.append({"self_flow_time": self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})

                    if 'pm' in list_el['time']:
                        # self_flow_time = list_el['time'].replace('pm', ' PM')
                        # fetched_record.append({"self_flow_time": list_el['time'].replace('pm', 'PM')})
                        fetched_record.append({"self_flow_time": self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})

                    # self_pat_name = list_el['patient_name']
                    fetched_record.append({"self_pat_name" : list_el['patient_name']})

            return fetched_record


    def provide_collision_up_check_details_with_apptmt_type(self, apptmt_type,fetched_apptmt_info_list):
        """
        This method is used to fetch the collision pop up details
        :param apptmt_type: apptmt_type as a string
        :param fetched_apptmt_info_list: fetched_apptmt_info_list (say irvine)
        :return: list of dict
        """
        fetched_record = []
        if len(fetched_apptmt_info_list) != 0:
            self.log.info("fetched_apptmt_info_list available is {}".format(fetched_apptmt_info_list))

            for a, list_el in enumerate(fetched_apptmt_info_list):
                if list_el['apptmt_type'] == apptmt_type:
                    # sd = list_el['time'].replace('am', ' AM') if 'am' in list_el['time'] else list_el['time']
                    if 'am' in list_el['time']:
                        # dependent_flow_time = list_el['time'].replace('am', ' AM')
                        # fetched_record.append({"dependent_flow_time":self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})
                        fetched_record.append({"dependent_flow_time":list_el['time'].replace('am', 'AM')})

                    if 'pm' in list_el['time']:
                        # dependent_flow_time = list_el['time'].replace('pm', ' PM')
                        fetched_record.append({"dependent_flow_time": list_el['time'].replace('pm', 'PM')})
                        # fetched_record.append({"dependent_flow_time": self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})
                else:
                    if 'am' in list_el['time']:
                        # self_flow_time = list_el['time'].replace('am', ' AM')
                        # fetched_record.append({"self_flow_time": list_el['time'].replace('am', 'AM')})
                        fetched_record.append({"self_flow_time": self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})

                    if 'pm' in list_el['time']:
                        # self_flow_time = list_el['time'].replace('pm', ' PM')
                        # fetched_record.append({"self_flow_time": list_el['time'].replace('pm', 'PM')})
                        fetched_record.append({"self_flow_time": self.fetch_24_hr_12_hr_with_AM_PM_am_pm_time_slot_conversion(list_el['time'])})

                    # self_pat_name = list_el['patient_name']
                    fetched_record.append({"self_pat_name" : list_el['patient_name']})

            return fetched_record


# d = DataReader()
# print(df)







