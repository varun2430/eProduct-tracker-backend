

from scraper.amazon_search import AmazonSearch
from scraper.flipkart_search import FlipkartSearch

def scrape_search(store, search):
    if store == "amazon":
        ams = AmazonSearch()
        return ams.get_search_result(search)
    elif store == "flipkart":
        fls = FlipkartSearch()
        return fls.get_search_result(search)