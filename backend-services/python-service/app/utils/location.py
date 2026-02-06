"""
location.py
===========
Stellt eine Funktion bereit, um den Standort des aktuellen Benutzers über die IP zu ermitteln.
"""

import geocoder;

def get_location():
    """
    Bestimmt die aktuelle Latitude und Longitude anhand der IP-Adresse.

    Returns:
       list[float]: [latitude, longitude]
    """
    g = geocoder.ip('me')
    return g.latlng