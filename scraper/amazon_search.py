from datetime import datetime

from scraper.utils import get_page, get_soup, price_to_str
from models.product import Price, Product




class AmazonSearch():

    def __init__(slef):
        pass


    def get_search_result(slef, search: str):
        search = search.strip()
        search = search.replace(" ", "+")
        url = "https://www.amazon.in/s?k=" + search

        content = get_page(url)
        soup = get_soup(content)

        search_items_0 = soup.find_all("div", class_="s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16", limit=3)
        search_items_1 = soup.find_all("div", class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20", limit=3)

        result = []

        if search_items_0:
            for item in search_items_0:
                try:
                    product_id = item["data-asin"]
                    base_url = "https://www.amazon.in/dp/" + product_id
                    product_name = item.find("h2", class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2").text
                    product_price = item.find("span", class_="a-price-whole").text

                    price = Price(p=price_to_str(product_price), dt=str(datetime.now()))
                    product_date = Product(store="amazon", product_id=product_id, base_url=base_url, product_name=product_name, product_price=[price])
                    result.append(product_date)
                except Exception as err:
                    print("Unable to get product data")

        elif search_items_1:
            for item in search_items_1:
                try:
                    product_id = item["data-asin"]
                    base_url = "https://www.amazon.in/dp/" + product_id
                    # product_name = item.find("h2", class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4").text
                    product_name = item.find("span", class_="a-size-base-plus a-color-base a-text-normal").text
                    product_price = item.find("span", class_="a-price-whole").text

                    price = Price(p=price_to_str(product_price), dt=str(datetime.now()))
                    product_date = Product(store="amazon", product_id=product_id, base_url=base_url, product_name=product_name, product_price=[price])
                    result.append(product_date)
                except Exception as err:
                    print("Unable to get product data")
        return result