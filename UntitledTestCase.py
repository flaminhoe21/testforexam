# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://dec.vumk.eu/student/web/site/login")
        driver.find_element_by_id("UserLoginForm_username").click()
        driver.find_element_by_id("UserLoginForm_username").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=UserLoginForm_username | ]]
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("1814093")
        driver.find_element_by_id("UserLoginForm_password").click()
        print(driver.current_url)
        self.assertIn("dec.vumk.eu", driver.current_url)
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("210199")
        driver.find_element_by_id("login-content-button").click()
        driver.find_element_by_link_text("Forum").click()
    

    
    def tearDown(self):
        #-self.driver.quit()
        pass

if __name__ == "__main__":
    unittest.main()
