from POM.pages.basePage import Base
from POM.Locators.locators import Locators
class LoginPage():
    def __init__(self,driver):
        self.driver=driver 
        self.search_number_id =Locators.search_number_id

    def login_into_whatsapp(self):
        b =openpyxl.load_workbook("C:/Users/SunMoon Computer/Desktop/automate/book1.xlsx")                                    #get active sheet
        sht = b.active  
        cl = sht.cell(row = 2, column = 1).value 
        self.driver.find_element_by_xpath(self.search_number_id).clear
        self.driver.find_element_by_xpath(self.search_number_id).send_keys(cl)
        self.search.send_keys(Keys.RETURN)
