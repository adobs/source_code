# todo
# rename unit test and functionaltest

"""
tests.py

Tests file.  Of note, if Google (example used in many test cases) were to change 
its page, many of the tests would fail.
"""

import unittest
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
import server
from source import convert_url_text, is_valid_url, count_tags, escape_html, source_text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(unittest.TestCase):
    """ Unit tests """

    #################### SETUP AND TEARDOWN FOR EACH TEST ######################

    def setUp(self):
        """ Setup for all test cases """

        self.client = server.app.test_client()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """ Teardown for all test cases """

        self.browser.quit()

    ########################### TESTING ROUTES #################################

    def test_home(self):
        """ Testing routes """

        result = self.client.get('/')
        self.assertIn('Enter a URL to see the source code for that website', result.data)
        self.assertEqual(result.status_code, 200)

    ##################### TESTING FUNCTIONS IN SOURCE.PY #######################

    def test_convert_url_text(self):
        """ Testing convert_url_text() function """

        self.assertIn("<head", convert_url_text("https://www.google.com"))

    def test_is_valid_url_true(self):
        """ Testing is_valid_url() function """

        self.assertEqual("True", is_valid_url("https://www.google.com"))

    def test_is_valid_url_false(self):
        """ Testing is_valid_url() function """

        self.assertEqual("False", is_valid_url("hi"))

    def test_count_tags(self):
        """ Testing count_tags() function """

        self.assertIn('u', count_tags("https://www.google.com"))

    def test_escape_html(self):
        """ Testing escape_html() function """

        self.assertEqual(escape_html("<html><head><title></title></head><body></body></html>"),
                         '&lt;html&gt;<br>&lt;head&gt;<br>&lt;title&gt;<br>&lt;/title&gt;<br>&lt;/head&gt;<br>&lt;body&gt;<br>&lt;/body&gt;<br>&lt;/html&gt;<br>')

    def test_source_text(self):
        """ Testing source_text() function """

        self.assertIsInstance(source_text("https://www.google.com"), basestring)

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
