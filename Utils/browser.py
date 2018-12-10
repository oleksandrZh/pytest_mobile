from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging

class Browser(object):

    def __init__(self, driver):
        self.driver = driver
        logging.info("create new driver")
        self.wait = WebDriverWait(self.driver, 30)
        logging.info("create new wait")

    def tap_button(self, selector):
        self.wait_element(selector)
        logging.info(str(selector) + " are waiting ")
        element = self.driver.find_element(By.XPATH, selector)
        self.wait_element(selector)
        logging.info("tap " + str(selector))
        element.click()

    def get_text(self, selector):
        self.wait_element(selector)
        element = self.driver.find_element(By.XPATH, selector)
        return element.text

    def wait_element(self, selector):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, selector)))
