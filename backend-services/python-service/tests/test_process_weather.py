"""
test_process_weather.py
=======================
Testet die Funktion process_weather aus weather_processor.py
"""

import pytest
from app.processors.weather_processor import process_weather

def test_process_weather():
    """
    Prüft, ob process_weather die aktuellen und täglichen Wetterwerte korrekt extrahiert.

    Szenario:
    - Es werden Dummy-Daten mit aktuellen Wetterwerten und Tageswerten bereitgestellt.
    - Die Funktion sollte Temperatur und Minimum korrekt zurückgeben.

    Assertions:
    - Aktuelle Temperatur wird korrekt extrahiert
    - Tages-Minimum wird korrekt extrahiert
    """
    
    weather_raw = {
        "current_weather": {
            "temperature": 20,
            "windspeed": 5,
            "weathercode": 1
        },
        "daily": {
            "temperature_2m_max": [22],
            "temperature_2m_min": [14],
            "sunrise": ["2026-02-06T07:32"],
            "sunset": ["2026-02-06T17:32"]
        }
    }

    result = process_weather(weather_raw)
    assert result["current"]["temperature"] == 20
    assert result["daily"]["temp_min"] == 14