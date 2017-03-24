# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("F:\soft\chromedriver.exe")

    def tearDown(self):
        self.driver.quit()
    def test_can_start_list_and_retrieve_it_later(self):
        self.driver.get('http://localhost:8000')
        self.assertIn( 'To-Do', self.driver.title)
        self.fail('Finish the test!')
if __name__=='__main__':
    unittest.main(warnings='ignore')