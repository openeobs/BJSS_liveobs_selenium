.. LiveObs Selenium documentation master file, created by
   sphinx-quickstart on Tue May 23 15:44:43 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LiveObs Selenium's documentation!
============================================

Installation
------------
To get started using the LiveObs Selenium library you first need to include it
in your project. You can do this adding the following to your
``requirements.txt``:

.. code-block:: none

    git+git://github.com/BJSS/BJSS_liveobs_selenium.git@OPTIONAL_VERSION_NUMBER

Usage
-----
Once you've got the library installed you can then import the page object
models to interact with the LiveObs GUI.

Example:

.. code-block:: python

    from liveobs_selenium.ui.page_object_models.login_page import LoginPage


    def login_into_liveobs(username, password):
        """
        Log into the LiveObs Mobile Frontend
        :param username: Username of user to log in with
        :param password: Password of the user to log in with
        """"
        login_page = LoginPage(self.client)  # self.client must be a webdriver
        login_page.login(username, password)

You shouldn't need to import the element selectors as these are intended for
use within the page object models themselves. If you do need to use the element
selectors then it's suggested that you create a pull request with the
functionality to add this back into the liveobs_selenium library.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   page_object_models



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
