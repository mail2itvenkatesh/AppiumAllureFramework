from traceback import print_stack
from configparser import ConfigParser
import utility.framework.logger_utility as log_utils
import logging
import os

class ConfigUtility:
    """
    This class includes basic reusable config_helpers.
    """

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))  #Gives Absoluete Path + directory name
        print(self.cur_path)
        self.config_path = os.path.join(self.cur_path, r"../../configs/config.ini")

    def load_properties_file(self):
        """
        This method loads the properties/ini file
        :return: this method returns config reader instance.
        """

        config = None
        try:
            # https://stackoverflow.com/questions/40775709/avoiding-too-broad-exception-clause-warning-in-pycharm

            # noinspection PyBroadException
            config = ConfigParser()
            config.read(self.config_path)

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
            print_stack()
        #print(config)
        return config

    def change_properties_file(self, section, property_name, property_value):
        """
        This method is used to change the property value
        :param section: property section in ini file
        :param property_name: property name to change
        :param property_value: property value to set
        :return: it returns boolean value for successful change property operation
        """
        try:
            config = self.load_properties_file()
            config[section][property_name] = property_value

            with open(self.config_path, 'w') as configfile:
                config.write(configfile)

            return True

        except Exception as ex:
            self.log.error("Failed to change ini/properties file.", ex)
            print_stack()
            return False
