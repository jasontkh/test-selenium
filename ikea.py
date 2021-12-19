from flask import Flask
from flask import send_file
app = Flask(__name__)


@app.route("/")
def hello_world():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.ikea.com.hk/zh")

    elem = driver.find_element(By.CSS_SELECTOR, "#header_searcher_desktop_input")
    elem.clear()
    elem.send_keys("chair")
    elem.send_keys(Keys.RETURN)
    all_products = []
    while True:

        product_brief_list = driver.find_element(By.CSS_SELECTOR, ".products_list.w-100.d-flex.flex-wrap")
        for product_brief in product_brief_list.find_elements(By.CSS_SELECTOR,
                                                              ".col-6.col-md-4.col-lg-3.p-0.itemBlock"):
            title = product_brief.find_element(By.CSS_SELECTOR, ".itemName").text
            detail = product_brief.find_element(By.CSS_SELECTOR, ".itemFacts").text
            price = product_brief.find_element(By.CSS_SELECTOR, ".itemPrice-wrapper").text
            rate = product_brief.find_element(By.CSS_SELECTOR, ".plp-rating").text
            all_products.append([title, detail, price, rate])
        print(all_products)

        if len(driver.find_elements(By.CSS_SELECTOR, ".page-item.next ")) > 0:
            driver.find_element(By.CSS_SELECTOR, ".page-item.next ").click()
        else:
            break

    driver.close()

    import pandas as pd
    df = pd.DataFrame(all_products)
    df.to_csv("IKEA.csv", index=False)   # <<<<<<<< add index=False to avoid writing a column of index to csv
    return send_file("IKEA.csv", as_attachment=True)
