# coding=utf-8

import pyowm
import geo as g

class Weather:
    def __init__(self):
        self.owm = pyowm.OWM('bd494464200b3a800a37d4a20963fea2')  
        self.place = g.Place()
        self.coords = None
        self.city = None

    def observe(self):
        self.coords = self.place.getCoords()
        self.city = self.place.getPlace()
        observation = self.owm.weather_at_coords(self.coords[0], self.coords[1])
        return observation.get_weather()

    def getWeather(self):
        w = self.observe()
        time = self.timeCorrection(w.get_reference_time(timeformat="iso"))
        tmp = w.get_temperature('celsius')['temp']
        hum = w.get_humidity() 
        sts = w.get_detailed_status()
        wnd = w.get_wind()['speed']
        prs = w.get_pressure()['press']
        return {"temp":tmp, "hum":hum, "sts":sts, "wnd":wnd, "prs":prs, "city":self.city, "time":time}

    def getIcon(self):
        w = self.observe()
        icn = w.get_weather_icon_name()
        image_url = "http://openweathermap.org/img/w/" + icn + ".png"
        return image_url

    def timeCorrection(self, t):
        parts1 = t.split(" ")
        parts2 = parts1[1].split(":")
        parts3 = parts2[2].split("+")
        h = int(parts2[0]) + 1
        return parts1[0] + " " + str(h) + ":" + parts2[1] + ":" + parts3[0]