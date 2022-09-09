Framework to automate the XXXX Android App using Appium and Python with PyTest as Testing Framework. It uses Allure Reporting tool for Report Generation.

#### .apk or .ipa binary placement
1. Place the .apk binary in the directory - binary/android/<app_name.apk>
2. Place the .ipa binary in the directory - binary/iOS/<app_name.ipa>

#### Configuration Management for Appium Clients(Android/iOS) through configs/config.ini
1. Include the appium desired capabilities in the form of the name value pairs and in runtime it can be used to invoke the 
   android driver or iOS driver or any driver we need.
2. UiAutomator2 is driver client for automating the Android apps through Appium.
3. Include the name value pairs for android appium desired capabilities under the section - Cap_Android
4. Once the new name value pairs is added, update the get_driver_instance() python method available in directory - utility/support/driver_factory.py/get_driver_instance()
   under the **desired_caps python dict** variable available.
5. Always refer the url - http://appium.io/docs/en/writing-running-appium/caps/ for getting the information about appium desired capabilities available.
6. Key defined in utility/support/driver_factory.py/get_driver_instance() method's **desired_caps python dict** variable should be valid value from appium desired capabilities.
7. If **platform is set as android** under **App** section of config.ini, Cap_Android driver variables would be passed at runtime for driver instantiation.

#### Locator Strategy or Locators Fetched Categorized
1. locators/common directory have locators strategy fetched for both Guest and Registered user common screen flows.
2. locators/registered directory have locators strategy fetched for registered user flows.
3. All of the locator strategy available in selenium or appium will be supported in this framework 

#### Page Object Model(POM)
1. POM is created is each and every page of the Application Under Test(AUT).
2. pages/common directory have POM strategy methods fetched for both Guest and Registered user common screen flows.
3. pages/registered directory have POM strategy methods fetched for registered user flows.

#### Logs, Screenshots
1. Debug logs are available in logs/ directory.
2. Failure scenario screenshots are available in screenshots/ directory.

#### Framework and Support Utility Concepts and Methods
1. framework/ directory have utility methods for config file or property file reading, json or yaml file reading,
   reporting related utilities and other useful utility methods.
2. support/ directory have utility methods for text validations, appium driver instantiation, generalized appium and selenium methods to
   interact with Web Elements available.
3. support/ui_helpers.py python file have wrapper methods for differnt selenium or appium concepts.


#### Test Data for Framework
1. test_data/user_info.json file have different user related login and profile related info.
2. test_data/general_info.json file have general information specific to clinic available/displayed to the patient.
3. test_data/global_variables.py file have global variables and it wld be referenced across the framework during runtime.
4. test_data/brands_test_data/*.json - Have individual clinic information for booking appointment and validating the appointment flows.

#### Report Generation
1. This framework uses the interactive allure commandline plugin for generating the HTML reports.
2. Refer this URL - https://docs.qameta.io/allure/#_get_started for configuration.
3. This framework would create the test results in the form of **.txt and .json** and this is available in reports/* directory.
4. This intermediate files would be generated as part of pytest command invoked.
5. View the html reports using the command - allure open final_report



##### Execute the test and Generate the Allure Reports
#Not generating history trends and if it is integrated with jenkins/any CI/CD trends and history would be available
py.cleanup -p && py.test -v -m "not cancel_appointment" tests/test_manager_registered.py --platform=android --brand irvine_rosslyn --apptmt Dental --user mfa_disabled --provider custom_random --timeslot action=random --alluredir reports & allure generate reports -o final_report --clean 

#### Executing all appointment types one after another
py.cleanup -p && py.test -v tests/cmdline_workflow/test_01_registered_scenario_workflow_self_back_to_back_appmnts_different_types.py --platform=android --brand <brand_name> --apptmt <apptmt_type> --user <user_name> --flow <flow_type> --alluredir reports & allure generate reports -o final_report --clean


#### Notes
1. Don't mention the class name with TestSomePage, because would need like that.
2. Also inside the pytest anotated classes, tests created are sorted alphabetically while running most of the times.
3. so to avoid the above issue, class name should starts with RegistrationPageTests.
4. Also test filename should starts with registered_welcome_screen_tests.py # Not needed eventhough if we put like this sorting not works

### Appium Device Farm(Have to Implement)

https://github.com/AppiumTestDistribution/appium-device-farm

https://github.com/sudharsan-selvaraj/appium-dashboard-plugin

Boilerplate:
============
https://github.com/karimelkomy/Python-Test-Automation-Framework

https://github.com/Abhilash04/AppiumPythonHybridFramework
https://github.com/ikostan/TestAutomationFrameworkUsingAppiumWithPython/tree/master/tests

https://github.com/WasiqB/coteafs-appium/blob/master/src/test/resources/test-config.yaml
https://qxf2.com/blog/appium-mobile-automation/
https://dzone.com/articles/appium-tutorial-for-complete-beginners
https://www.browserstack.com/app-automate/appium-python
https://developer.nevercode.io/docs/appium-tests-written-in-python
https://www.appcoda.com/automated-ui-testing-appium/
https://github.com/topics/appium-framework

http://toolsqa.com/mobile-automation/appium/appium-tutorial/
http://toolsqa.com/mobile-automation/appium/set-up-android-environment-path/
http://blogs.quovantis.com/appium-basics-part-1-pre-requisites-and-setting-up-your-appium-environment-for-windows/
https://scrolltest.com/2016/02/21/appium-introduction/
