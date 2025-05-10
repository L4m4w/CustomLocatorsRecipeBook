from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import selenide as browser

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install())
browser.config.driver = webdriver.Chrome()
browser.config.timeout = 2

# oop version of config
# browser = Browser(driver = webdriver.Chrome(), timeout = 2)

query = browser.element('[name=q]')

# browser.driver.get('https://google.com')
browser.visit('https://google.com')

# assert driver.find_element(By.CSS_SELECTOR, '[name=q]').get_attribute('value') == ''

# wait = WebDriverWait(driver= driver, timeout=4)
# wait.until(element_value_is_empty('[name=q]'))
# wait.until(element_value_is_empty('[name=q]'))
# wait.until(lambda webdriver: webdriver.find_element(By.CSS_SELECTOR, '[name=q]').get_attribute('value') == '')

# recaptcha-checkbox-borderAnimation
# LC20lb MBeuO DKV0Md
query.should_be_blank()
query.set_value('google').press_enter()
# browser.Element('#rso g a').click()
browser.element('LC20lb MBeuO').element('DKV0Md').click()
