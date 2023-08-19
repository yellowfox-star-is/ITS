from selenium import webdriver
import behave
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

def before_all(context):
    context.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                      desired_capabilities=DesiredCapabilities.FIREFOX)
    context.driver.implicitly_wait(5)
    context.base_url = "http://localhost:8080/VALU3S/"


def after_all(context):
    context.driver.quit()


