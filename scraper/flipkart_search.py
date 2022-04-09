import re
from datetime import datetime

from scraper.utils import get_page, get_soup, price_to_str
from models.product import Price, Product




class FlipkartSearch():

    def __init__(slef):
        pass


    def get_baseURL(self, URL):
        return URL[:URL.index("&lid")]


    def get_productID(self, base_url):
        pid = re.search(r"=([a-zA-Z0-9]{16})", base_url)
        return pid.group(1)


    def get_search_result(self, search: str):
        search = search.strip()
        search = search.replace(" ", "+")
        url = "https://www.flipkart.com/search?q=" + search

        content = get_page(url)
        soup = get_soup(content)

        search_items_0 = soup.find_all("a", class_="_1fQZEK", limit=3)
        search_items_1 = soup.find_all("div", class_="_4ddWXP", limit=3)
        search_items_2 = soup.find_all("div", class_="_1xHGtK _373qXS", limit=3)

        result = []

        if search_items_0:
            for item in search_items_0:
                try:
                    full_url = "https://www.flipkart.com" + item["href"]
                    base_url = self.get_baseURL(full_url)
                    product_id = self.get_productID(base_url)
                    product_name = item.find("div", class_="_4rR01T").text
                    product_price = item.find("div", class_="_30jeq3 _1_WHN1").text

                    price = Price(p=price_to_str(product_price), dt=str(datetime.now()))
                    product_data = Product(store="flipkart", product_id=product_id, base_url=base_url, product_name=product_name, product_price=[price])
                    result.append(product_data)
                except Exception as err:
                    print("Unable to get product data")

        elif search_items_1:
            for item in search_items_1:
                try:
                    full_url = "https://www.flipkart.com" + item.find("a", class_="_2rpwqI")["href"]
                    base_url = self.get_baseURL(full_url)
                    product_id = self.get_productID(base_url)
                    product_name = item.find("a", class_="s1Q9rs")["title"]
                    product_price = item.find("div", class_="_30jeq3").text

                    price = Price(p=price_to_str(product_price), dt=str(datetime.now()))
                    product_data = Product(store="flipkart", product_id=product_id, base_url=base_url, product_name=product_name, product_price=[price])
                    result.append(product_data)
                except Exception as err:
                    print("Unable to get product data")

        elif search_items_2:
            for item in search_items_2:
                try:
                    full_url = "https://www.flipkart.com" + item.find("a", class_="_2UzuFa")["href"]
                    base_url = self.get_baseURL(full_url)
                    product_id = self.get_productID(base_url)
                    product_name = item.find("a", class_="IRpwTa")["title"]
                    product_price = item.find("div", class_="_30jeq3").text

                    price = Price(p=price_to_str(product_price), dt=str(datetime.now()))
                    product_data = Product(store="flipkart", product_id=product_id, base_url=base_url, product_name=product_name, product_price=[price])
                    result.append(product_data)
                except Exception as err:
                    print("Unable to get product data")
        return result