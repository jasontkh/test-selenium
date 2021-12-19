from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.select import Select
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options, executable_path=os.getcwd() + "/chromedriver")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0'})
print(driver.execute_script("return navigator.userAgent;"))
driver.get("https://premier.hkticketing.com/shows/show.aspx?sh=DISNE0122")

time.sleep(2.1)
the_dropdown = driver.find_element_by_css_selector('#p')
the_dropdown.click()

time.sleep(2.1)
the_option = driver.find_element_by_css_selector('option[value=EKSH2022601M]')
the_option.click()

time.sleep(1.1)
the_buy_button = driver.find_element_by_id("buyButton")
the_buy_button.click()

time.sleep(3.1)
the_seat_option = driver.find_element_by_css_selector("[data-ng-click='selectSeatArea(seatArea)']")
the_seat_option.click()

time.sleep(0.91)
the_quantity_selector = driver.find_element_by_css_selector("select[aria-label=Quantity]")
the_quantity_selector.click()

time.sleep(1.3)
the_quantity_option = driver.find_element_by_css_selector("select[aria-label='Quantity'] > option[value='1']")
the_quantity_option.click()

time.sleep(0.5)
the_deliver_selector = driver.find_element_by_css_selector("#selectDeliveryType")
the_deliver_selector.click()
time.sleep(1.3)
the_quantity_option = driver.find_element_by_css_selector("#selectDeliveryType > option[value='1']")
the_quantity_option.click()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1.3)
the_next = driver.find_element_by_css_selector("#continueBar > .chooseTicketsOfferDiv")
the_next.click()

time.sleep(4)
the_gotopayment = driver.find_element_by_css_selector("#continueBar > .chooseTicketsOfferDiv")
the_gotopayment.click()

driver.close()