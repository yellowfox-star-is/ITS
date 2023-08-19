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


def create_content(context):
    original_url = context.driver.current_url
    context.driver.get("http://localhost:8080/VALU3S/tools")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    context.driver.find_element(By.CSS_SELECTOR, ".context").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("testing_standard_x0000145")
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.get(original_url)



def teardown(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/delete_confirmation")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    if text == "Do you really want to delete this folder and all its contents?":
        context.driver.find_element(By.ID, "form-buttons-Delete").click()
    context.driver.get("http://localhost:8080/VALU3S/logout")


@given(u'An account with administrator privileges is logged in')
def step_impl(context):
    log_admin(context)


@given(u'Parent content exists')
def step_impl(context):
    original_url = context.driver.current_url
    context.driver.get("http://localhost:8080/VALU3S/tools")
    assert(context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text == "Tools")
    context.driver.get(original_url)
    


@given(u'User creates a new content')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    context.driver.find_element(By.CSS_SELECTOR, ".context").click()


@when(u'User fills all required inputs')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("testing_standard_x0000145")


@when(u'User clicks \'Save\'')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'New content is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert(context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text == "testing_standard_x0000145")


@then(u'Content is in the state \'Private\'')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert(context.driver.find_element(By.CLASS_NAME, "plone-toolbar-state-title").text == 'Private')


@then(u'Content is in a parent content (content viewed at the time of creation)')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools")
    context.driver.find_element(By.LINK_TEXT, "testing_standard_x0000145").click()
    context.driver.get("http://localhost:8080/VALU3S/tools")
    teardown(context)


@given(u'Content edit is open')
def step_impl(context):
    create_content(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/edit")


@when(u'User changes input fields')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("1")


@then(u'Changed properties are changed')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert("testing_standard_x00001451" in context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text)


@then(u'Changes are visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/delete_confirmation")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    if text == "Do you really want to delete this folder and all its contents?":
        context.driver.find_element(By.ID, "form-buttons-Delete").click()
    context.driver.get("http://localhost:8080/VALU3S/logout")


@given(u'Content was cut')
def step_impl(context):
    create_content(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-actions-cut").click()


@given(u'Another content is viewed')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases")


@when(u'User pastes')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-actions-paste").click()
    time.sleep(1)


@then(u'Content\'s parent content is changed')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases/testing_standard_x0000145")
    assert(context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text == "testing_standard_x0000145")
    context.driver.get("http://localhost:8080/VALU3S/use-cases/testing_standard_x0000145/delete_confirmation")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    if text == "Do you really want to delete this folder and all its contents?":
        context.driver.find_element(By.ID, "form-buttons-Delete").click()
    context.driver.get("http://localhost:8080/VALU3S/logout")


@given(u'Content was copied')
def step_impl(context):
    create_content(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions .plone-toolbar-title").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-actions-copy").click()
    time.sleep(1)


@then(u'Copy of copied contend is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases/testing_standard_x0000145")
    assert(context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text == "testing_standard_x0000145")


@then(u'New content\'s parent is viewed content')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases/testing_standard_x0000145")
    assert(context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text == "testing_standard_x0000145")


@then(u'New content\'s state is \'Private\'')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "plone-toolbar-state-title").text
    assert(text == 'Private')
    context.driver.get("http://localhost:8080/VALU3S/use-cases/testing_standard_x0000145/delete_confirmation")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    if text == "Do you really want to delete this folder and all its contents?":
        context.driver.find_element(By.ID, "form-buttons-Delete").click()
    teardown(context)


@given(u'Content exists')
def step_impl(context):
    create_content(context)


@given(u'Content is being viewed')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-case/s/testing_standard_x0000145")


@given(u'Deletion of the content is allowed')
def step_impl(context):
    pass


@when(u'User deletes content')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/delete_confirmation")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    if text == "Do you really want to delete this folder and all its contents?":
        context.driver.find_element(By.ID, "form-buttons-Delete").click()


@then(u'Content is deleted')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert(context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text == "This page does not seem to exist…")


@then(u'Content cannot be found anywhere')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert(context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text == "This page does not seem to exist…")
    logout(context)
