from openpyxl.workbook import workbook
from selenium import webdriver
import time 
import openpyxl
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

class Base(object):
    def __init__(self, driver,base_url):
        driver=self.driver
        driver.webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/automate/chromedriver.exe")
        base_url=driver.get('https://web.whatsapp.com/')
        self.timeout = 30
