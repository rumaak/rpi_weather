# coding=utf-8

import pyowm
import geo as g
import datetime
import dateutil.parser
import calendar

class WeatherManager:
    def __init__(self):
        self.owm = pyowm.OWM('bd494464200b3a800a37d4a20963fea2')  
        self.place = g.Place()
        self.coords = None
        self.city = None
        self.position = None

    def observe(self):
        self.coords = self.place.getCoords()
        self.position = self.place.getPlace()
        parts1 = self.position.split(",")
        self.city = parts1[0]
        observation = self.owm.weather_at_coords(self.coords[0], self.coords[1])
        return observation.get_weather()

    def getToday(self):
        w = self.observe()
        day = calendar.day_name[dateutil.parser.parse(w.get_reference_time("iso")).weekday()]
        # time = self.timeCorrection(w.get_reference_time(timeformat="iso"))
        tmp = int(round(w.get_temperature('celsius')['temp']))
        # hum = w.get_humidity() 
        sts = w.get_detailed_status()
        # wnd = w.get_wind()['speed']
        # prs = w.get_pressure()['press']
        sts = sts[0].capitalize() + sts[1:]
        month = self.getMonthFromISO(w.get_reference_time('iso'))
        datum = self.getDayFromISO(w.get_reference_time('iso'))
        return {"temp":str(tmp) + "°", "sts":sts, "city":self.city, "position":self.position, "icon":self.getTodayIcon(), "day":day, "month":month, "datum":datum}

    def getTodayIcon(self):
        w = self.observe()
        icn = w.get_weather_icon_name()
        image = "icons/" + icn + ".png"
        return image

    def getForecast(self):
        o = self.observe()
        w = self.owm.three_hours_forecast_at_coords(self.coords[0], self.coords[1])        
        forecast = w.get_forecast()
        forecasts = []
        mean = 0
        fs = 8
        icon = ""
        for f in forecast:
            if int(self.getDayFromISO(f.get_reference_time('iso'))) != datetime.date.today().day:
                weekday = calendar.day_name[dateutil.parser.parse(f.get_reference_time('iso')).weekday()]
                mean += f.get_temperature('celsius')['temp']
                if fs == 5:
                    icon = f.get_weather_icon_name()
                if fs > 1:
                    fs -= 1
                else:
                    forecasts.append({"temp":str(int(round(mean/8))) + "°", "day":weekday, "icon":"icons/" + icon + ".png"})
                    fs = 8
                    mean = 0
        return forecasts

    def getDayFromISO(self, iso):
        parts1 = iso.split("-")
        parts2 = parts1[2].split(" ")
        return parts2[0]

    def getMonthFromISO(self, iso):
        parts1 = iso.split("-")
        return calendar.month_name[int(parts1[1])]

    # def timeCorrection(self, t):
    #     parts1 = t.split(" ")
    #     parts2 = parts1[1].split(":")
    #     parts3 = parts2[2].split("+")
    #     h = int(parts2[0]) + 1
    #     return parts1[0] + " " + str(h) + ":" + parts2[1] + ":" + parts3[0]