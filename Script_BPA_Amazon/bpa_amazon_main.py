from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter

driver_path = "C:\\Users\willi\\Projeto Python\\Script_BPA_Amazon\\Chrome_Driver\\chromedriver.exe"

driver = webdriver.Chrome(driver_path)
driver.get('https://www.amazon.com.br/')

search_box = driver.find_element_by_id('twotabsearchtextbox').send_keys("iphone")

search_button = driver.find_element_by_id("nav-search-submit-text").click()

driver.implicitly_wait(5)

soup = BeautifulSoup(driver.page_source, "lxml")

driver.implicitly_wait(5)

products = soup.find_all('div', {'data-asin': True, 'data-component-type': 's-search-result'})

driver.implicitly_wait(5)

list_products = []
list_prices = []

for product in products:
    product_name = product.h2.text
    try:
        product_price_whole = product.find('span', class_= 'a-price-whole').text
        try:
            product_price_fration = product.find('span', class_= 'a-price-fraction').text
            product_price = product_price_whole + product_price_fration
        except:
            product_price = product_price_whole + '00'
    except:
        product_price = "Dado indisponível"

    list_products.append(product_name)
    list_prices.append(product_price)

df = pd.DataFrame({'Nome do produto': list_products, 'Preço do produto': list_prices})
writer = pd.ExcelWriter("Pesquisa_Iphone_Amazon_Pagina1.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='Pesquisa_Iphone_Amazon_Pagina1', index=False)
writer.save()
