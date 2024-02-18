from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

class HomePage():
    myaccount_xpath = "//span[normalize-space()='My Account']"
    register_linktext = "Register"
    login_linktext = "Login"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def clickMyAccount(self):
        wait = WebDriverWait(self.driver, 30, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                               ElementNotVisibleException,
                                                                               ElementNotSelectableException,
                                                                               Exception])
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.myaccount_xpath)))
        self.driver.find_element(By.XPATH, self.myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.login_linktext).click()
