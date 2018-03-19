# coding=utf-8

import pyowm

owm = pyowm.OWM('bd494464200b3a800a37d4a20963fea2')  
city = 'Pisek, CZ'

observation = owm.weather_at_place(city)

def getWeather():
    w = observation.get_weather()
    tmp = w.get_temperature('celsius')['temp']
    hum = w.get_humidity() 
    sts = w.get_detailed_status()
    wnd = w.get_wind()['speed']
    prs = w.get_pressure()['press']
    return {"temp":tmp, "hum":hum, "sts":sts, "wnd":wnd, "prs":prs, "city":city}

def getIcon():
    w = observation.get_weather()
    icn = w.get_weather_icon_name()
    image_url = "http://openweathermap.org/img/w/" + icn + ".png"
    return image_url

