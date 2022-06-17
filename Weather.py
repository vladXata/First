import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('ac7402a84bmsh46c1cd42f2ef07ep19aab5jsn1270e8c82c08', language="ru")
mgr = owm.weather_manager()

place=input('What country/city are you interested in?: ')

observation = mgr.weather_at_place(place)
w = observation.weather

print("In the city " + place + " now " + w.temperature('celsius'))

pritn(w)
