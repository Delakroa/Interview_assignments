# pip install webdriver-manager
# pip install seline
# pip install notebook
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
url = 'https://service.nalog.ru/addrno.do'
driver.get(url)
sleep(3)
input_tab = driver.find_element_by_class_name("no-data")
input_tab.click()
sleep(3)
button = ('#txtFilter')
print(button.text)
button.send_keys('7840')
