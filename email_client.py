import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
SENDER_GMAIL_USER = os.getenv("GMAIL_TEST_USER")
SENDER_APP_PW = os.getenv("APP_PASSWORD")


class EmailClient:

    def __init__(self, smtp_client: str) -> None:
        self.smtp_client = smtp_client


    def send_email(
                    self, 
                    to_user: str, 
                    payload: str
                    ) -> None:
        with smtplib.SMTP(self.smtp_client, 587) as connection:
            connection.starttls()
            connection.login(user=SENDER_GMAIL_USER, password=SENDER_APP_PW)
            connection.sendmail(
                from_addr=SENDER_GMAIL_USER, 
                to_addrs=to_user, 
                msg=payload
                )
