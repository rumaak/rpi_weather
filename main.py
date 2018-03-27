import gui
import weather
from Tkinter import Tk

w = weather.WeatherManager()
root = Tk()
g = gui.GUI(root, w)
g.put_data()
root.mainloop()