import datetime
import sqlite3
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.4939&longitude=31.2893&current=temperature_2m"

print("Отримуємо актуальну погоду для Чернігова...")
try:
  response = requests.get(url)
  data = response.json()

  temperature = data["current"]["temperature_2m"]
except Exception as e:
  print(f"Помилка при отриманні погоди: {e}")
  temperature = 0.0

city_name = "Чернігів"
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


conn = sqlite3.connect("weather_city.db")
cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS weather_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        timestamp TEXT,
        temperature REAL
    )
"""
)


cursor.execute(
    """
    INSERT INTO weather_logs (city, timestamp, temperature)
    VALUES (?, ?, ?)
""",
    (city_name, current_time, temperature),
)
conn.commit()


cursor.execute("SELECT * FROM weather_logs")
all_records = cursor.fetchall()

print(f"\n=== Історія записів у базі даних (Місто: {city_name}) ===")
print(f"{'ID':<5} | {'Місто':<12} | {'Дата та час':<20} | {'Температура':<12}")
print("-" * 60)

for row in all_records:
  row_id, city, timestamp, temp = row
  print(f"{row_id:<5} | {city:<12} | {timestamp:<20} | {temp} °C")


conn.close()