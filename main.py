import requests
import smtplib
from bs4 import BeautifulSoup

MY_EMAIL = #email
MY_PASSWORD = #password

product_url = "https://www.amazon.com/Kamado-Joe-BJ24RH-Big-Grill/dp/B00IIUO9FQ/"

response = requests.get(
    product_url,
    headers={
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/102.0.5005.63 Safari/537.36",
    }
)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")

price_unformatted = soup.find(name="span", class_="a-offscreen").getText()
price = float(price_unformatted.split("$")[1].replace(",", ""))
buy_price = 1100.00
title = soup.find(id="productTitle").getText().replace("       ", "")

if price < buy_price:
    price = '{0:.2f}'.format(price)
    message = f"{title} is now only ${price}!"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=#email address,
            msg=f"Subject: Amazon Price Alert!!\n\n{message}\n{product_url}"
        )
        
