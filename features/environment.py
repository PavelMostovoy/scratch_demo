from selenium import webdriver


def before_scenario(context, scenario):
    browser = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities={
                    "browserName": "chrome",
            })
    context.browser = browser


def after_scenario(context, scenario):
    browser = context.browser
    browser.quit()
