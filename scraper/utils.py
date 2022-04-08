import re

from selenium import webdriver
from bs4 import BeautifulSoup


def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("incognito")
    return options


def get_chrome_driver():
    return webdriver.Chrome(options=get_chrome_options())


def get_page(URL):
    driver = get_chrome_driver()
    driver.set_page_load_timeout(5)

    try:
        driver.get(URL)
    except Exception as err:
        pass

    return driver.page_source


def get_soup(content):
    soup = BeautifulSoup(content, "lxml")
    return soup


def price_to_str(price):
    return str(re.sub(r'[^\d.]', '', price))