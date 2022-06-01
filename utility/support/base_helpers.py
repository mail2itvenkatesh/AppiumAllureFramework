import logging
# from traceback import print_stack
# from utility.support.ui_helpers import UIHelpers
# from configparser import ConfigParser
import utility.framework.logger_utility as log_utils
import imaplib
import email
import re
import datetime
from PIL import Image, ImageDraw
import json, sys, os
from utility.framework.data_reader_utility import DataReader

def make_orderer():
    order = {}

    def ordered(f):
        order[f.__name__] = len(order)
        return f

    def compare(a, b):
        return [1, -1][order[a] < order[b]]

    return ordered, compare

'''
usage in module before start of the class
    ordered, compare = make_orderer()
unittest.defaultTestLoader.sortTestMethodsUsing = compare

https://codereview.stackexchange.com/questions/122532/controlling-the-order-of-unittest-testcases
'''
#class BaseHelpers(UIHelpers):
class BaseHelpers(object):
    """
    This class includes basic reusable base_helpers.
    """
    log = log_utils.custom_logger(logging.INFO)

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    def identify_space_in_sentence(self, text):
        """
        Identify whether space is available in the text or not
        :param text: text as string
        :return: space count
        """
        count=0
        for a in text:
            if (a.isspace()) == True:
                count += 1

        return count

    def generate_random_integer(self, rnge=9999):
        """
        Generate the random integer from the range
        :param rnge: rnge as int
        :return: int
        """
        import random
        return random.randint(0, rnge)

    def sigpad2image_write_as_file(self, pincolor=(0, 0, 255)):
        """
        Creates an image from the JSON string and writes it to a file.
        :param jsonsig: The JSON representing the signature. Mentioned inside
        :param output_image: The path to the default image. Default="signature.png" Mentioned inside
        :param input_image: The path to the input image. Default="blanksig.png" Mentioned inside
        :param pincolor: the ink's color. Default=(0,0,255). This is blue
        :return: str - A string containing the output image path.
        """
        BLANK_IMAGE = r"blanksig.png"
        jsonsig = """[{"lx":32,"ly":13,"mx":32,"my":12},{"lx":32,"ly":11,"mx":32,"my":13},{"lx":31,"ly":11,"mx":32,"my":11},{"lx":30,"ly":11,"mx":31,"my":11},{"lx":29,"ly":11,"mx":30,"my":11},{"lx":28,"ly":11,"mx":29,"my":11},{"lx":26,"ly":11,"mx":28,"my":11},{"lx":23,"ly":11,"mx":26,"my":11},{"lx":21,"ly":11,"mx":23,"my":11},{"lx":19,"ly":11,"mx":21,"my":11},{"lx":17,"ly":11,"mx":19,"my":11},{"lx":15,"ly":11,"mx":17,"my":11},{"lx":13,"ly":11,"mx":15,"my":11},{"lx":12,"ly":12,"mx":13,"my":11},{"lx":11,"ly":12,"mx":12,"my":12},{"lx":10,"ly":13,"mx":11,"my":12},{"lx":9,"ly":13,"mx":10,"my":13},{"lx":8,"ly":14,"mx":9,"my":13},{"lx":7,"ly":14,"mx":8,"my":14},{"lx":6,"ly":15,"mx":7,"my":14},{"lx":6,"ly":16,"mx":6,"my":15},{"lx":5,"ly":17,"mx":6,"my":16},{"lx":3,"ly":18,"mx":5,"my":17},{"lx":2,"ly":19,"mx":3,"my":18},{"lx":2,"ly":20,"mx":2,"my":19},{"lx":1,"ly":21,"mx":2,"my":20},{"lx":1,"ly":22,"mx":1,"my":21},{"lx":0,"ly":23,"mx":1,"my":22},{"lx":0,"ly":24,"mx":0,"my":23},{"lx":0,"ly":25,"mx":0,"my":24},{"lx":0,"ly":26,"mx":0,"my":25},{"lx":0,"ly":27,"mx":0,"my":26},{"lx":0,"ly":28,"mx":0,"my":27},{"lx":0,"ly":29,"mx":0,"my":28},{"lx":1,"ly":29,"mx":0,"my":29},{"lx":1,"ly":30,"mx":1,"my":29},{"lx":2,"ly":30,"mx":1,"my":30},{"lx":3,"ly":30,"mx":2,"my":30},{"lx":4,"ly":30,"mx":3,"my":30},{"lx":5,"ly":30,"mx":4,"my":30},{"lx":6,"ly":30,"mx":5,"my":30},{"lx":7,"ly":30,"mx":6,"my":30},{"lx":8,"ly":30,"mx":7,"my":30},{"lx":8,"ly":29,"mx":8,"my":30},{"lx":10,"ly":29,"mx":8,"my":29},{"lx":11,"ly":28,"mx":10,"my":29},{"lx":12,"ly":28,"mx":11,"my":28},{"lx":12,"ly":27,"mx":12,"my":28},{"lx":13,"ly":27,"mx":12,"my":27},{"lx":14,"ly":27,"mx":13,"my":27},{"lx":15,"ly":26,"mx":14,"my":27},{"lx":16,"ly":26,"mx":15,"my":26},{"lx":16,"ly":25,"mx":16,"my":26},{"lx":17,"ly":25,"mx":16,"my":25},{"lx":18,"ly":24,"mx":17,"my":25},{"lx":18,"ly":23,"mx":18,"my":24},{"lx":19,"ly":23,"mx":18,"my":23},{"lx":19,"ly":22,"mx":19,"my":23},{"lx":20,"ly":22,"mx":19,"my":22},{"lx":20,"ly":20,"mx":20,"my":22},{"lx":21,"ly":20,"mx":20,"my":20},{"lx":21,"ly":19,"mx":21,"my":20},{"lx":22,"ly":19,"mx":21,"my":19},{"lx":22,"ly":18,"mx":22,"my":19},{"lx":23,"ly":18,"mx":22,"my":18},{"lx":23,"ly":19,"mx":23,"my":18},{"lx":22,"ly":19,"mx":23,"my":19},{"lx":22,"ly":20,"mx":22,"my":19},{"lx":21,"ly":21,"mx":22,"my":20},{"lx":21,"ly":22,"mx":21,"my":21},{"lx":20,"ly":23,"mx":21,"my":22},{"lx":19,"ly":24,"mx":20,"my":23},{"lx":19,"ly":26,"mx":19,"my":24},{"lx":18,"ly":27,"mx":19,"my":26},{"lx":17,"ly":28,"mx":18,"my":27},{"lx":17,"ly":30,"mx":17,"my":28},{"lx":16,"ly":31,"mx":17,"my":30},{"lx":16,"ly":32,"mx":16,"my":31},{"lx":16,"ly":33,"mx":16,"my":32},{"lx":16,"ly":34,"mx":16,"my":33},{"lx":17,"ly":34,"mx":16,"my":34},{"lx":17,"ly":35,"mx":17,"my":34},{"lx":18,"ly":35,"mx":17,"my":35},{"lx":20,"ly":36,"mx":18,"my":35},{"lx":22,"ly":36,"mx":20,"my":36},{"lx":24,"ly":36,"mx":22,"my":36},{"lx":26,"ly":36,"mx":24,"my":36},{"lx":29,"ly":36,"mx":26,"my":36},{"lx":31,"ly":36,"mx":29,"my":36},{"lx":34,"ly":36,"mx":31,"my":36},{"lx":37,"ly":35,"mx":34,"my":36},{"lx":40,"ly":34,"mx":37,"my":35},{"lx":42,"ly":33,"mx":40,"my":34},{"lx":44,"ly":32,"mx":42,"my":33},{"lx":47,"ly":31,"mx":44,"my":32},{"lx":49,"ly":30,"mx":47,"my":31},{"lx":51,"ly":29,"mx":49,"my":30},{"lx":52,"ly":28,"mx":51,"my":29},{"lx":54,"ly":27,"mx":52,"my":28},{"lx":55,"ly":26,"mx":54,"my":27},{"lx":56,"ly":25,"mx":55,"my":26},{"lx":57,"ly":24,"mx":56,"my":25},{"lx":57,"ly":23,"mx":57,"my":24},{"lx":58,"ly":22,"mx":57,"my":23},{"lx":59,"ly":20,"mx":58,"my":22},{"lx":59,"ly":19,"mx":59,"my":20},{"lx":59,"ly":18,"mx":59,"my":19},{"lx":60,"ly":18,"mx":59,"my":18},{"lx":60,"ly":17,"mx":60,"my":18},{"lx":60,"ly":16,"mx":60,"my":17},{"lx":60,"ly":15,"mx":60,"my":16},{"lx":59,"ly":15,"mx":60,"my":15},{"lx":59,"ly":14,"mx":59,"my":15},{"lx":58,"ly":14,"mx":59,"my":14},{"lx":58,"ly":13,"mx":58,"my":14},{"lx":57,"ly":13,"mx":58,"my":13},{"lx":56,"ly":13,"mx":57,"my":13},{"lx":55,"ly":13,"mx":56,"my":13},{"lx":54,"ly":13,"mx":55,"my":13},{"lx":53,"ly":13,"mx":54,"my":13},{"lx":52,"ly":13,"mx":53,"my":13},{"lx":51,"ly":13,"mx":52,"my":13},{"lx":50,"ly":13,"mx":51,"my":13},{"lx":48,"ly":14,"mx":50,"my":13},{"lx":46,"ly":15,"mx":48,"my":14},{"lx":44,"ly":16,"mx":46,"my":15},{"lx":42,"ly":17,"mx":44,"my":16},{"lx":40,"ly":19,"mx":42,"my":17},{"lx":39,"ly":21,"mx":40,"my":19},{"lx":37,"ly":22,"mx":39,"my":21},{"lx":36,"ly":24,"mx":37,"my":22},{"lx":36,"ly":25,"mx":36,"my":24},{"lx":35,"ly":27,"mx":36,"my":25},{"lx":35,"ly":28,"mx":35,"my":27},{"lx":35,"ly":29,"mx":35,"my":28},{"lx":35,"ly":30,"mx":35,"my":29},{"lx":35,"ly":31,"mx":35,"my":30},{"lx":36,"ly":31,"mx":35,"my":31},{"lx":37,"ly":31,"mx":36,"my":31},{"lx":38,"ly":31,"mx":37,"my":31},{"lx":39,"ly":31,"mx":38,"my":31},{"lx":40,"ly":31,"mx":39,"my":31},{"lx":41,"ly":31,"mx":40,"my":31},{"lx":42,"ly":31,"mx":41,"my":31},{"lx":44,"ly":31,"mx":42,"my":31},{"lx":46,"ly":31,"mx":44,"my":31},{"lx":49,"ly":31,"mx":46,"my":31},{"lx":51,"ly":31,"mx":49,"my":31},{"lx":54,"ly":30,"mx":51,"my":31},{"lx":55,"ly":30,"mx":54,"my":30},{"lx":57,"ly":30,"mx":55,"my":30},{"lx":59,"ly":29,"mx":57,"my":30},{"lx":60,"ly":29,"mx":59,"my":29},{"lx":61,"ly":28,"mx":60,"my":29},{"lx":62,"ly":28,"mx":61,"my":28},{"lx":63,"ly":27,"mx":62,"my":28},{"lx":64,"ly":26,"mx":63,"my":27},{"lx":65,"ly":26,"mx":64,"my":26},{"lx":67,"ly":25,"mx":65,"my":26},{"lx":69,"ly":24,"mx":67,"my":25},{"lx":70,"ly":23,"mx":69,"my":24},{"lx":72,"ly":21,"mx":70,"my":23},{"lx":74,"ly":20,"mx":72,"my":21},{"lx":75,"ly":20,"mx":74,"my":20},{"lx":77,"ly":19,"mx":75,"my":20},{"lx":79,"ly":18,"mx":77,"my":19},{"lx":81,"ly":17,"mx":79,"my":18},{"lx":82,"ly":17,"mx":81,"my":17},{"lx":84,"ly":17,"mx":82,"my":17},{"lx":85,"ly":17,"mx":84,"my":17},{"lx":86,"ly":17,"mx":85,"my":17},{"lx":86,"ly":18,"mx":86,"my":17},{"lx":85,"ly":18,"mx":86,"my":18},{"lx":84,"ly":18,"mx":85,"my":18},{"lx":83,"ly":18,"mx":84,"my":18},{"lx":83,"ly":19,"mx":83,"my":18},{"lx":82,"ly":19,"mx":83,"my":19},{"lx":80,"ly":19,"mx":82,"my":19},{"lx":78,"ly":20,"mx":80,"my":19},{"lx":77,"ly":21,"mx":78,"my":20},{"lx":75,"ly":22,"mx":77,"my":21},{"lx":74,"ly":23,"mx":75,"my":22},{"lx":73,"ly":24,"mx":74,"my":23},{"lx":71,"ly":24,"mx":73,"my":24},{"lx":70,"ly":25,"mx":71,"my":24},{"lx":70,"ly":26,"mx":70,"my":25},{"lx":69,"ly":27,"mx":70,"my":26},{"lx":69,"ly":28,"mx":69,"my":27},{"lx":68,"ly":29,"mx":69,"my":28},{"lx":68,"ly":30,"mx":68,"my":29},{"lx":68,"ly":31,"mx":68,"my":30},{"lx":69,"ly":31,"mx":68,"my":31},{"lx":70,"ly":31,"mx":69,"my":31},{"lx":71,"ly":31,"mx":70,"my":31},{"lx":72,"ly":31,"mx":71,"my":31},{"lx":74,"ly":31,"mx":72,"my":31},{"lx":76,"ly":31,"mx":74,"my":31},{"lx":79,"ly":31,"mx":76,"my":31},{"lx":82,"ly":31,"mx":79,"my":31},{"lx":84,"ly":31,"mx":82,"my":31},{"lx":85,"ly":30,"mx":84,"my":31},{"lx":87,"ly":29,"mx":85,"my":30},{"lx":88,"ly":29,"mx":87,"my":29},{"lx":88,"ly":28,"mx":88,"my":29},{"lx":89,"ly":27,"mx":88,"my":28},{"lx":89,"ly":26,"mx":89,"my":27},{"lx":89,"ly":25,"mx":89,"my":26},{"lx":90,"ly":25,"mx":89,"my":25},{"lx":90,"ly":26,"mx":90,"my":25},{"lx":90,"ly":27,"mx":90,"my":26},{"lx":90,"ly":28,"mx":90,"my":27},{"lx":89,"ly":29,"mx":90,"my":28},{"lx":89,"ly":31,"mx":89,"my":29},{"lx":88,"ly":32,"mx":89,"my":31},{"lx":88,"ly":34,"mx":88,"my":32},{"lx":88,"ly":35,"mx":88,"my":34},{"lx":88,"ly":36,"mx":88,"my":35},{"lx":88,"ly":37,"mx":88,"my":36},{"lx":89,"ly":37,"mx":88,"my":37},{"lx":90,"ly":37,"mx":89,"my":37},{"lx":90,"ly":36,"mx":90,"my":37},{"lx":92,"ly":35,"mx":90,"my":36},{"lx":94,"ly":33,"mx":92,"my":35},{"lx":95,"ly":31,"mx":94,"my":33},{"lx":98,"ly":28,"mx":95,"my":31},{"lx":100,"ly":26,"mx":98,"my":28},{"lx":102,"ly":24,"mx":100,"my":26},{"lx":104,"ly":22,"mx":102,"my":24},{"lx":106,"ly":21,"mx":104,"my":22},{"lx":107,"ly":21,"mx":106,"my":21},{"lx":108,"ly":20,"mx":107,"my":21},{"lx":109,"ly":20,"mx":108,"my":20},{"lx":110,"ly":20,"mx":109,"my":20},{"lx":110,"ly":21,"mx":110,"my":20},{"lx":111,"ly":21,"mx":110,"my":21},{"lx":111,"ly":22,"mx":111,"my":21},{"lx":112,"ly":23,"mx":111,"my":22},{"lx":113,"ly":23,"mx":112,"my":23},{"lx":114,"ly":24,"mx":113,"my":23},{"lx":115,"ly":25,"mx":114,"my":24},{"lx":116,"ly":26,"mx":115,"my":25},{"lx":118,"ly":27,"mx":116,"my":26},{"lx":121,"ly":28,"mx":118,"my":27},{"lx":123,"ly":28,"mx":121,"my":28},{"lx":126,"ly":29,"mx":123,"my":28},{"lx":129,"ly":29,"mx":126,"my":29},{"lx":132,"ly":30,"mx":129,"my":29},{"lx":135,"ly":30,"mx":132,"my":30},{"lx":138,"ly":30,"mx":135,"my":30},{"lx":139,"ly":30,"mx":138,"my":30},{"lx":141,"ly":30,"mx":139,"my":30},{"lx":142,"ly":30,"mx":141,"my":30},{"lx":143,"ly":30,"mx":142,"my":30},{"lx":143,"ly":29,"mx":143,"my":30},{"lx":144,"ly":29,"mx":143,"my":29}]"""

        # Decode valid json or return None
        try:
            l = json.loads(jsonsig)
        except Exception as ex:
            print(ex)
            return None
        # Make sure its a signature or return None
        if "lx" not in l[0] or "my" not in l[0]:
            return None
        # create a blank image from out template
        im = Image.open(BLANK_IMAGE)
        # create a drawing object
        draw = ImageDraw.Draw(im)
        # iterate over our list of points and draw corresponding lines
        for i in l:
            draw.line((i["lx"], i["ly"], i["mx"], i["my"]), fill=pincolor, width=1)
        # delete our draw object (cleanup and free the memory)
        del draw

        # # save image
        # im.save(output_image, "PNG")
        # # get its path
        # BASE_DIR = os.path.dirname(os.path.abspath(output_image))
        # IMAGE_PATH = os.path.join(BASE_DIR, output_image)
        # return IMAGE_PATH

    def get_date(self,days=0):
        """
        Fetch current day date as form of new date format based upon timedelta
        :param days: days in int
        :return: date object in formatted string
        """
        return (datetime.date.today() + datetime.timedelta(days=days)).strftime("%b %d")

    def get_usa_date_format(self, days=0):
        """
        Fetch USA current day date as form of new date format based upon timedelta
        :param days: days in int
        :return: date object in formatted string
        """
        return (datetime.date.today() + datetime.timedelta(days=days)).strftime("%m/%d/%Y")

    def format_date_and_produce_day(self,date_with_month_fetched_from_app,year=DataReader().fetch_current_year()):
        """
        Get the date as input and return the day(weekday)
        :param date_with_month_fetched_from_app: date_with_month_fetched_from_app in string like Oct 10
        :param year: year in int
        :return: for today => Today, tomorrow => Tomorrow and further days => Thursday,Monday, etc
        """
        full_weekday_name = None

        if (datetime.date.today() + datetime.timedelta(days=0)).strftime("%b %d") == date_with_month_fetched_from_app:
            full_weekday_name = "Today"

        elif (datetime.date.today() + datetime.timedelta(days=1)).strftime("%b %d") == date_with_month_fetched_from_app:
            full_weekday_name = "Tomorrow"

        else:
            date_string = "{} {}".format(date_with_month_fetched_from_app, year)
            date_object = datetime.datetime.strptime(date_string, "%b %d %Y")
            print("date_object =", date_object)
            full_weekday_name = date_object.strftime("%A")

        return full_weekday_name

    def format_date_and_produce_day_for_apptmt_booking(self,date_with_month_fetched_from_app,year=DataReader().fetch_current_year()):
        """
        Get the date as input and return the day(weekday)
        :param date_with_month_fetched_from_app: date_with_month_fetched_from_app in string like Oct 10
        :param year: year in int
        :return: for today => Today, tomorrow => Tomorrow and further days => Thursday,Monday, etc
        """
        full_weekday_name = None

        if (datetime.date.today() + datetime.timedelta(days=0)).strftime("%b %d") == date_with_month_fetched_from_app:
            full_weekday_name = "Today"

        elif (datetime.date.today() + datetime.timedelta(days=1)).strftime("%b %d") == date_with_month_fetched_from_app:
            full_weekday_name = "Tomorrow"

        else:
            date_string = "{} {}".format(date_with_month_fetched_from_app, year)
            date_object = datetime.datetime.strptime(date_string, "%b %d %Y")
            print("date_object =", date_object)
            full_weekday_name = date_object.strftime("%A")

        return full_weekday_name


    def is_time_format(self,string):
        """
        This method is used to validate the time format available while booking the appointment
        :param string: string as str like 8:00 am or 12:56 pm or 08:34 am
        :return: True | False
        """
        time_re = re.compile(r'(^0?\d|1[0-2]):[0-5]\d\s*(?:am|pm)', re.M | re.I)
        return bool(time_re.match(string))

    def is_doctor_name_format(self,string):
        """
        This method is used to validate the doctor name format available while booking the appointment
        :param string: string as str like "Dr. Venkatesh Miller, MD"
        :return: True | False
        """
        #doctor_name_re = re.compile(r'(?:Dr|Mr)\.\s+[a-z\s]+\,\s*(?:MD|MBBS)', re.M | re.I)
        doctor_name_re = re.compile(r'[a-z\s]+\,\s*(?:MD|MBBS|BSN|HWC)', re.M | re.I)
        return bool(doctor_name_re.match(string))

    def is_payment_price_format(self, string):
        """
        This method is used to validate the payment price format available
        :param string: string as str like "$50.00"
        :return: True | False
        """
        payment_price_re = re.compile(r'(\$)(?:\d+\.)?\d+', re.M | re.I)
        return bool(payment_price_re.match(string))

    def is_estimated_time_value_format(self, string):
        """
        This method is used to validate the estimated time value format available
        :param string: string as str like "30 min/ 30 minutes"
        :return: True | False
        """
        #estimated_time = re.compile(r'(?:\d+)\s+(min)', re.M | re.I)
        estimated_time = re.compile(r'(?:\d+\s+Hour).*|(?:\d+\s+Minutes)', re.M | re.I) # Still have to optimize this regex
        return bool(estimated_time.match(string))

    def is_mobile_number_format(self, string):
        """
        This method is used to validate the mobile no format available
        :param string: string as str like (555) 123-4567
        :return: True | False
        """
        mobile_no = re.compile(r'^\(\d{1,3}\)\s+\d{1,3}\-\d{1,4}$', re.M | re.I)
        return bool(mobile_no.match(string))

    def is_date_format(self, string):
        """
        This method is used to validate the date format available
        :param string: string as str like 03/11/2020
        :return: True | False
        """
        # date_provided = re.compile(r'^(0[1-9]|1[0-2])\/(3[01]|[12][0-9]|0[1-9])\/[0-9]{4}$', re.M | re.I)
        # return bool(date_provided.match(string))

        try:
            datetime.datetime.strptime(string, '%m/%d/%Y')
            return True
        except ValueError:
            return False

    def no_of_clinics_available_format_with_zipcode(self, string):
        """
        This method is used to validate the text present in clinic locator
        :param string: string as str like 5 clinics near 92618
        :return: True | False
        """
        str_format = re.compile(r'(\d+\s+clinics near\s\d\w{0,4})', re.M | re.I)
        return bool(str_format.match(string))

    def no_of_providers_available_format_advanced_serach(self, service_type,string):
        """
        This method is used to validate the text present in Advanced Provider Search
        :param string: string as str like 5 Medical Providers
        :param service_type: service_type as str like Medical, Dental
        :return: True | False
        """
        str_format = re.compile(r'(\d+\s+{}\s Providers)'.format(service_type), re.M | re.I)
        return bool(str_format.match(string))

    def no_of_clinics_available_format(self, string, service_type):
        """
        This method is used to validate the text present in clinic locator
        :param string: string as str like 5 Clinics With Medical Services
        :param service_type: service_type as str like Medical, Dental
        :return: True | False
        """
        str_format = re.compile(r'(\d+\s+Clinics near {} Services)'.format(service_type), re.M | re.I)
        return bool(str_format.match(string))

    def no_of_articles_available_format(self, string, search_term):
        """
        This method is used to validate the articles text available
        :param string: string as str like 69 articles for Covid 19
        :param search_term: search_term as str like Covid 19, Diabetes
        :return: True | False
        """
        # 69 articles for Covid 19
        str_format = re.compile(r'(\d+\s+articles for {})'.format(search_term), re.M | re.I)
        return bool(str_format.match(string))

    def no_of_articles_results_in_detailed_load_more_results(self, string, search_term):
        """
        This method is used to validate the no of full articles
        :param string: string as str like 3 Results for
        :param search_term: search_term as str like Covid 19, Diabetes
        :return: True | False
        """
        # 69 articles for Covid 19
        str_format = re.compile(r'(\d+\s+articles for {})'.format(search_term), re.M | re.I)
        return bool(str_format.match(string))

    def clinic_miles_text_format(self, string):
        """
        This method is used to validate the miles (3.7 mi)text present in clinic locator address list
        :param string: string as str like 3.7 mi
        :return: True | False
        """
        # str_format = re.compile(r'^(\d+.\d\s+mi)$', re.M | re.I)
        str_format = re.compile(r'^[0-9]{1,11}(?:\.[0-9]{1,3})?\s+mi$', re.M | re.I)
        return bool(str_format.match(string))

    def parse_timezone_comparision_info(self, comparison_text):
        """
        This method is used to fetch and parse the timezone and comparison hours info
        :param comparison_text: comparison_text as str like Hours are shown in this clinic's local time (America/Los_Angeles), which is 12 hours 30 minutes later than your current local time (Asia/Calcutta).
        :return:
        """
        splitted_comp_text = comparison_text.replace(')', '').split('(')
        self.log.info("Splitted Comparison text info is {}".format(splitted_comp_text))
        self.log.info({'clinic_local_timezone': splitted_comp_text[1].split(',')[0].strip(), 'timezone_diff_clinic_local': splitted_comp_text[1].split(',')[1].strip(), 'device_timezone': splitted_comp_text[2].replace('.', '').strip()})
        return {'clinic_local_timezone': splitted_comp_text[1].split(',')[0].strip(), 'timezone_diff_clinic_local': splitted_comp_text[1].split(',')[1].strip(), 'device_timezone': splitted_comp_text[2].replace('.', '').strip()}

    def provide_tz_database_time_zones(self, timezone_info):
        """
        Fetch the TZ timezone information by accepting the full timezone info. Ref URL :: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        :param timezone_info: timezone_info as string and example is Indian Standard Time
        :return: Time Zone info like Asia/Calcutta
        """
        fetched_tz_timezone = None

        if timezone_info in ('Indian Standard Time','India Standard Time', 'India Daylight Time'):
            fetched_tz_timezone = "Asia/Calcutta"

        elif timezone_info in ('Pacific Standard Time','Pacific Daylight Time', 'Pacific Time'):
            fetched_tz_timezone = "US/Pacific"

        elif timezone_info in ('Eastern Standard Time','Eastern Daylight Time', 'Eastern Time'):
            fetched_tz_timezone = "US/Eastern"

        elif timezone_info in ('Mountain Standard Time','Mountain Daylight Time', 'Mountain Time'):
            fetched_tz_timezone = "US/Mountain"

        elif timezone_info in ('Central Standard Time','Central Daylight Time', 'Central Time'):
            fetched_tz_timezone = "US/Central"

        else:
            fetched_tz_timezone = None

        return fetched_tz_timezone

    # https://stackabuse.com/how-to-get-the-current-date-and-time-in-python/
    def timezone_date_identify_compare(self, timezone1, timezone2):
        """
        Method to compare and verify whether two timezones date is equal or not
        :param timezone1: timezone1 as string .Eg America/Los_Angeles
        :param timezone2: timezone1 as string Eg Asia/Calcutta
        :return:
        """
        flag = None
        import pytz
        from datetime import datetime

        tz = datetime.now(pytz.timezone(self.provide_tz_database_time_zones(timezone1))).date()
        tz1 = datetime.now(pytz.timezone(self.provide_tz_database_time_zones(timezone2))).date()

        self.log.info("Timezone1 date is {} and Timezone2 date is {}".format(tz, tz1))
        print("Timezone1 date is {} and Timezone2 date is {}".format(tz, tz1))

        if tz == tz1:
            self.log.info("Timezone1 date - {} and Timezone2 date - {} are equal".format(tz, tz1))
            # print("Timezone1 date - {} and Timezone2 date - {} are equal".format(tz, tz1))
            flag = True
        else:
            self.log.info("Timezone1 date - {} and Timezone2 date - {} are not equal".format(tz, tz1))
            flag = False

        return flag

    def fetch_timezone_by_abbreviation(self, timezone_abbreviation):
        """
        Method to fetch the timezone using the abbreviated timezone form
        :param timezone_abbreviation: timezone_abbreviation as string .Eg IST
        :return:
        """

        timezone_info = None

        if timezone_abbreviation == "IST":
            timezone_info = "India Standard Time"

        elif timezone_abbreviation == "GST":
            # This timezone is for Dubai/Gulf Standard Time. Windows doesn't have GST listed.So AST is same as GST
            timezone_info = "Arabian Standard Time"

        elif timezone_abbreviation == "PST":
            timezone_info = "Pacific Standard Time"

        elif timezone_abbreviation == "Hawaii":
            timezone_info = "Hawaiian Standard Time"

        elif timezone_abbreviation == "Alaska":
            timezone_info = "Alaskan Standard Time"

        elif timezone_abbreviation == "MST":
            timezone_info = "Mountain Standard Time"

        elif timezone_abbreviation == "CST":
            timezone_info = "Central Standard Time"

        elif timezone_abbreviation == "EST":
            timezone_info = "Eastern Standard Time"

        elif timezone_abbreviation == "WAST":
            timezone_info = "W. Australia Standard Time"

        elif timezone_abbreviation == "CAST":
            timezone_info = "Cen. Australia Standard Time"

        elif timezone_abbreviation == "ACST":
            timezone_info = "AUS Central Standard Time"

        else:
            # Setting to default timezone of India
            timezone_info = "India Standard Time"

        return timezone_info

    def fetch_timezone_by_expanded_form(self, timezone_retrieved):
        """Method to fetch the timezone abbreviation by giving the expaned form """

        timezone_abbreviation = None

        if timezone_retrieved in ('India Standard Time', 'India Daylight Time'):
            timezone_abbreviation = 'IST'

        elif timezone_retrieved in ('Arabian Standard Time', 'Arabian Daylight Time'):
            timezone_abbreviation = 'GST'

        elif timezone_retrieved in ('Pacific Standard Time', 'Pacific Daylight Time'):
            timezone_abbreviation = 'PST'

        elif timezone_retrieved in ('Hawaiian Standard Time', 'Hawaiian Daylight Time'):
            timezone_abbreviation = 'Hawaii'

        elif timezone_retrieved in ('Alaskan Standard Time', 'Alaskan Daylight Time'):
            timezone_abbreviation = 'Alaska'

        elif timezone_retrieved in ('Mountain Standard Time', 'Mountain Daylight Time'):
            timezone_abbreviation = 'MST'

        elif timezone_retrieved in ('Central Standard Time', 'Central Daylight Time'):
            timezone_abbreviation = 'CST'

        elif timezone_retrieved in ('Eastern Standard Time', 'Eastern Daylight Time'):
            timezone_abbreviation = 'EST'

        elif timezone_retrieved in ('W. Australia Standard Time', 'W. Australia Daylight Time'):
            timezone_abbreviation = 'WAST'

        elif timezone_retrieved in ('Cen. Australia Standard Time', 'Cen. Australia Daylight Time'):
            timezone_abbreviation = 'CAST'

        elif timezone_retrieved in ('AUS Central Standard Time', 'AUS Central Daylight Time'):
            timezone_abbreviation = 'ACST'

        else:
            timezone_abbreviation = None

        return timezone_abbreviation

    def get_body(self, msg):
        """
        This method is used to get the mail body
        :param msg: input parameter as raw message
        :return: it returns the mail body according to content type
        """

        for part in msg.walk():
            con_type = part.get_content_type()

            if con_type == 'text/html':
                payload = part.get_payload(decode=True)
                if payload is not None:
                    return payload
            elif con_type == 'text/plain':
                payload = part.get_payload(decode=True)
                if payload is not None:
                    return payload
            elif con_type == 'multipart/mixed':
                payload = part.get_payload(decode=True)
                if payload is not None:
                    return payload
            elif con_type == 'multipart/alternative':
                payload = part.get_payload(decode=True)
                if payload is not None:
                    return payload
            else:
                return None

    def get_reset_password_url(self, host, username, password, subject, site_url):
        """
        This method is used to get the reset password link from mail
        :param host: imap ssl host name
        :param username: email id of the user
        :param password: password for registered email id to log into mail
        :param subject: query parameter to search for specific subject in mails
        :param site_url: website url to reset the password for
        :return: it returns the password reset url
        """
        token_value = ""
        try:

            # Connect to the server
            print('Connecting to ' + host)
            mail = imaplib.IMAP4_SSL(host)

            # Login to our account
            mail.login(username, password)

            mail_list = mail.list()
            # print(mail_list)

            mail.select()
            search_query = '(SUBJECT "' + subject + '")'
            result, data = mail.uid('search', None, search_query)
            ids = data[0]

            # list of uids
            id_list = ids.split()

            i = len(id_list)
            for x in range(i):
                if x == 0:
                    latest_email_uid = id_list[0]
                else:
                    latest_email_uid = id_list[i - x]

                # fetch the email body (RFC822) for the given ID
                result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
                raw_email = email_data[0][1]

                # converts byte literal to string removing b''
                raw_email_string = raw_email.decode('UTF-8')
                email_message = email.message_from_string(raw_email_string)

                final_payload = (self.get_body(email_message)).decode('UTF-8')

                if final_payload is not None:
                    pattern = re.compile('token=(.*)">')
                    token = pattern.findall(final_payload)
                    if len(token) != 0:
                        token_value = token[0]
                        mail.uid('STORE', latest_email_uid, '+FLAGS', '(\\Deleted)')
                        break

            mail.expunge()
            mail.close()
            mail.logout()

            if token_value != "":
                return site_url + "/password/reset?token=" + token_value
            else:
                return None

        except Exception as ex:
            self.log.error("Failed to get reset password link from mail.", ex)
            return None

    def clean_mailbox(self, host, username, password, subject):
        """
        This method is used to clean the reset password link message from mail /clean the mailbox
        :param host: imap ssl host name
        :param username: email id of the user
        :param password: password for registered email id to log into mail
        :param subject: query parameter to search for specific subject in mails
        :return: returns boolean value for successful cleanup
        """
        token_value = ""
        try:

            # Connect to the server
            print('Connecting to ' + host)
            mail = imaplib.IMAP4_SSL(host)

            # Login to our account
            mail.login(username, password)

            mail_list = mail.list()
            # print(mail_list)

            mail.select()
            search_query = '(SUBJECT "' + subject + '")'
            result, data = mail.uid('search', None, search_query)
            ids = data[0]

            # list of uids
            id_list = ids.split()

            i = len(id_list)
            for x in range(i):
                if x == 0:
                    latest_email_uid = id_list[0]
                else:
                    latest_email_uid = id_list[i - x]

                mail.uid('STORE', latest_email_uid, '+FLAGS', '(\\Deleted)')

            mail.expunge()
            mail.close()
            mail.logout()

            self.log.info("Cleaned up all mail with subject as: " + subject)
            return True
        except Exception as ex:
            self.log.error("Failed to get reset password link from mail.", ex)
            return False

    def identify_provide_day(self,day_count):
        """
        Get the days in integer and identify the day for appointment booking
        :param day_count: day_count in int
        :return: for today => Today, tomorrow => Tomorrow and further days => Thursday,Monday, etc
        """
        day_identified = None

        fetched_date_day = (datetime.date.today() + datetime.timedelta(days=day_count)).strftime("%b %d")
        today_info_fetched = datetime.date.today()

        if fetched_date_day == datetime.date.today().strftime("%b %d"):
            if today_info_fetched.strftime("%A") not in ('Sunday', 'Saturday'):
                self.log.info("Current Day is Today")
                day_identified = "Today"
            else:
                self.log.info("Current Day is {} and hence not taken into consideration".format(today_info_fetched.strftime("%A")))

                if datetime.date.today().strftime("%A") == "Saturday":
                    self.log.info("Day to be passed is {}".format("Monday"))
                    day_identified = "Monday"
                else:
                    self.log.info("Day to be passed is {}".format("Tomorrow"))
                    day_identified = "Tomorrow"

        if fetched_date_day != datetime.date.today().strftime("%b %d"):
            self.log.info("Current Day is {} and given day is {}".format(today_info_fetched.strftime("%A"), fetched_date_day))
            diff = (datetime.date.today() + datetime.timedelta(days=day_count)) - datetime.date.today()
            self.log.info("Day difference is {}".format(diff.days))

            if diff.days == 1 and today_info_fetched.strftime("%A") not in ('Sunday', 'Saturday'):
                self.log.info("Tomorrow")
                day_identified = "Tomorrow"

            elif diff.days == 1 and today_info_fetched.strftime("%A") == "Saturday":
                self.log.info("Monday")
                day_identified = "Monday"

            elif diff.days == 1 and today_info_fetched.strftime("%A") == "Sunday":
                self.log.info("Tomorrow")
                day_identified = "Tomorrow"

            else:
                if (datetime.date.today() + datetime.timedelta(days=day_count)).strftime("%A") == "Saturday":
                    self.log.info("Day to be passed is {}".format("Monday"))
                    day_identified = "Monday"

                elif (datetime.date.today() + datetime.timedelta(days=day_count)).strftime("%A") == "Sunday":
                    self.log.info("Day to be passed is {}".format("Tomorrow"))
                    day_identified = "Tomorrow"
                else:
                    day_to_be_passed = (datetime.date.today() + datetime.timedelta(days=day_count)).strftime("%A")
                    self.log.info("Day to be passed is {}".format(day_to_be_passed))
                    day_identified = day_to_be_passed

        return day_identified

    def timezone_date_identify_compare_v2(self, country):
        """
        Method to compare and verify whether two timezones date is equal or not
        :param country: country as string .Eg USA
        :return: Date list
        """
        import pytz
        from datetime import datetime
        date_collector = []

        if country == "USA":
            for tz in ["US/Pacific", "US/Eastern", "US/Mountain", "US/Central"]:
                date_collector.append(datetime.now(pytz.timezone(tz)).date().strftime("%b %d"))

        self.log.info("Available date for the {} Country is {}".format(country, date_collector))

        return date_collector

    # def validate_other_clinic_timeslot_info_format(self, time_slot, hospital_name, hour_min_info, mile_info, actual_string):
    def validate_other_clinic_timeslot_info_format(self, hospital_name, actual_string):
        """
        This method is used to validate the text present(08:00 AM at Irvine General Hosptal 5 mins (1.6 mi) away.)
        :param time_slot: time_slot as str like 08:00 AM | 17:00 AM
        :param hospital_name: hospital_name as str
        :param hour_min_info: hour_min_info as str like 0 mins/ 1 hour 30 mins
        :param mile_info: mile_info as str like 1.6/9 mi
        :return: True | False
        """
        str_format = re.compile(r'(^[0-2]?\d|1[0-2]):[0-5]\d\s*(?:AM|PM)\s+at\s+{}\s+((?:\d+\s+hour).*|(?:\d+\s+mins)\s+{}{})'.format(hospital_name,"/\([0-9]{1,11}(?:\.[0-9]{1,3})?\s+mi\)/\s+","away."), re.M | re.I)
        return bool(str_format.match(actual_string))

# b = BaseHelpers()
# print(b.generate_random_integer())
# print(b.identify_space_in_sentence("972-535-1111"))
# print(b.timezone_date_identify_compare_v2("USA"))
# print(b.validate_other_clinic_timeslot_info_format("Irvine General Hosptal","17:00 PM at Irvine General Hosptal 5 mins (1.6 mi) away."))

# print(b.identify_provide_day(day_count=2))