from bs4 import BeautifulSoup
import requests
from lxml import etree
import smtplib

my_email = ""
my_password = ""

response = requests.get("https://www.amazon.com/dp/B07WJFS6LH",
                        headers={"Accept-Language": "en-US,en;q=0.9,tr;q=0.8,en-GB;q=0.7",
                                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"})

webpage = response.text

soup = BeautifulSoup(webpage, 'lxml')
price_whole = soup.find(class_="a-price-whole")
price_fraction = soup.find(class_="a-price-fraction")
price = float(price_whole.getText() + price_fraction.getText())

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Price Down Alert!\n\nThe price is now {price}. Get it while it lasts!")

    print("Message Sent.")

else:
    print("The price is still too high :(")
