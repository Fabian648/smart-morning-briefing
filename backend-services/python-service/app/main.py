"""
main.py
=======
Startpunkt der Python-Service-Anwendung. 
Lädt Standort und Wetterdaten und gibt sie strukturiert aus.
"""

from app.api_clients.weather_client import *
from app.utils.location import get_location
from app.processors.weather_processor import process_weather

lat, lon = get_location()

response = get_weather(lat, lon)

weather_data = process_weather(response)
print(weather_data)