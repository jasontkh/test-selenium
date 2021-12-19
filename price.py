from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

quotations = driver.find_elements(By.CSS_SELECTOR, ".page-product > ul > li[id]")

know_smallest_price = 999999999
know_smallest_btn = None

for quotation in quotations:
    price_elem = quotation.find_element(By.CSS_SELECTOR, ".text-price-number")
    
    price = float(price_elem.text.replace(",", "")) # 8,980
    price = float(price_elem.get_attribute("data-price")) # 8980.0

    quotation_elem = quotation.find_element(By.CSS_SELECTOR, ".new_referral_btn")
    quotation_elem = quotation.find_element(By.CSS_SELECTOR, "[title=安心訂購]")

    if price < know_smallest_price:
        
        know_smallest_price = price
        know_smallest_btn = quotation_elem
        
know_smallest_btn.click()


    


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.apple.com/hk-zh/shop/buy-iphone/iphone-13-pro")

driver.find_element(By.CSS_SELECTOR, "input[value='6_1inch']").click()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, "input[value='graphite']").click()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, "input[value='256gb']").click()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, "input[value='noTradeIn']").click()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR, ".add-to-cart > button").click()


