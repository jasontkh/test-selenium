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

driver.get("https://www.hktvmall.com/")

elem = driver.find_element(By.CSS_SELECTOR, '.SuggestionSearch-input')

elem.send_keys("魚")
elem.send_keys(Keys.ENTER)

import time
time.sleep(5)


all_products = []

while True:
    product_brief_list = driver.find_element(By.CSS_SELECTOR, '.product-brief-list')

    for product_brief in product_brief_list.find_elements(By.CSS_SELECTOR, '.product-brief-wrapper'):
        title = product_brief.find_element(By.CSS_SELECTOR, '.brand-product-name>h4').text
        price = product_brief.find_element(By.CSS_SELECTOR, '.price').text
        image_url = product_brief.find_element(By.CSS_SELECTOR, '.square-wrapper img').get_attribute("src")

        # TODO : download
        # download(url, destination)


        all_products.append([title, price])

    next_btn = driver.find_element(By.CSS_SELECTOR, "#paginationMenu_nextBtn")

    if next_btn.get_attribute("class") == "disabled":
        break

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    next_btn.click()

    time.sleep(5)

print("done")


driver.back()

thumbnail