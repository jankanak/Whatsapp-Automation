from POM.pages.basePage import Base
from POM.Locators.locators import Locators
class MessageSent():
    def __init__(self,driver):
        self.driver=driver 
        self.message =Locators.message

    def message(self):
        self.driver.find_element_by_xpath(self.message).clear
        self.driver.find_element_by_xpath(self.message).send_keys("HI")
        self.search.send_keys(Keys.RETURN)
