from datetime import date
from selenium import webdriver

today_day = date.today().day


def pick_products(ss,aa):
    driver = webdriver.Chrome('/home/luch/PycharmProjects/test_walmart/walmart/chromedriver')
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('https://www.walmart.com/')
    driver.implicitly_wait(10)
    driver.get('https://www.walmart.com/ip/' + aa)
    driver.implicitly_wait(10)
    c = driver.find_elements_by_xpath('//*[@class="prod-ProductCTA primaryProductCTA-marker"]//select[@class="field-input field-input--secondary"]/option')
    c[ss-1].click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@class="spin-button-children"]').click()
    driver.implicitly_wait(10)

    driver.get('https://www.walmart.com/cart')
    try:
        driver.find_element_by_xpath('//div[contains(text(),‘Remove’) ]').click()
    except:
        pass



