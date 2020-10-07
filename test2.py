from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://eportal.stust.edu.tw/")

elem_user = driver.find_element_by_name("Ecom_User_ID")
elem_user.send_keys("4a9g0065")
elem_pwd = driver.find_element_by_name("Ecom_Password")
elem_pwd.send_keys("qqq159357")
elem_pwd.send_keys(Keys.RETURN)
time.sleep(3)
