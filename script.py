from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser =  webdriver.Remote(
   command_executor="http://127.0.0.1:4444/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
        })

browser.get("https://www.wikipedia.org/")

try:
    elem = browser.find_element(By.ID, 'searchInput')
    elem.send_keys('World War I')
    elem.send_keys(Keys.RETURN)
    result = browser.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[2]')
    assert result.text == '"World  War One", "Great War", and "WWI" redirect here. For other uses, see World War One (disambiguation), Great War (disambiguation), and WWI (disambiguation).', "Header page not found "
except AssertionError as error:
    print(f"Something went wrong : {error}")
finally:
    browser.quit()
