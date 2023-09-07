import os
import requests
import time


api_key = os.environ["OPENWEATHERMAP_API_KEY"]
lat = 48.8566
lon = 2.3522
weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&exclude=minutely,hourly,daily,alerts"
weather_response = requests.get(weather_url).json()
weather_to_emoji = {
    "Thunderstorm": "⛈",
    "Drizzle": "🌦",
    "Rain": "🌧",
    "Snow": "❄️",
    "Mist": "🌫",
    "Smoke": "💨",
    "Haze": "🌁",
    "Dust": "💨",
    "Fog": "🌁",
    "Sand": "🌀",
    "Ash": "🌋",
    "Squall": "🌀",
    "Tornado": "🌪",
    "Clear": "☀️",
    "Clouds": "☁️",
}

current_weather_emoji = weather_to_emoji.get(
    weather_response["weather"][0]["main"], "❓"
)
current_temp_c = weather_response["main"]["temp"]
current_temp_f = current_temp_c * 9 / 5 + 32

svg = None

# Read the template.svg file as utf8
with open("template.svg", "r", encoding="utf8") as f:
    svg = f.read()

if svg is None:
    raise Exception("Could not read template.svg")

# Replace the values
svg = svg.replace("[[TEMPC]]", f"{current_temp_c:.1f}")
svg = svg.replace("[[TEMPF]]", f"{current_temp_f:.1f}")
svg = svg.replace("[[WEATHER]]", current_weather_emoji)
svg = svg.replace("[[DAYOFWEEK]]", time.strftime("%A"))

# Write the new 🐈.svg file
with open("🐈.svg", "w", encoding="utf8") as f:
    f.write(svg)
