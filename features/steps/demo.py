from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")

expected_result = '''"World  War One", "Great War", and "WWI" redirect here. 
For other uses, see World War One (disambiguation), Great War (
disambiguation), and WWI (disambiguation).', "Header page not found "
'''

test_data = {
        "url1": "https://www.wikipedia.org/",
        "url2": "https://en.www.wikipedia.org/",
        "search_field": 'searchInput',
        "expected_data": expected_result

}


@given("(?P<url>.+) name")
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    # res_url = test_data[url]
    driver = context.browser

    context.driver = driver.get(url)


@when("Find (?P<element>.+) on page")
def step_impl(context, element):
    """
    :type context: behave.runner.Context
    :type element: str
    """
    element = context.driver.find_element(By.ID, element)


@step("Fill (?P<data>.+) in element")
def step_impl(context, data):
    """
    :type context: behave.runner.Context
    :type data: str
    """
    raise NotImplementedError(u'STEP: And  Fill <data> in element')


@step("Press button on (?P<element>.+)")
def step_impl(context, element):
    """
    :type context: behave.runner.Context
    :type element: str
    """
    raise NotImplementedError(u'STEP: And  Press button on <element>')


@then("Check that element Equal to (?P<something>.+)")
def step_impl(context, something):
    """
    :type context: behave.runner.Context
    :type something: str
    """
    raise NotImplementedError(
            u'STEP: Then Check that element Equal to <something>')
