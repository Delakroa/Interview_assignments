# pip install webdriver-manager
# pip install selenium
# pip install notebook
# pip install bs4
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

input_tab = driver.find_element_by_class_name("no-data").click()
# input_tab.click()

sleep(3)


button = driver.find_element_by_class_name('btn-node')
# button.send_key('7840')
button.click()


# Class name (Имя класса)
# CSS Selector
# ID
# Link text (текст ссылки)
# Name (имя)
# Partial link text (частичный текст ссылки)
# Tag name (название тэга)
# XPath


