"""
test_location.py
================
Testet die Funktion get_location aus location.py
"""

import pytest
from app.utils.location import get_location

def test_get_location():
    """
    Prüft, ob get_location die aktuelle Position korrekt zurückgibt.

    Assertions:
    - Ergebnis ist eine Liste
    - Liste hat genau zwei Elemente (Latitude und Longitude)
    - Beide Elemente sind vom Typ float
    """
    
    loc = get_location()
    
    assert isinstance(loc, list), "Ergebnis sollte eine Liste sein"
    assert len(loc) == 2, "Liste sollte genau zwei Elemente enthalten"
    assert all(isinstance(coord, float) for coord in loc), "Beide Elemente sollten float sein"