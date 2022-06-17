# pip install webdriver-manager
# pip install selenium
# pip install notebook
# pip install bs4
from selenium import webdriver
from test.link import *

def test_get():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    driver.implicitly_wait(10)  # Неявное ожидание

    driver.get('https://service.nalog.ru/addrno.do')

    input_tab = driver.find_element_by_class_name("no-data").click()
    # input_tab.click()


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
