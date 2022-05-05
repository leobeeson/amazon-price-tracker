from time import sleep

from notification_manager import NotificationManager
from scraper_amazon_product import ScraperAmazonProduct


PRODUCT_NAME = "Some Useful Gadget"
PRODUCT_URL = "https://www.amazon.co.uk/some_useful_gadget/1234567890"
DESIRED_PRICE = 500
NOTIFICATION_EMAIL = "tylerdurden@gmail.com"
NOTIFICATION_FREQUENCY = 86400


def main() -> None:
    amazon_scraper = ScraperAmazonProduct(PRODUCT_URL, PRODUCT_NAME)
    price = amazon_scraper.get_product_price()

    if price <= DESIRED_PRICE:
        notifier = NotificationManager()
        message = notifier.format_email_message(PRODUCT_NAME, price, PRODUCT_URL)
        notifier.email_client.send_email(NOTIFICATION_EMAIL, message)


#TODO: Convert to a cron job locally or to a Lambda on AWS.
while True: 
    main()
    sleep(NOTIFICATION_FREQUENCY)
