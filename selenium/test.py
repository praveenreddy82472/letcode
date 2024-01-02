from datetime import time
import time 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://lewisu.edu/")
print(driver.title)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
'''2-Home page must include the following links:
a.About Us
b.Academics
c.Admission and Aid
d.Athletics
e.Student Life
f.Locations'''
'''driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[1]/a")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/a")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[3]/a")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[4]/a")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[5]/a")
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[6]/a")'''

about_us  = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[1]/a") #click the about_us
about_us.click()
academics  = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/a") #click the about_us
academics.send_keys(Keys.ENTER)
admission_aid  = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[3]/a") #click the about_us
admission_aid.send_keys(Keys.ENTER)
atheletics  = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[4]/a") #click the about_us
atheletics.send_keys(Keys.ENTER)
student_life  = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[5]/a") #click the about_us
student_life.send_keys(Keys.ENTER)
time.sleep(2)
location  = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[6]/a") #click the about_us
location.send_keys(Keys.ENTER)
time.sleep(3)
#----->User must be able to navigate to the Faculty/Staff directory from the homepage
#------->User must be able to search for “Omari” and get results.
time.sleep(4)
ele1 = driver.find_element(By.XPATH, "/html/body/header/div/ul[1]/div/li[3]/a") #faculty/staff
ele1.send_keys(Keys.ENTER)
time.sleep(3)
ele2=driver.find_element(By.XPATH,"/html/body/main/div[2]/div[1]/ul[3]/li[4]/a") #fac/staff directory
ele2.send_keys(Keys.ENTER)
time.sleep(3)
ele3 = driver.find_element(By.NAME,"last") #search the proffesor name
ele3.clear()
ele3.send_keys("omari")
ele3.send_keys(Keys.RETURN)
time.sleep(2)
'''ele4 = driver.find_element(By.XPATH,"/html/body/main/div/div[2]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/div/form/p/input")
time.sleep(1)
ele4.send_keys(Keys.RETURN)
actions = ActionChains(driver)
actions.context_click().perform()
time.sleep(3)'''

driver.get_screenshot_as_file('D:\Lewis\Testing & Quality\lab5\lab5.png') #screenshot of the result
#ele5 = driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[2]/td[1]/a')

#driver.get_screenshot_as_file('D:\Lewis\Testing & Quality\lab5\omari.png')
driver.close()