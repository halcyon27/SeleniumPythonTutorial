from selenium import webdriver

driver_path = "this.that"
driver = webdriver.Firefox(driver_path)
driver.get("google.com")
if driver.current_url == "google":
    print('Pass')
    Else:
    Print ("Fail")
