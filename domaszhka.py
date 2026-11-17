import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
response = requests.get(url).json()

usd_rate = response[0]["rate"]
date = response[0]["exchangedate"]

print(f"Офіційний курс НБУ на {date}: 1 USD = {usd_rate} грн\n")

uah = float(input("Введіть суму в гривнях (UAH): "))
usd = uah / usd_rate

print(f"{uah} грн = {usd:.2f} USD")