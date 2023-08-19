import sys
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

from shared_functions import *


def teardown(context):
    context.driver.get("http://localhost:8080/VALU3S/logout")
    log_admin(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/delete_confirmation")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    if text == "Do you really want to delete this folder and all its contents?":
        context.driver.find_element(By.ID, "form-buttons-Delete").click()
    context.driver.get("http://localhost:8080/VALU3S/logout")
    logout(context)
    context.driver.get("http://localhost:8080/VALU3S")


@given(u'Administrator account exists')
def step_impl(context):
    context.driver.set_window_size(1280, 720)
    context.driver.get("http://localhost:8080/VALU3S")


@given(u'Administrator account is logged in')
def step_impl(context):
    logout(context)
    log_admin(context)


@given(u'Content is being edited')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    context.driver.find_element(By.CSS_SELECTOR, ".context").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("testing_standard_x0000145")
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.get("http://localhost:8080/VALU3S/tools/testos-combine/edit")


@given(u'Content was added in relations')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()
    #context.driver.find_element(By.CLASS_NAME, "select2-search-field").click()
    #context.driver.find_element(By.CSS_SELECTOR, "#s2id_autogen13 > ul:nth-child(1) > li:nth-child(1)").click()
    #formfield-form-widgets-standards > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3) > span:nth-child(1) > a:nth-child(1)
    context.driver.find_element(By.CSS_SELECTOR, "#formfield-form-widgets-standards .path-wrapper > .separator > span > .crumb").click()
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    #context.driver.find_element().click()


@when(u'User saves')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'Relations are saved')
def step_impl(context):
    text = context.driver.find_element(By.CSS_SELECTOR, ".portalMessage").text
    assert("Changes saved" in text)


@then(u'Links to related content are shown in the Method')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testos-combine")
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    print(text, file=sys.stderr)
    assert(text == "testing_standard_x0000145")
    teardown(context)


@given(u'Relations to other content exists')
def step_impl(context):
    original_url = context.driver.current_url
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()
    context.driver.find_element(By.CSS_SELECTOR, "#formfield-form-widgets-standards .path-wrapper > .separator > span > .crumb").click()
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.get(original_url)
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()


@given(u'Relation to other content is removed')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()
    context.driver.find_element(By.CSS_SELECTOR, "#s2id_autogen13 .select2-search-choice-close").click()

@then(u'Relation to other content is removed')
def step_impl(context):
    text = context.driver.find_element(By.CSS_SELECTOR, ".portalMessage").text
    assert("Changes saved" in text)


@then(u'Links to related content is no longer shown in edited Content')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testos-combine")
    removed = False
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    except NoSuchElementException:
        removed = True
    assert(removed)
    teardown(context)
