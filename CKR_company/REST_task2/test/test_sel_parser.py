
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from link import *


def test_get():
    pytest.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    pytest.driver.implicitly_wait(20)  # Неявное ожидание
    wait = WebDriverWait(pytest.driver, 20)
    pytest.driver.get(FNS_RUSSIA)

    pytest.driver.find_element_by_class_name("no-data").click()

    # assert pytest.driver.find_element(By.TAG_NAME, 'span').text == "Код ИФНС"

    # Варианты тегов: CSS
    # 'input[id="txtFilter"]' 'input[class="hidden.inp-std"]'  'input#txtFilter.hidden.inp-std'
    input_region = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="txtFilter"]'))).click()
    input_region.send_keys('7840')

    pytest.driver.quit()
