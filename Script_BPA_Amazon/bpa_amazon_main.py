from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

DRIVER_PATH = 'D:\will\Projeto Python\Script_BPA_Amazon\Chrome_Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')