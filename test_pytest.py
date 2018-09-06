import pytest
import json
from weather import Weather

def test_WeatherProvider():
    w = Weather()
    j = w.getDataAsJSON("http://api.openweathermap.org/data/2.5/weather?q=Istanbul&APPID=3d049d48e11ad8bf9a8a7d01c66135aa") 
    print(j)  
    assert j[0]["main"]["temp"] is not None
    
def test_getinfo():
    w = Weather()
    ret = json.loads(w.getInfo())
    assert ret["error"] is None

def test_unknowncity():
    ret = json.loads(Weather().getInfo(city="Ankarak"))
    print(ret)
    assert ret["error"] is None

