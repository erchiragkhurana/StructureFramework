from selenium.webdriver import Chrome
from BaseFiles import InitiateDriver
from Library import ConfigReader

def test_ValidateRegistration():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name(ConfigReader.fetchElementLocators("Registration","username_name")).send_keys("Hello")
    driver.find_element_by_name(ConfigReader.fetchElementLocators("Registration","email_name")).send_keys("abcd")
    InitiateDriver.closeBrowser()