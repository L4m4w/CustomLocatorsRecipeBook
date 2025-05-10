from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

driver.get('https://google.com')

assert driver.find_element(By.CSS_SELECTOR, '[name=q]').get_attribute('value') == ''

class element_value_is_empty(object):
    def __init__(self, selector):
        self.selector = selector


    def __call__(self, driver):
        return driver.find_element(By.CSS_SELECTOR, self.selector).get_attribute('value') == ''

wait = WebDriverWait(driver= driver, timeout=4)
wait.until(element_value_is_empty('[name=q]'))

driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('google')
driver.find_element(By.CSS_SELECTOR, '[name=q]').clear()
# driver.
# driver.get()