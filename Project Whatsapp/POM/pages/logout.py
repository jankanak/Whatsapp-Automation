from POM.pages.basePage import Base
from POM.Locators.locators import Locators
class Logout():
    def __init__(self,driver):
        self.driver=driver 
        self.logout_id =Locators.logout_id
        self.logout_click=Locators.logout_click


    def login_out_whatsapp(self):
        self.driver.find_element_by_xpath(self.logout_id).clear
        self.driver.find_element_by_xpath(self.logout_id).click()
        self.find_element_by_css_selector(self.logout_click).clear
        self.find_element_by_css_selector(self.logout_click).click()
