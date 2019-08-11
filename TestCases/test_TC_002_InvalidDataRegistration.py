from selenium.webdriver import Chrome
from BaseFiles import InitiateDriver
from Library import ConfigReader

def test_registration_invalid_data():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name(ConfigReader.fetchElementLocators("Registration", "password_name")).send_keys("Hello")