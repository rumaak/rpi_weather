# coding=utf-8

import weather as w
from Tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master, wthr):
        self.master = master
	self.wthr = wthr
	#master.attributes("-fullscreen", True)
	master.minsize(width=400, height=240)
    	master.maxsize(width=400, height=240)
	master.title("A simple GUI")

       # self.label = Label(master, text="This is our first GUI!")
       # self.label.pack()

       # self.greet_button = Button(master, text="Greet", command=self.greet)
       # self.greet_button.pack()

       # self.close_button = Button(master, text="Close", command=master.quit)
       # self.close_button.pack()

	self.label = Label(master, anchor="w", justify="left", 
			   text="Weather in " + wthr["city"] + "\n" + wthr["sts"] + "\nTemperature: " + str(wthr["temp"]) + "°C\nHumidity: " + str(wthr["hum"]) + "% \nWind: " + str(wthr["wnd"]) + "m/s \nPressure: " + str(wthr["prs"]) + "hPa")
	self.label.pack()

    def greet(self):
        print("Greetings!")

we = w.getWeather()
root = Tk()
my_gui = MyFirstGUI(root, we)
root.mainloop()
