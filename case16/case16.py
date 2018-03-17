from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities["marionette"] = True
firefox_capabilities["binary"] = "/usr/bin/firefox"

driver = webdriver.Firefox(capabilities=firefox_capabilities,executable_path='./case16/geckodriver')
driver.get("http://www.wsb.com/Assignment2/case16/controller.php")
delay = 3

try:
  myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'msg')))
  myElem.click()
  myElem.send_keys("haha")
  btn = driver.find_element_by_id("send")
  btn.click()
  driver.close()
except TimeoutException:
  print "Loading took too much time!"

