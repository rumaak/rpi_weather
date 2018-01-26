# coding=utf-8

from PIL import Image, ImageTk
import urllib, cStringIO
import weather as w
from Tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master, wthr, img):
        self.master = master

	master.config(cursor="none")
	master.attributes("-fullscreen", True)
	#master.minsize(width=400, height=240)
    	#master.maxsize(width=400, height=240)
	master.title("Weather")
	master.configure(background='black')

	file = cStringIO.StringIO(urllib.urlopen(img).read())
	img = Image.open(file)
	img = ImageTk.PhotoImage(img)

       # self.label = Label(master, text="This is our first GUI!")
       # self.label.pack()

       # self.greet_button = Button(master, text="Greet", command=self.greet)
       # self.greet_button.pack()

       # self.close_button = Button(master, text="Close", command=master.quit)
       # self.close_button.pack()

	self.label = Label(master, background="black", compound="top", image=img, font=("Times New Roman",12,"bold"),foreground="white",
			   text="Weather in " + str(wthr["city"]) + "\n" + str(wthr["sts"]) + "\nTemperature: " + str(wthr["temp"]) + "°C\nHumidity: " + str(wthr["hum"]) + "% \nWind: " + str(wthr["wnd"]) + "m/s \nPressure: " + str(wthr["prs"]) + "hPa")

	self.label.image = img

	self.label.pack()

    def greet(self):
        print("Greetings!")

we = w.getWeather()
img = w.getIcon()
root = Tk()
my_gui = MyFirstGUI(root, we, img)
root.mainloop()
