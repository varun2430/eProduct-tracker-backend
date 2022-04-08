from datetime import datetime
import re

from .utils import get_page, get_soup, price_to_str
from models.product import Price, Product




def get_product_name(soup):
    return soup.find("span", class_="B_NuCI")


def get_product_price(soup):
    return soup.find("div", class_="_30jeq3 _16Jk6d")




class Flipkart:
    def __init__(self):
        pass


    def get_baseURL(self, URL):
        return URL[:URL.index("&lid")]


    def get_productID(self, base_url):
        pid = re.search(r"=([a-zA-Z0-9]{16})", base_url)
        return pid.group(1)


    def get_product_data(self, URL):
        try:
            self.base_url = self.get_baseURL(URL)
            self.product_id = self.get_productID(self.base_url)
        except Exception as err:
            print("Invalid URL")
            return None

        try:
            self.content = get_page(self.base_url)
            self.soup = get_soup(self.content)
        except Exception as err:
            print("Unable to get soup/page content")
            return None

        try:
            self.product_name = get_product_name(self.soup).text
            self.product_price = price_to_str(get_product_price(self.soup).text)
        except Exception as err:
            print("Unable to get product data")
            return None

        self.price = Price( p=self.product_price, dt=str(datetime.now()) )
        self.product_data = Product( store="flipkart", product_id=self.product_id, base_url=self.base_url, product_name=self.product_name, product_price=[self.price] )

        return self.product_data
