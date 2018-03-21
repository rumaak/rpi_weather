# coding=utf-8

from PIL import Image, ImageTk
import urllib2, cStringIO
import weather as w
import pyowm
import googlemaps
from Tkinter import Tk, Label, Button

class GUI:
    def __init__(self, master, wet):
        self.master = master
        self.wet = wet
        self.wthr = None
        self.img = None
        self.tkImg = None

        master.config(cursor="none")
        # master.attributes("-fullscreen", True)
        master.minsize(width=400, height=240)
        master.maxsize(width=400, height=240)
        master.title("Weather")
        master.configure(background='black')

        self.label = Label(master)
        self.label.pack()

        self.err_label = Label(master, background="black", foreground="white")
        self.err_label.pack()

    def put_data(self):
        print("updated")
        try:
          self.wthr = wet.getWeather()
          self.img = wet.getIcon()

          file = cStringIO.StringIO(urllib2.urlopen(self.img).read())
          self.tkImg = Image.open(file)
          self.img = ImageTk.PhotoImage(self.tkImg)

          self.label.config(text=self.weatherInfo())
          self.err_label.config(text="")

        except (googlemaps.exceptions.TransportError, pyowm.exceptions.api_call_error.APICallError):
          if self.wthr:
            self.label.config(text=self.weatherInfo())
            self.img = ImageTk.PhotoImage(self.tkImg)
            self.err_label.config(text="Connection interrupted, last updated: " + self.wthr["time"])
          else:
            self.img = Image.open("error.png")
            self.img = ImageTk.PhotoImage(self.img)
    
            self.label.config(text="No internet connection")

        self.label.config(background="black", compound="top", image=self.img, font=("Times New Roman",12,"bold"),foreground="white")
        self.label.image = self.img
        self.master.after(6000, self.put_data)

    def weatherInfo(self):
        return "Weather in " + str(self.wthr["city"]) + "\n" + str(self.wthr["sts"]) + "\nTemperature: " + str(self.wthr["temp"]) + "°C\nHumidity: " + str(self.wthr["hum"]) + "% \nWind: " + str(self.wthr["wnd"]) + "m/s \nPressure: " + str(self.wthr["prs"]) + "hPa"

wet = w.Weather()
root = Tk()
my_gui = GUI(root, wet)  
my_gui.put_data() 
root.mainloop()
