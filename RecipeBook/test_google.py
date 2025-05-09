from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

driver.get('https://google.com')
# driver.
# driver.get()