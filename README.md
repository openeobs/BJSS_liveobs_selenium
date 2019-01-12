# LiveObs Selenium
[![Build Status](https://travis-ci.org/bjss/BJSS_liveobs_selenium.svg?branch=master)](https://travis-ci.org/bjss/BJSS_liveobs_selenium) [![Documentation Status](https://readthedocs.org/projects/liveobs-selenium/badge/?version=latest)](http://liveobs-selenium.readthedocs.io/en/latest/?badge=latest) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/6e1201e1f12b41d89d8a60450434c748)](https://www.codacy.com/app/BJSS/BJSS_liveobs_selenium?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bjss/BJSS_liveobs_selenium&amp;utm_campaign=Badge_Grade)

This library contains element selectors and page object models for use in testing
the GUI of LiveObs.

[Further documentation can be found on ReadTheDocs](http://liveobs-selenium.readthedocs.io/en/latest/?)

## What this library is
A library to use with automation projects that separates the concerns of interacting with
the GUI and the automated job the implementing library is doing.

This library supports both Python 2.7 and Python 3.

## What this library isn't
This library is not a test library and does not contain any test suites, assertions or 
other code that does not deal explicitly with the GUI.

# What's in the box
We're using the page object model with Selenium so that the actions on the page and the
CSS selectors to find elements in the components on the page are separated, this allows
for easier refactoring and greater flexibility.

## Element selectors
The element selectors are grouped into the relevant component they will be found 
in. You can find a list of components used within the mobile frontend[in the Styleguide.](http://neovahealth.github.io/openeobs/)

## Page Object Models
The page object models reflect interaction with a particular page in the app 
which aligns with the product overview. Common actions are abstracted into the `common` folder.

# Development
 To ensure that the library is built to a high standard the following development 
 guidelines are in place.
 - Code must have no `flake8` or `pylint` linting errors
 - All Code must have docstrings (enforced by `pylint`) and documentation should be 
 published via [ReadTheDocs](https://readthedocs.org/)
 
 ## Opening a pull request
 When opening a pull request it's important to state what functionality has been added
 and what functionality has been removed - the `git diff` only tells us the changes not
 the context behind them.
 
 Once a pull request has been opened a code review will then be conducted which will 
 cover:
 - Timing on `Expected Conditions` such as elements becoming visible / hidden
 - Deprecation of element selectors 
 - Code re-usability
