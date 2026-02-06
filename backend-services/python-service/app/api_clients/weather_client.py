"""
weather_client.py
=================
Stellt eine Funktion bereit, um Wetterdaten von Open-Meteo abzurufen.
"""

import requests
from app.config import WEATHER_API_URL, WEATHER_DAILY_PARAMS, TIMEZONE

def get_weather(lat: float, lon: float):
    """
    Ruft Wetterdaten für einen gegebenen Standort ab.

    Args:
        lat (float): Breitengrad
        lon (float): Längengrad

    Returns:
        dict: JSON-Daten von Open-Meteo als Python-Dict
    """
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "daily": ",".join(WEATHER_DAILY_PARAMS), # Liste der Tagesparameter
        "timezone": TIMEZONE
    }

    response = requests.get(WEATHER_API_URL, params=params)
    response.raise_for_status() # Fehler werfen, falls die Anfrage fehlschlägt
    return response.json()
