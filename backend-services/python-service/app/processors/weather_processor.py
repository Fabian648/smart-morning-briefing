"""
weather_processor.py
====================
Verarbeitet die rohen Wetterdaten von Open-Meteo in ein vereinfachtes Format.
"""

def process_weather(weather_json: dict) -> dict:
    """
    Extrahiert die wichtigsten Werte aus den aktuellen und täglichen Wetterdaten.

    Args:
        weather_json (dict): JSON-Daten von Open-Meteo

    Returns:
        dict: strukturierte Wetterinformationen mit aktuellen und Tageswerten
    """
    current = weather_json.get("current_weather", {})
    daily = weather_json.get("daily", {})

    return {
        "current": {
            "temperature": current.get("temperature"),
            "windspeed": current.get("windspeed"),
            "weathercode": current.get("weathercode")
        },
        "daily":{
            # [0] nehmen, weil Open-Meteo eine Liste zurückgibt, wir aber nur den heutigen Wert brauchen
            "temp_max": daily.get("temperature_2m_max",[None])[0],
            "temp_min": daily.get("temperature_2m_min",[None])[0],
            "sunrise": daily.get("sunrise",[None])[0],
            "sunset": daily.get("sunset",[None])[0],
            "weathercode": daily.get("weathercode",[None])[0]
        }

    }