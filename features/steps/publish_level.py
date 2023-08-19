import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from shared_functions import *


def teardown(context):
    context.driver.get("http://localhost:8080/VALU3S/logout")
    log_admin(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/delete_confirmation")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    if text == "Do you really want to delete this folder and all its contents?":
        context.driver.find_element(By.ID, "form-buttons-Delete").click()
    context.driver.get("http://localhost:8080/VALU3S/logout")
    context.driver.get("http://localhost:8080/VALU3S")


@given(u'A content exists')
def step_impl(context):
    context.driver.set_window_size(1017, 745)
    context.driver.get("http://localhost:8080/VALU3S")
    log_admin(context)
    #context.driver.find_element(By.LINK_TEXT, "Tools").click()
    context.driver.get("http://localhost:8080/VALU3S/tools")
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    #context.driver.find_element(By.ID, "standards").click()
    context.driver.find_element(By.CSS_SELECTOR, ".contenttype-standards").click()
    context.driver.find_element(By.CSS_SELECTOR, ".context").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("testing_standard_x0000145")
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    #context.driver.find_element(By.ID, "personaltools-logout").click()
    context.driver.find_element(By.ID, "personaltoolspage-logout").click()
    context.driver.find_element(By.CSS_SELECTOR, "img").click()

@given(u'User is viewing the content')
def step_impl(context):
    context.driver.set_window_size(1280, 720)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")


@when(u'User clicks \'Send back\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks \'Send back\'')


@then(u'Content\'s state is changed to \'Private\'')
def step_impl(context):
    logout(context)
    log_admin(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "plone-toolbar-state-title").text
    assert(text == 'Private')
    logout(context)


@given(u'"reviewer" user is logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given "reviewer" user is logged in')


@given(u'Content is in the "Pending review" state')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Content is in the "Pending review" state')


@when(u'User clicks \'State: "Pending review"\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks \'State: "Pending review"\'')


@given(u'Content is in the "Published" state')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Content is in the "Published" state')


@when(u'User clicks \'State: "Published"\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks \'State: "Published"\'')


@then(u'"Reviewers" can no longer see the content')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Reviewers" can no longer see the content')


@then(u'"Consumers" can no longer see the content')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Consumers" can no longer see the content')


@given(u'Administrator is logged in')
def step_impl(context):
    original_url = context.driver.current_url
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.ID, "personaltools-login").click()
    element = context.driver.find_element(By.ID, "personaltools-login")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").click()
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()
    context.driver.get(original_url)
    

@given(u'Content is in the \'Private\' state')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "plone-toolbar-state-title").text
    assert(text == 'Private')


@when(u'Administrator clicks \'State: Private\'')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "label-state-private").click()


@when(u'Administrator clicks \'Publish\'')
def step_impl(context):
    context.driver.find_element(By.ID, "workflow-transition-publish").click()


@then(u'Content\'s state is changed to \'Published\'')
def step_impl(context):
    original_url = context.driver.current_url
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "plone-toolbar-state-title").text
    assert(text == 'Published')
    context.driver.get(original_url)


@then(u'Everyone can see the content')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then Everyone can see the content')
    context.driver.get("http://localhost:8080/VALU3S/logout")
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    assert(text == "testing_standard_x0000145")
    teardown(context)


@when(u'Administrator clicks \'Submit for publication\'')
def step_impl(context):
    context.driver.find_element(By.ID, "workflow-transition-submit").click()



@then(u'Content state is changed to \'Pending review\'')
def step_impl(context):
    original_url = context.driver.current_url
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "plone-toolbar-state-title").text
    assert(text == "Pending review")
    context.driver.get(original_url)


@then(u'Only "administrators" can see the content')
def step_impl(context):
    logout(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert(context.driver.current_url.startswith("http://localhost:8080/VALU3S/login"))
    log_admin(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    assert(text == "testing_standard_x0000145")
    teardown(context)


@then(u'Only "reviewers" can see the content')
def step_impl(context):
    logout(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert(context.driver.current_url.startswith("http://localhost:8080/VALU3S/login"))
    log_reviewer(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    assert(text == "testing_standard_x0000145")
    teardown(context)


@given(u'"Administrator" account is logged in')
def step_impl(context):
    log_admin(context)


@given(u'Content is in the \'Pending review\' state')
def step_impl(context):
    log_admin(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/content_status_modify?workflow_action=submit")
    context.driver.find_element(By.NAME, "form.button.confirm").click()
    logout(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")


@when(u'"Administrator" clicks \'State: Pending review\'')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    context.driver.find_element(By.CLASS_NAME, "label-state-pending").click()


@when(u'"Administrator" clicks \'Publish\'')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/content_status_modify?workflow_action=publish")
    context.driver.find_element(By.NAME, "form.button.confirm").click()
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")



@given(u'"Reviewer" account is logged in')
def step_impl(context):
    log_reviewer(context)

@when(u'"Reviewer" clicks \'State: Pending review\'')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    context.driver.find_element(By.CLASS_NAME, "label-state-pending").click()


@when(u'"Reviewer" clicks \'Publish\'')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/content_status_modify?workflow_action=publish")
    context.driver.find_element(By.NAME, "form.button.confirm").click()
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")


@when(u'"Administrator" clicks \'Send back\'')
def step_impl(context):
    #context.driver.find_element(By.ID, "workflow-transition-reject").click()
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/content_status_modify?workflow_action=reject")
    context.driver.find_element(By.NAME, "form.button.confirm").click()
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")


@then(u'Only Administrators can see the content')
def step_impl(context):
    logout(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    assert(context.driver.current_url.startswith("http://localhost:8080/VALU3S/login"))
    log_admin(context)
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")
    text = context.driver.find_element(By.CLASS_NAME, "documentFirstHeading").text
    assert(text == "testing_standard_x0000145")
    teardown(context)
    


@when(u'"Reviewer" clicks \'Send back\'')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145/content_status_modify?workflow_action=reject")
    context.driver.find_element(By.NAME, "form.button.confirm").click()
    context.driver.get("http://localhost:8080/VALU3S/tools/testing_standard_x0000145")


