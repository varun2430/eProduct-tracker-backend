from scraper.flipkart_scraper import Flipkart


if __name__ == "__main__":
    flp = Flipkart()
    p = flp.get_product_data("https://www.flipkart.com/apple-iphone-13-blue-128-gb/p/itm6c601e0a58b3c?pid=MOBG6VF5SMXPNQHG&lid=LSTMOBG6VF5SMXPNQHGL5FN51&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_metro_expandable_6_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_92RED14GXPXF_wp2&fm=neo%2Fmerchandising&iid=9dc19af6-2495-41aa-be3f-32ebc0b76a66.MOBG6VF5SMXPNQHG.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=c9620oxbio0000001649394584614")
    print(p)