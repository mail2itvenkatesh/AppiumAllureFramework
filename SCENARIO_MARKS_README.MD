### Pytest Marker Expressions

| **FLOW MARKER OPTIONS**                                                          | **DESCRIPTION**                                                                                            |
| :------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------  |
| "cleanup"                                                                        | Cancel the existing appointments if available                                                              |
| "login"                                                                          | Run Login specific tests                                                                                   |
| "navigation"                                                                     | Navigation from one page to another page                                                                   |
| "navigation_specific"                                                            | Run only specific page navigation related tests(as of now this utilized for add dependent/edit dependent flow to avoid common navigation marker                                                                     |
| "cleanup or login or navigation or book_appointment"                             | Cancel the existing appointments if available,Login,navigation and book myself appointment                 |
| "cleanup or login"                                                               | Cancel the existing appointments if available,Login                                                        |
| "cleanup or login or navigation or book_appointment or reschedule_appointment"   | Cancel the existing appointments if available,Login,navigation and book myself and reschedule appointment  |
| "cleanup or login or navigation or book_appointment or cancel_appointment"       | Cancel the existing appointments if available,Login,navigation and book myself and cancel appointment      |
| "cleanup or login or navigation or book_appointment or reschedule_appointment or cancel_appointment" | Cancel the existing appointments if available,Login,navigation and book myself and cancel appointment|
| "cleanup or login or navigation_specific or add_dependent"                       | Cancel the existing appointments if available,Login,navigation,add dependent                               |
| "cleanup or login or navigation_specific or add_dependent or book_appointment"   | Cancel the existing appointments if available,Login,navigation,add dependent and book_appointment          |
| "cleanup or login or navigation_specific or edit_dependent "                     | Cancel the existing appointments if available,Login,navigation,edit dependent                              |
| "cleanup or login or navigation_specific or edit_dependent or book_appointment"  | Cancel the existing appointments if available,Login,navigation,edit dependent and book_appointment         |
| "cleanup or login or navigation or book_appointment or check_in"                 | Cancel the existing appointments if available,Login,navigation,book_appointment and check in appointment   |
| "login or review_navigation or check_in"                                         | Login,navigation to check in appointment. This option would be utilized for coordinated tests with P360 and Performance tests|
                                                                                                                                           
 ### Pytest Command to Execute the test using Markers Mechanism and Generate the Allure Reports for Registered User Flow

##### Multiple Marker Combination Command Example
    Below Command will execute the set of tests related with actions like Cancel the existing appointment if available, login, paerform page navigations, book, reschedule and cancel appointment.
    
    py.cleanup -p && py.test -v tests/registered -m "cleanup or login or navigation or book_appointment or reschedule_appointment or cancel_appointment" --platform=android --brand irvine --apptmt Medical --user mfa_disabled --provider custom --timeslot action=random --alluredir reports & allure generate reports -o final_report --clean

##### Two Marker Combination Command Example
    Below Command will execute the set of tests related with actions like Cancel the existing appointment if available and login.
    
    py.cleanup -p && py.test -v tests/registered -m "cleanup or login" --platform=android --brand irvine --apptmt Medical --user mfa_disabled --provider custom --timeslot action=random --alluredir reports & allure generate reports -o final_report --clean

##### One Marker Combination Command Example
    Below Command will execute the set of tests related with actions like Cancel the existing appointment if available.
    
    py.cleanup -p && py.test -v tests/registered -m "cleanup" --platform=android --brand irvine --apptmt Medical --user mfa_disabled --provider custom --timeslot action=random --alluredir reports & allure generate reports -o final_report --clean

##### Running all tests except the specific ones
    Below Command will execute all tests available except the cancel appointment flow
    
    py.cleanup -p && py.test -v tests/registered -m "not cancel_appointment" --platform=android --brand irvine --apptmt Medical --user mfa_disabled --provider custom --timeslot action=random --alluredir reports & allure generate reports -o final_report --clean

##### Reference materials for implementing the markers
    http://doc.pytest.org/en/latest/example/markers.html