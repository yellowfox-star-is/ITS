import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def log_admin(context):
    original_url = context.driver.current_url
    context.driver.get("http://localhost:8080/VALU3S")
    time.sleep(0.2)
    context.driver.find_element(By.ID, "personaltools-login").click()
    time.sleep(0.2)
    element = context.driver.find_element(By.ID, "personaltools-login")
    time.sleep(0.2)
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    context.driver.find_element(By.ID, "__ac_name").click()
    time.sleep(0.2)
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    time.sleep(0.2)
    context.driver.find_element(By.ID, "__ac_password").click()
    time.sleep(0.2)
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    time.sleep(0.2)
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
    context.driver.get(original_url)


def log_reviewer(context):
    original_url = context.driver.current_url
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.ID, "personaltools-login").click()
    element = context.driver.find_element(By.ID, "personaltools-login")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsreviewer")
    context.driver.find_element(By.ID, "__ac_password").click()
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsreviewer")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
    context.driver.get(original_url)


def logout(context):
    context.driver.get("http://localhost:8080/VALU3S/logout")
