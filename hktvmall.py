from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, executable_path=os.getcwd() + "/chromedriver")
driver.get("https://www.hktvmall.com/")

driver.find_element_by_css_selector(".SuggestionSearch-input").send_keys("牛扒")
driver.find_element_by_css_selector(".SuggestionSearch-input").send_keys(Keys.RETURN)

wrapper = driver.find_element_by_css_selector(".product-brief-list")
for product_brief in wrapper.find_elements_by_css_selector(".product-brief-wrapper"):
    print(product_brief.find_element_by_css_selector(".brand-product-name>h4").text)

driver.close()