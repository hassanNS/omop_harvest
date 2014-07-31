from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class VerifyCanChangeColumns(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_verify_can_change_columns(self):
        driver = self.driver
        driver.get(self.base_url + "/login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("user002")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("test")
        driver.find_element_by_css_selector("button.btn-info.btn").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.info-region"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//button[2]").click()
        driver.find_element_by_xpath("//div[@id='content']/div[8]/div/div/div/button").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div/button").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div[3]/button[2]").click()
        driver.find_element_by_xpath("//div[@id='content']/div[8]/div/div/div/button").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_css_selector("li > button.btn.btn-mini").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/ul/li[2]/button").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/ul/li[3]/button").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div[3]/button[2]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "tbody"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text("user002").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
