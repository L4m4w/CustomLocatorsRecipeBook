from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from wait import WebDriverWait

class config:
    driver: WebDriver = ...
    timeout: int = 4


def wait():
    return WebDriverWait(driver=config.driver, timeout=config.timeout, ignored_exceptions=(WebDriverException,))

class Element:
    def __init__(self, selector):
        self.selector = selector
    def should_be_blank(self) -> 'Element':
        wait().until(element_value_is_empty(self.selector))
        return self

    def set_value(self, text) -> 'Element':
        def command(driver):
            config.driver.find_element(By.CSS_SELECTOR, self.selector).clear()
            config.driver.find_element(By.CSS_SELECTOR, self.selector).send_keys(text)
            return True
        wait().until(command)

        return self

    def press_enter(self) -> 'Element':
        def command(driver):
            config.driver.find_element(By.CSS_SELECTOR, self.selector).send_keys(Keys.ENTER)
            return True

        wait().until(command)
        return self

    def click(self)-> 'Element':
        def command(driver):
            config.driver.find_element(By.CSS_SELECTOR, self.selector).click()
            return True

        wait().until(command)
        return self

    def element(self, selector: str)->'Element':
        return Element(self.selector + ' ' + selector)


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
    config.driver.get(url)