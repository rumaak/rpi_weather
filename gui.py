# coding=utf-8

from PIL import Image, ImageTk
from Tkinter import Tk, Label, Button
import weather
import googlemaps
import pyowm

class GUI:
    def __init__(self, master, wet):
        self.master = master
        self.img = None
        self.tkImg = None
        self.wet = wet
        self.today_color = "#202020"
        self.other_day_color = "#353535"
        self.line_color = "#494949"
        self.text_color = "white"
        self.succ_request = False

        master.config(cursor="none")
        master.attributes("-fullscreen", True)
        # master.minsize(width=400, height=240)
        # master.maxsize(width=400, height=240)
        master.title("Weather")
        master.configure(background='white')

        self.bigImage = Label(master, bg=self.today_color)
        self.bigImage.place(width=160, height=155, x=0, y=0)

        self.bigTemp = Label(master, font=("Arial",48), padx=0, pady=0, anchor="w", bg=self.today_color, fg="white")
        self.bigTemp.place(width=120, height=115, x=160, y=0)

        self.status = Label(master, font=("Arial",10, "italic"), anchor="nw", padx=0, pady=0, wraplength=120, justify="left", bg=self.today_color, fg=self.text_color)
        self.status.place(width=120, height=65, x=160, y=90)

        self.bigDate = Label(master, font=("Arial",12, "bold"), justify="left", anchor="sw", bg=self.today_color, fg=self.text_color)
        self.bigDate.place(width=120, height=50, x=280, y=0)

        self.smallDate = Label(master, font=("Arial",10), justify="left", anchor="w", bg=self.today_color, fg=self.text_color)
        self.smallDate.place(width=120, height=15, x=280, y=50)

        self.bigPlace = Label(master, font=("Arial",12,"bold"), justify="left", anchor="sw", bg=self.today_color, fg=self.text_color)
        self.bigPlace.place(width=120, height=40, x=280, y=65)

        self.smallPlace = Label(master, font=("Arial",10), justify="left", anchor="nw", bg=self.today_color, fg=self.text_color)
        self.smallPlace.place(width=120, height=55, x=280, y=105)

        self.horizontal_line = Label(master, bg=self.line_color)
        self.horizontal_line.place(width=400, height=1, x=0, y=154)

        # 1st day

        self.day1up = Label(master, font=("Arial",10), bg=self.today_color, fg=self.text_color)
        self.day1up.place(width=80, height=30, x=0, y=155)

        self.day1temp = Label(master, font=("Arial",10), bg=self.today_color, fg=self.text_color)
        self.day1temp.place(width=80, height=30, x=0, y=210)

        self.day1pic = Label(master, bg=self.today_color)
        self.day1pic.place(width=80, height=30, x=0, y=185)

        # 2nd day

        self.day2up = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day2up.place(width=80, height=30, x=80, y=155)

        self.day2temp = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day2temp.place(width=80, height=30, x=80, y=210)

        self.day2pic = Label(master, bg=self.other_day_color)
        self.day2pic.place(width=80, height=30, x=80, y=185)

        # 3rd day
        self.day3up = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day3up.place(width=80, height=30, x=160, y=155)

        self.day3temp = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day3temp.place(width=80, height=30, x=160, y=210)

        self.day3pic = Label(master, bg=self.other_day_color)
        self.day3pic.place(width=80, height=30, x=160, y=185)        

        # 4th day
        self.day4up = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day4up.place(width=80, height=30, x=240, y=155)

        self.day4temp = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day4temp.place(width=80, height=30, x=240, y=210)

        self.day4pic = Label(master, bg=self.other_day_color)
        self.day4pic.place(width=80, height=30, x=240, y=185)   

        # 5th day 
        self.day5up = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day5up.place(width=80, height=30, x=320, y=155)

        self.day5temp = Label(master, font=("Arial",10), bg=self.other_day_color, fg=self.text_color)
        self.day5temp.place(width=80, height=30, x=320, y=210)

        self.day5pic = Label(master, bg=self.other_day_color)
        self.day5pic.place(width=80, height=30, x=320, y=185)  

        # Vertical lines
        self.vertical_line1 = Label(master, bg=self.line_color)
        self.vertical_line1.place(width=1, height=85, x=80, y=155)

        self.vertical_line2 = Label(master, bg=self.line_color)
        self.vertical_line2.place(width=1, height=85, x=160, y=155)

        self.vertical_line3 = Label(master, bg=self.line_color)
        self.vertical_line3.place(width=1, height=85, x=240, y=155)

        self.vertical_line4 = Label(master, bg=self.line_color)
        self.vertical_line4.place(width=1, height=85, x=320, y=155)

    def put_data(self):
        print("updated")
        try:
            self.today = self.wet.getToday()
            self.forecast = self.wet.getForecast()
            self.succ_request = True
        except (googlemaps.exceptions.TransportError, pyowm.exceptions.api_call_error.APICallError):
            if not self.succ_request:
                self.today = {"temp":"", "sts":"No internet connection", "city":"", "position":"", "icon":"icons/error.png", "day":"", "month":"", "datum":""}
                self.forecast = [{"temp":"", "day":"", "icon":"icons/error.png"}]*4

        # Today
        self.todayImage = Image.open(self.today["icon"])
        self.todayImage = self.todayImage.resize((110,110), Image.ANTIALIAS)
        self.todayImage = ImageTk.PhotoImage(self.todayImage)

        self.bigImage.config(image=self.todayImage)
        self.bigImage.img = self.todayImage
        self.bigTemp.config(text=self.today["temp"])
        self.status.config(text=self.today["sts"])
        self.bigDate.config(text=self.today["day"])
        self.smallDate.config(text=self.today["month"]+ " " + self.today["datum"])
        self.bigPlace.config(text=self.today["city"])
        self.smallPlace.config(text=self.today["position"])

        # Day 1
        self.smallImage1 = Image.open(self.today["icon"])
        self.smallImage1 = self.smallImage1.resize((30,30), Image.ANTIALIAS)
        self.smallImage1 = ImageTk.PhotoImage(self.smallImage1)

        self.day1up.config(text=self.today["day"])
        self.day1temp.config(text=self.today["temp"])
        self.day1pic.config(image=self.smallImage1)
        self.day1pic.img = self.smallImage1

        # Day 2 
        self.smallImage2 = Image.open(self.forecast[0]["icon"])
        self.smallImage2 = self.smallImage2.resize((30,30), Image.ANTIALIAS)
        self.smallImage2 = ImageTk.PhotoImage(self.smallImage2)

        self.day2up.config(text=self.forecast[0]["day"])
        self.day2temp.config(text=self.forecast[0]["temp"])
        self.day2pic.config(image=self.smallImage2)
        self.day2pic.img = self.smallImage2        

        # Day 3
        self.smallImage3 = Image.open(self.forecast[1]["icon"])
        self.smallImage3 = self.smallImage3.resize((30,30), Image.ANTIALIAS)
        self.smallImage3 = ImageTk.PhotoImage(self.smallImage3)

        self.day3up.config(text=self.forecast[1]["day"])
        self.day3temp.config(text=self.forecast[1]["temp"])
        self.day3pic.config(image=self.smallImage3)
        self.day3pic.img = self.smallImage3      

        # Day 4
        self.smallImage4 = Image.open(self.forecast[2]["icon"])
        self.smallImage4 = self.smallImage4.resize((30,30), Image.ANTIALIAS)
        self.smallImage4 = ImageTk.PhotoImage(self.smallImage4)

        self.day4up.config(text=self.forecast[2]["day"])
        self.day4temp.config(text=self.forecast[2]["temp"])
        self.day4pic.config(image=self.smallImage4)
        self.day4pic.img = self.smallImage4 

        # Day 5
        self.smallImage5 = Image.open(self.forecast[3]["icon"])
        self.smallImage5 = self.smallImage5.resize((30,30), Image.ANTIALIAS)
        self.smallImage5 = ImageTk.PhotoImage(self.smallImage5)

        self.day5up.config(text=self.forecast[3]["day"])
        self.day5temp.config(text=self.forecast[3]["temp"])
        self.day5pic.config(image=self.smallImage5)
        self.day5pic.img = self.smallImage5 

        # Lines
        self.vertical_line1.config(bg=self.line_color)
        self.vertical_line2.config(bg=self.line_color)
        self.vertical_line3.config(bg=self.line_color)
        self.vertical_line4.config(bg=self.line_color)
        self.horizontal_line.config(bg=self.line_color)

        self.master.after(300000, self.put_data)

