from pageobjects.Homepage import HomePage
from pageobjects.AccountRegPage import AccountRegPage
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountReg:
    #baseURL = "https://demo.opencart.com/"
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    def test_account_reg(self,setup):
        self.logger.info("**** test_001_AccountRegistration started *** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage=AccountRegPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email=randomString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)

        self.regpage.setPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        self.driver.close()
        if self.confmsg=="Your Account Has Been Created!":
            assert True
        else:
            assert False
