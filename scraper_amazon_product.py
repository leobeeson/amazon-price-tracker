import json
from scraper import Scraper


ID_PRICE_DISPLAY = "corePriceDisplay_desktop_feature_div"
CLASS_PRICE_WHOLE = "a-price-whole"
CLASS_PRICE_DECIMALS = "a-price-fraction"

# Get your http headers using this: http://myhttpheader.com/  
REQUEST_HEADERS_FILEPATH = "./request_headers.json"

class ScraperAmazonProduct(Scraper):

    def __init__(self, product_url, product_name) -> None:
        self.page_url = product_url
        self.product_name = product_name
        self.read_request_headers_from_file(REQUEST_HEADERS_FILEPATH)
        super().__init__()


    def get_product_price(self) -> float:
        seletor_price_whole = f"#{ID_PRICE_DISPLAY} .{CLASS_PRICE_WHOLE}"
        seletor_price_decimals = f"#{ID_PRICE_DISPLAY} .{CLASS_PRICE_DECIMALS}"
        price_whole = self.soup.select(seletor_price_whole)[0].get_text()
        price_decimals = self.soup.select(seletor_price_decimals)[0].get_text()
        price_float = float(price_whole+price_decimals)
        return price_float


    def read_request_headers_from_file(self, filepath: str) -> dict:
        with open(filepath) as json_file:
            data = json.load(json_file)
            self.headers = data


