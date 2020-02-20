# Python-Demo-browserstack

[Python](https://www.browserstack.com/automate/python) Integration with BrowserStack

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

## Prerequisites

* [BrowserStack Automate](https://www.browserstack.com/automate) account with at least 4 parallel tests. Signup for a free trial [here](https://www.browserstack.com/users/sign_up).
<!--* [Gauge](http://getgauge.io) should be installed and in $PATH. Latest version of Gauge can be downloaded from [the website](http://getgauge.io/get-started/index.html).-->

## Setup

* Clone the repo
* Install Gauge `https://docs.gauge.org/getting_started/installing-gauge.html?os=macos&language=python&ide=vscode`
* Install dependencies `pip install -r requirements.txt`
* Update `*.json` files inside the `config/` directory with your [BrowserStack Username and Access Key](https://www.browserstack.com/accounts/settings)

## Running your tests
* To run a single test, run `paver run single`
* To run local tests, run `paver run local`
* To run parallel tests, run `paver run parallel`
## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
* You can export the environment variables for the Username and Access Key of your BrowserStack account

  ```
  export BROWSERSTACK_USERNAME=<browserstack-username> &&
  export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
  ```
  
## Additional Resources
* [Documentation for writing Automate test scripts in Python](https://www.browserstack.com/automate/python)
* [Customizing your tests on BrowserStack](https://www.browserstack.com/automate/capabilities)
* [Browsers & mobile devices for selenium testing on BrowserStack](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate)
* [Using REST API to access information about your tests via the command-line interface](https://www.browserstack.com/automate/rest-api)

