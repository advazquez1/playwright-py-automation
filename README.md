# playwright-py-automation
## Overview

This project is a POC which showcases the use of Python 3+, playwright, and pytest in a test automation context.
The primary methodology which will be used for this project is the Page Object Model (POM), a design pattern that enhances test script maintainability and re-usabilty.

For this project, we'll be using a tester friendly automation web application as our demo
https://automationintesting.online/


## Tech Stack

| Tool           | Description                                                          |
|----------------|----------------------------------------------------------------------|
| playwright     | An automation library for testing web applications with a single API |
| pytest         | Testing framework for Python                                         |
| requests       | Python Library for making HTTP requests                              |
| allure         | Reporting tool that generates detailed test reports                  |
| GitHub Actions | A CI/CD tool integrated into GitHub                                  |

## Getting Started

1. Clone the repository to your local machine
2. Install the required Python packages

```pip install -r requirements.txt```

## Executing Tests

To run the demo scripts using pytest, we can use the following commands

```pytest --alluredir allure-results -s --headed --slowmo -k test_admin_logout```

```pytest --alluredir allure-results -m sanity```

To view results using Allure

```allure serve .\allure-results\```

## What the Demo Does

The purpose of the project is to demonstrate a variety of different test cases using the Restful Booker Platform web application.
In this demo, we'll perform the following.

1. Navigates through a couple web pages
2. Verifies page title and fields
3. Clicks on different links
4. Fills out and submits forms
5. Verifies a couple of negative test cases
6. Demonstrates a combination of REST API and UI within a script

Also want to note that by adopting the POM design pattern, we made our automation more robust, scalable, and maintainable.
It simplifies and enhances the readability of our test scripts.

## Standards and Best Practices

The following respect title case convention
- Directory names inside the `tests` and `src` folders

The following respect snake case convention
- Test files
- Page object files
- Test scripts and test functions
- Page object methods