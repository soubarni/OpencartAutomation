import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    serv_obj = Service()
    driver = webdriver.Chrome(service=serv_obj)
    return driver

    #driver = webdriver.Chrome(ChromeDriverManager().install())
