from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

driver: WebDriver = ...

def wait():
    return WebDriverWait(driver=driver, timeout=4)

class Element:
    def __init__(self, selector):
        self.selector = selector
    def should_be_blank(self):
        wait().until(element_value_is_empty(self.selector))


class element_value_is_empty(object):
    def __init__(self, selector):
        self.selector = selector
    def __call__(self, driver):
        return driver.find_element(By.CSS_SELECTOR, self.selector).get_attribute('value') == ''

# def element_value_is_empty(selector):
#     def call(webdriver):
#         return webdriver.find_element(By.CSS_SELECTOR, selector).get_attribute('value') == ''
#     return call
def visit(url):
    driver.get(url)