"""
config.py
=========
Konfigurationsparameter für die API Schnittstellen
"""
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_DAILY_PARAMS = [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_probability_max",
    "sunrise",
    "sunset",
    "weathercode"
]

TIMEZONE = "auto"

