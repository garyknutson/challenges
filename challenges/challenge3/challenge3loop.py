import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class Challenge3(unittest.TestCase):
  def setUp(self):
          self.driver = webdriver.Chrome("../chromedriver.exe")

  def tearDown(self):
         self.driver.close()

  def test_challenge3loop(self):
          self.driver.get("https://www.copart.com")
          time.sleep(5)
          myElements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
          #myElements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")

          for item in myElements:
                print(item.text + "-" + item.get_property("href"))
          #print(myElement.text)
          #print(myElement.get_property("href"))
          #self.driver.find_element(By.ID, "input-search").send_keys("exotics")
          #self.driver.find_element(By.CSS_SELECTOR, ".btn-lightblue").click()
          #time.sleep(5)
          #assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").text == "PORSCHE"
          print("test finished")
if __name__ == '__main__':
    unittest.main()
