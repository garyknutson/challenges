# Generated by Selenium IDE
from unittest import TestCase
import time
import json
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestExoticsearch(TestCase):
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_exoticsearch(self):
    self.driver.get("https://www.copart.com/")
    self.driver.set_window_size(968, 548)
    self.driver.execute_script("window.scrollTo(0,1)")
    self.driver.find_element(By.ID, "input-search").click()
    self.driver.find_element(By.ID, "input-search").send_keys("exotics")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-lightblue:nth-child(1)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").text == "PORSCHE"
  
