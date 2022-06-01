from utility.support.driver_factory import DriverFactory
from utility.framework.data_reader_utility import DataReader
import pytest
from test_data import global_variables as gv
import argparse

#https://stackoverflow.com/questions/29986185/python-argparse-dict-arg
#https://github.com/Parsely/streamparse/blob/master/streamparse/cli/common.py
class StoreDictKeyPair(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self._nargs = nargs
        super(StoreDictKeyPair, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        time_dict = {}
        print("values: {}".format(values))
        if values is not None:
            for kv in values:
                k, v = kv.split("=")
                time_dict[k] = v
        else:
            # parser.error("{0} ".format(option_string))
            # pytest.fail("{0} ".format(option_string))
            raise ValueError("{0} ".format(option_string))

        setattr(namespace, self.dest, time_dict)

#https://stackoverflow.com/questions/49824248/allow-argparse-nargs-to-accept-comma-separated-input-with-choices
def pytest_addoption(parser):
    """ Implement pytest hook that defines custom command line options to be passed to pytest.
        Args:
            parser (parser config object): Holds the pytest command line options information

        Attributes:
            --platform option (str) : Retrieve the platform name for test execution
            --brand option (str) : Retrieve the partner/brand name for test execution
            --timeslot option (dict) : RUse this option to choose timeslot for appointment booking during test execution
            --apptmt option (str) : Appointment Type for booking like Medical, Dental, Cardiology, etc for test execution
            --user option (str) : user info for test execution
            --provider option (str) : This option is used to choose the medical provider for the appointment type provided
            --flow option (str) : If option is simple, then Choose Another Appointment btn wld be clicked and option is custom, then Choose This Appointment btn wld be clicked

        Returns:
                parser object which can be accessible via request fixture available to pytest

        """
    parser.addoption("--platform", action="store", required=False, default='android',help="Mobile Platform like android,ios")
    parser.addoption("--brand", action="store", required=False, default='hps', choices= DataReader().fetch_partner_brands_list(),help="Use this option to fetch partners information")
    parser.addoption("--timeslot", action=StoreDictKeyPair, required=False, nargs='+', metavar="KEY=VAL",help="Use this option to choose timeslot for appointment booking. For random timeslot, give --timeslot action=default to use default from the nextavailable screen available,give --timeslot action=random and for custom timeslot, give --timeslot action=custom day=Today/Tomorroe/Friday,"
                                                                                                              "session=Morning/Evening/Afternoon, for automation suite predefined test data select, --timeslot auto_run and then day,time and session would be automatically selected")
    parser.addoption("--apptmt", action="store", required=False, default='Medical',help="Appointment Type for booking like Medical, Dental, Cardiology, etc")
    parser.addoption("--user", action="store", required=False, default='mfa_disabled',help="User info for apointment booking and default is mfa_disabled user")
    parser.addoption("--provider", action="store", required=False, default='recommend',choices=['recommend', 'custom', 'custom_random'],help="This option is used to choose the medical provider for the appointment type provided")
    parser.addoption("--flow", action="store", required=False, default='direct',choices=['direct', 'custom'],help="If option is simple, then Choose Another Appointment btn wld be clicked and option is custom, then Choose This Appointment btn wld be clicked")

def pytest_collection_modifyitems(config, items):
    """ PytestHook to verify whether commandline arguments are available to the pytest runtime for later usage

        Args:
            config (_pytest.config.Config) object: Holds command line arguments passed and other config info
            items (items object): Holds the pytest mark and parameterize objects

        Attributes:
            --platform option (str) : Retrieve the platform name for test execution
            --brand option (str) : Retrieve the partner/brand name for test execution
            --timeslot option (dict) : RUse this option to choose timeslot for appointment booking during test execution
            --apptmt option (str) : Appointment Type for booking like Medical, Dental, Cardiology, etc for test execution
            --user option (str) : user info for test execution
            --provider option (str) : This option is used to choose the medical provider for the appointment type provided
            --flow option (str) : If option is simple, then Choose Another Appointment btn wld be clicked and option is custom, then Choose This Appointment btn wld be clicked

        Returns:
            Fails the pytest session if requested commandline arguments is not available else return nothing
    """

    if config.getoption("--brand") or config.getoption("--platform") or config.getoption("--apptmt") or config.getoption("--user") or config.getoption("--timeslot") or config.getoption("--provider") or config.getoption("--flow"):
        return

    pytest.fail("need to provide either --platform, --brand,--apptmt, --user, --timeslot ,--provider, --flow option for test execution")

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture(scope="session", name='get_config_params')
def get_config_params(request):
    config_param = {}
    config_param["brand"] = request.config.getoption("--brand")
    config_param["user"] = request.config.getoption("--user")
    config_param["timeslot"] = request.config.getoption("--timeslot")
    config_param["provider"] = request.config.getoption("--provider")
    config_param["flow"] = request.config.getoption("--flow")
    return config_param

#https://stackoverflow.com/questions/12411431/how-to-skip-the-rest-of-tests-in-the-class-if-one-has-failed
# https://github.com/pytest-dev/pytest/issues/2417 ## Access the commandline line argument from conftest.py file to another test files
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "incremental: mark test to run incremental test i.e tests stop after certain no of failures"
    )

    config.addinivalue_line(
        "markers", "cleanup: mark test to cancel the existing appointments available"
    )

    config.addinivalue_line(
        "markers", "login: mark test to run login related tests only"
    )

    config.addinivalue_line(
        "markers", "navigation: mark test to run only page navigation related tests"
    )

    config.addinivalue_line(
        "markers", "navigation_specific: mark test to run only specific page navigation related tests"
    )

    config.addinivalue_line(
        "markers", "review_navigation: mark test to run Review Your Information specific page navigation related tests"
    )

    config.addinivalue_line(
        "markers", "add_dependent: mark test to run tests related to dependent add"
    )

    config.addinivalue_line(
        "markers", "edit_dependent: mark test to run tests related to dependent add"
    )

    config.addinivalue_line(
        "markers", "delete_dependent: mark test to run tests related to dependent delete"
    )

    config.addinivalue_line(
        "markers", "book_appointment: mark test to book an appointment"
    )

    config.addinivalue_line(
        "markers", "reschedule_appointment: mark test to reschedule an appointment"
    )

    config.addinivalue_line(
        "markers", "cancel_appointment: mark test to cancel an appointment"
    )

    config.addinivalue_line(
        "markers", "check_in: mark test to handle the check in flow"
    )

    config.addinivalue_line(
        "markers", "add_insurance: mark test to add insurance for payment"
    )

    config.addinivalue_line(
        "markers", "delete_insurance: mark test to delete insurance available"
    )

    config.addinivalue_line(
        "markers", "regression: mark test to run all regression test scenarios or test cases"
    )

    config.addinivalue_line(
        "markers", "smoke: mark test to run all smoke test scenarios or test cases"
    )

    config.addinivalue_line(
        "markers", "registered: mark test to run all registered user flow tests"
    )

    config.addinivalue_line(
        "markers", "guest: mark test to run all guest user flow tests"
    )

    config.addinivalue_line(
        "markers", "self_single_apptmt: mark test to book single self appointment only"
    )

    config.addinivalue_line(
        "markers", "self_dependent_continuous_apptmt: mark test to book self and dependent as continuous appointments"
    )

    config.addinivalue_line(
        "markers", "dependent_single_apptmt: mark test to book single dependent appointment only"
    )

    gv.service_brand = config.getoption("--brand")
    gv.cmdline_apptmt_type = config.getoption("--apptmt")

def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            #pytest.xfail("previous test failed ({})".format(previousfailed.name))
            pytest.mark.xfail("previous test failed ({})".format(previousfailed.name),run=True) #Even on failure tests will run

#@pytest.fixture(scope="class")
@pytest.fixture(scope="session")
def get_driver(request, platform):
    try:
        print("session_level_setup: Running session level setup.")
        df = DriverFactory(platform)
        driver = df.get_driver_instance()
        driver.reset()
        session = request.node
        for item in session.items:
            cls = item.getparent(pytest.Class)
            setattr(cls.obj, "driver", driver)
        yield
        print("session_level_setup: Running session level teardown.")

        '''
            Example Usage of driver.reset in appium:
            
            1. I want to test my application with different set of test data for login functionality. 
               Once i open my app and give username and password and close the app and open the app again 
               to test with another set of credentials.
            
            2. Reset the currently running app for this session.which is going to clear user data and restart the app.
        
        '''
        driver.reset()

    except (Exception) as e:
        print("Exception Occurred :::: e".format(e))


