import time
from datetime import date
from selenium import webdriver

today_day = date.today().day
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pick_products(sum_product,id_product):
    driver = webdriver.Chrome('/home/luch/PycharmProjects/test_walmart/walmart/chromedriver')
    driver.maximize_window()
    driver.get('https://www.walmart.com/')
    driver.implicitly_wait(10)
    driver.get('https://www.walmart.com/cart')
    try:
        driver.find_element_by_xpath('//div[contains(text(),‘Remove’) ]').click()
    except:
        pass
    driver.implicitly_wait(10)
    driver.get('https://www.walmart.com/ip/' + id_product)
    driver.implicitly_wait(10)

    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '// *[@availabilitystatus = "AVAILABLE"]'))
        )
        product_type = driver.find_elements_by_xpath('// *[@availabilitystatus = "AVAILABLE"]')
        product_type[0].click()
    except:
        pass

    time.sleep(3)
    driver.implicitly_wait(10)
    c = driver.find_elements_by_xpath('//*[@class="prod-ProductCTA primaryProductCTA-marker"]//select[@class="field-input field-input--secondary"]/option')
    c[sum_product-1].click()

    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@class="spin-button-children"]').click()
    driver.implicitly_wait(10)






