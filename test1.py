from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://eportal.stust.edu.tw/')
time.sleep(3)

context = driver.find_element_by_css_selector('#password')
context.send_keys("qqq159357")
time.sleep(1)

commit = driver.find_element_by_css_selector('#loginButton2')
commit.click()
time.sleep(5)
