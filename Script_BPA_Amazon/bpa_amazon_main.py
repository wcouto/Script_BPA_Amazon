from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter



def get_url(driver_path, url):
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    return driver

def wait(driver):
    driver.implicitly_wait(5)

def do_search(driver):
    search_box = driver.find_element_by_id('twotabsearchtextbox').send_keys("iphone")
    search_button = driver.find_element_by_id("nav-search-submit-text").click()

def get_all_products(driver):
    soup = BeautifulSoup(driver.page_source, "lxml")
    products = soup.find_all('div', {'data-asin': True, 'data-component-type': 's-search-result'})
    return products

def create_list_products():
    list_products = []
    return list_products

def create_list_prices():
    list_prices = []
    return list_prices

def populate_dicts(products, list_products, list_prices):

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

def create_excel(list_products, list_prices):
    df = pd.DataFrame({'Nome do produto': list_products, 'Preço do produto': list_prices})
    writer = pd.ExcelWriter("Pesquisa_Iphone_Amazon_Pagina1.xlsx", engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Pesquisa_Iphone_Amazon_Pagina1', index=False)
    writer.save()

def main():
    print("Receiving parameters to build the driver.")
    driver = get_url("C:\\Users\willi\\Projeto Python\\Script_BPA_Amazon\\Chrome_Driver\\chromedriver.exe", 'https://www.amazon.com.br/')
    wait(driver)

    print("Searching 'Iphone' on amazon website.")
    do_search(driver)
    wait(driver)

    print("Receiving all products from the first page.")
    products = get_all_products(driver)
    wait(driver)

    list_products = create_list_products()
    list_prices = create_list_prices()

    print("Saving the products informations")
    populate_dicts(products, list_products, list_prices)

    print("Creating Excel.")
    create_excel(list_products, list_prices)

if __name__ == '__main__':
    main()