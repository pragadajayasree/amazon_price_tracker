import requests
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.in/HP-i3-1215U-Graphics-Speakers-dy5008TU/dp/B0BZS88YPT/ref=lp_100144015031_1_3?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=N4BK9K0F4KGCCRSFN0A5&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",

}

response = requests.get(url=url, headers=header)
result = response.text

soup = BeautifulSoup(result, "lxml")
a = soup.select_one(selector=".a-price-whole")
price = a.getText()

p = soup.select_one(selector="#productTitle")
title = p.getText()
current_price = f"₹{price}"
link = url
message = f"subject:amazon price alert\n\ntitle:{title}\nprice:{current_price}\nlink:{link}"
email = "pragadajayasree@gmail.com"
password = "psqf nzxg kvui vybv"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="pragadajayasree@yahoo.com", msg=message)
print(message)
