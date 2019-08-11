from selenium.webdriver import Chrome
from BaseFiles import InitiateDriver
from Library import ConfigReader
from Pages_POM import RegistrationPage
import pytest
import openpyxl
from DataDrivenFiles import DataGenExcel

#first way of Data Driven Testing
def dataGenerator(): #Test Driven Framework
    li = [['uname1','test@1','test1'],['uname2','test@2','test2'],['uname3','test@3','test3']]
    return li

#second way to check DataGenExcel under DataDrivenFiles


@pytest.mark.parametrize('data',DataGenExcel.dataGenerator()) #whatever data coming from data generator put it in data
def test_ValidateRegistration(data):
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver) #passing driver object, because on Registration Page it was used fro constructor
    register.enter_username(data[0])
    register.enter_email(data[1])
    register.enter_password(data[2])
