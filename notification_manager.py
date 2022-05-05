from email_client import EmailClient


EMAIL_CLIENT = EmailClient("smtp.gmail.com")

class NotificationManager():

    def __init__(self) -> None:
        self.email_client = EMAIL_CLIENT
    

    def format_email_message(self, product_name: str, price: float, product_url: str) -> str:
        email_text = f"Subject:Amazon Price Tracker: {product_name}!\n\nProduct ({product_name}) is below your desired price. Currently it is being sold at: £{price}\n\nHere's its Amazon URL: {product_url}"
        email_text = email_text.encode("ascii", "ignore")
        return email_text
    
