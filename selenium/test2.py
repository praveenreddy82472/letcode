from selenium import webdriver

driver = webdriver.Firefox()

driver.get('"https://lewisu.edu/"')
print(driver.title)
driver.close()