from POM.Locators.locators import *
from POM.pages.basePage import Base
class MessageWrite():
    def __init__(self,driver):
        self.driver=driver

    def WriteMessageExcel(self):
        b =openpyxl.load_workbook("C:/Users/SunMoon Computer/Desktop/automate/book1.xlsx")   
        sht = b.active
        sht.cell(row=2,column=2).value="Messagesent"
        b.save(filename="C:/Users/SunMoon Computer/Desktop/automate/book1.xlsx")
