#from tkinter import *
import tkinter as tk
import math as m
import time

tkinter=tk.Tk()
tkinter.title("Clock")
height, width = 400,400
tkinter.geometry(f"{width}x{height}")

canvas = tk.Canvas(tkinter, width=width, height=height)
canvas.pack()

second = canvas.create_line(0,0,0,0)
minute = canvas.create_line(0,0,0,0)
hour = canvas.create_line(0,0,0,0)
background = canvas.create_line(0,0,0,0)

def clock_face():
    global background
    radius = ((height/2)/4)*3
    canvas.delete("all")
    #canvas.delete(background)
    background = canvas.create_rectangle(0, 0, width, height, fill="black")
    background = canvas.create_oval((width/2+radius),(height/2+radius),(width/2-radius),(height/2-radius), fill="gray", outline="orange", width="5")
    for step in range(0,360,6):
        x= radius * m.cos(m.radians(step))+(width/2)
        y= radius * m.sin(m.radians(step))+(height/2)
        background = canvas.create_line((width/2),(height/2),x,y, fill="yellow", width=2)
    background = canvas.create_oval((width/2+radius-10),(height/2+radius-10),(width/2-radius+10),(height/2-radius+10), fill="gray", outline="black", width="0")
    for step in range(0,360,30):
        x= radius * m.cos(m.radians(step))+(width/2)
        y= radius * m.sin(m.radians(step))+(height/2)
        background = canvas.create_line((width/2),(height/2),x,y, fill="purple", width=5)
    background = canvas.create_oval((width/2+radius-20),(height/2+radius-20),(width/2-radius+20),(height/2-radius+20), fill="gray", outline="black", width="0")

def hours():
    global hour
    canvas.delete(hour)
    radius = ((height/2)/4)*2
    #step_h = int(time.strftime('%I')) * 30
    '''Stunde an die Analoge Mechanic anpassen!!!'''
    step_h = int(time.strftime('%I')) * 30 + int(time.strftime('%M')) * 6/12
    x= radius * m.cos(m.radians(step_h-90))+(width/2)
    y= radius * m.sin(m.radians(step_h-90))+(height/2)
    hour = canvas.create_line((width/2),(height/2),x,y, fill="green", width=5)

def minutes():
    global minute
    canvas.delete(minute)
    radius = ((height/2)/4)*2.5
    step_m = int(time.strftime('%M'))*6
    x= radius * m.cos(m.radians(step_m-90))+(width/2)
    y= radius * m.sin(m.radians(step_m-90))+(height/2)
    minute = canvas.create_line((width/2),(height/2),x,y, fill="red", width=4)

def seconds():
    update_screensize()
    clock_face()
    hours()
    minutes()
    global second
    
    radius = ((height/2)/4)*3
    step_m = int(time.strftime('%S')) *6
    x= radius * m.cos(m.radians(step_m-90))+(width/2)
    y= radius * m.sin(m.radians(step_m-90))+(height/2)
    canvas.delete(second)
    second = canvas.create_line((width/2),(height/2),x,y, fill="blue", width=2)
    #canvas.create_oval((width/2*1.03),(height/2*1.03),(width/2*0.97),(height/2*0.97), fill="blue")
    second = canvas.create_oval((width/2+6),(height/2+6),(width/2-6),(height/2-6), fill="blue")
    canvas.after(1000, seconds)

def update_screensize():
    global height, width
    height = tkinter.winfo_height()
    width = tkinter.winfo_width()
    #print(width,height)
    canvas.config(width = width,  height = height)


seconds()
tkinter.mainloop()
