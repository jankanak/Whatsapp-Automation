from openpyxl.workbook import workbook
from selenium import webdriver
import time 
import openpyxl
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import unittest


class BaseTest(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/automate/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()


