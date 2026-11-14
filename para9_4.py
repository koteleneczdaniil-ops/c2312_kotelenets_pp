import requests
from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div",{"class":"Price__PriceTransition-sc-1fea8c8b-0 eZrteD"})
    res = soup_list[1].find("span")
    print(res.text)