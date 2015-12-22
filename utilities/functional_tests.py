"""
functional_tests.py

Tests file.  Of note, if Google were to change its page, a test would fail.
"""

import unittest
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(unittest.TestCase):
    """ Unit tests """

    #################### SETUP AND TEARDOWN FOR EACH TEST ######################

    def setUp(self):
        """ Setup for all test cases """

        self.browser = webdriver.Firefox()

    def tearDown(self):
        """ Teardown for all test cases """

        self.browser.quit()

    ###################### TESTING JAVASCRIPT USING SELENIUM ###################

    def test_title(self):
        """ Testing title """

        self.browser.get('http://textsource.herokuapp.com')
        self.assertEqual(self.browser.title, 'Text Source')

    def test_search(self):
        """ Testing search box with valid URL """

        self.browser.get('http://textsource.herokuapp.com')

        self.browser.execute_script("document.querySelector('#source').value = 'https://www.google.com';")

        self.browser.find_element_by_id("submit-btn").click()

        wait = WebDriverWait(self.browser, 10)
        tag_count_header = wait.until(EC.element_to_be_clickable((By.ID, 'tag-count-header')))

        self.assertEqual(tag_count_header.text, "TAG COUNT")


if __name__ == '__main__':
    unittest.main()
