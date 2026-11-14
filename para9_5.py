import requests
from bs4 import BeautifulSoup

# Ваш оригинальный код парсинга
response = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all("div", {"class": "Price__PriceTransition-sc-1fea8c8b-0 eZrteD"})
res = soup_list[1].find("span")

price = float(res.text.replace("$", "").replace(",", ""))

btc = float(input("Сколько у вас биткоинов? "))
print(f"Это: {btc * price * 41.5:,.2f} грн")