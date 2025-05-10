from typing import Callable

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from wait import WebDriverWait

class config:
    driver: WebDriver = ...
    timeout: int = 4


def wait():
    return WebDriverWait(driver=config.driver, timeout=config.timeout, ignored_exceptions=(WebDriverException,))

class Element:
    def __init__(self, locate: Callable[[], WebElement]):
        self.locate = locate

    def should_be_blank(self) -> 'Element':
        wait().until(element_value_is_empty(self.locate))
        return self

    def set_value(self, text) -> 'Element':
        def command(driver):
            webelement = self.locate()
            webelement.clear()
            # config.driver.find_element(By.CSS_SELECTOR, self.locate).clear()
            webelement.send_keys(text)
            # config.driver.find_element(By.CSS_SELECTOR, self.locate).send_keys(text)
            return True
        wait().until(command)

        return self

    def press_enter(self) -> 'Element':
        def command(driver):
            webelement = self.locate()
            webelement.send_keys(Keys.ENTER)
            # config.driver.find_element(By.CSS_SELECTOR, self.locate).send_keys(Keys.ENTER)
            return True

        wait().until(command)
        return self

    def click(self)-> 'Element':
        def command(driver):
            webelement = self.locate()
            webelement.click()
            # config.driver.find_element(By.CSS_SELECTOR, self.locate).click()
            return True

        wait().until(command)
        return self

    def element(self, selector: str)->'Element':
        def locate():
            original = self.locate()
            try:
                webelement = original.find_element(By.CSS_SELECTOR, selector)
                return webelement
            except Exception as e:
                outer_html = original.get_attribute('outerHTML')
                raise WebDriverException(msg=f'fail to find inside {outer_html} element by {selector}')
        return Element(locate)


class element_value_is_empty(object):
    def __init__(self, locate: Callable[[], WebElement]):
        self.locate = locate
    def __call__(self, driver):
        return self.locate().get_attribute('value') == ''

# def element_value_is_empty(selector):
#     def call(webdriver):
#         return webdriver.find_element(By.CSS_SELECTOR, selector).get_attribute('value') == ''
#     return call
def visit(url):
    config.driver.get(url)


def element(selector: str):
    return Element(lambda : config.driver.find_element(By.CSS_SELECTOR, selector))