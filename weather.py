# coding=utf-8

import pyowm

owm = pyowm.OWM('bd494464200b3a800a37d4a20963fea2')  
city = 'Pisek, CZ'

observation = owm.weather_at_place(city)
w = observation.get_weather()

#print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

tmp = w.get_temperature('celsius')['temp']
hum = w.get_humidity() 
sts = w.get_detailed_status()
wnd = w.get_wind()['speed']
prs = w.get_pressure()['press']

print('Weather in ' + city)
print(sts)
print('Temperature: '+ str(tmp) +'°C')
print('Humidity: '+ str(hum) +'%')
print('Wind: '+ str(wnd) +'m/s')
print('Pressure: '+ str(prs) +'hPa')

def getWeather():
	return {"temp":tmp, "hum":hum, "sts":sts, "wnd":wnd, "prs":prs, "city":city}
