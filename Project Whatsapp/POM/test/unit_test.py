
from POM.pages.loginPage import LoginPage
from POM.pages.message_sent import MessageSent
from POM.pages.logout import Logout
from POM.pages.message_write import MessageWrite
from POM.test.BaseTest import *

class LoginTest(BaseTest):

    def test_login_validation(self):
        driver=self.driver
        driver.get('https://web.whatsapp.com/') 
        driver.implicitly_wait(20)
        login=LoginPage(driver)
        login.login_into_whatsapp()
   

    def test_message_sent_validation(self):
        driver=self.driver
        message_sent_done=MessageSent(driver)
        message_sent_done.message()
      

    def test_message_sent_write_validation(self):
        driver=self.driver
        excel_message=MessageWrite(driver)
        excel_message.WriteMessageExcel()
        

    def test_logout_validation(self):
        driver=self.driver
        logout=Logout(driver)
        logout.login_out_whatsapp()


 


