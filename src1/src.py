from bs4 import BeautifulSoup
from selenium import webdriver
z = input("- Choose any crypto here: ")
        url = f'https://coinmarketcap.com/currencies/{z}/news/'
        driver = webdriver.Firefox()
