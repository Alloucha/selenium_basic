# Import WD lib


# Create WD Chrome Object


# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"

# Click on [Normal success message button]

# assert appeared green success message

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")

driver.find_element_by_id('normal-btn-success').click()

assert "I'm a normal success message." in driver.page_source
driver.quit()
