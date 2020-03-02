# Python-Demo-browserstack

[Python](https://www.browserstack.com/automate/python) Integration with BrowserStack

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

## Prerequisites

* [Brew](https://docs.brew.sh/Installation) (Optional)
* Python3 (Installation notes [here](https://gist.github.com/RathilVasani/0ab70692688b3632d447ced5c277a9be))
* [BrowserStack Automate](https://www.browserstack.com/automate) account with at least 4 parallel tests. Signup for a free trial [here](https://www.browserstack.com/users/sign_up).

## Setup

* Clone the repo
* Install dependencies `pip install -r requirements.txt`
* Export the environment variables for the Username and Access Key of your BrowserStack account

  ```
  export BROWSERSTACK_USERNAME=<browserstack-username> &&
  export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
  ```
## Running your tests
* To run a single test, run `python3 single.py`
* To run local tests, run `python3 local.py`
* To run parallel tests, run `python3 parallel.py`
* To run Appium tests for IOS, run `python3 ios-appium.py`
* To run Appium tests for Android, run `python3 android-appium.py`
* To run Espresso tests,run `python3 espresso.py`
* To run XcuiTest tests,run `python3 xcuittest.py`
* To run Earlgrey tests,run `python3 earlgrey.py`

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)

## Additional Resources
* [Documentation for writing Automate test scripts in Python](https://www.browserstack.com/automate/python)
* [Customizing your tests on BrowserStack](https://www.browserstack.com/automate/capabilities)
* [Browsers & mobile devices for selenium testing on BrowserStack](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate)
* [Using REST API to access information about your tests via the command-line interface](https://www.browserstack.com/automate/rest-api)

