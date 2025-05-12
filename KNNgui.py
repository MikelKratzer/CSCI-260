import tkinter as tk  # Current version 
from tkinter import ttk # Special version
from kNearestNeighbors import *

def handle_click(event): # gathers user input and passes them to KNN
    global entry1,entry2,entry3,combo1,combo2,combo3,Kentry,Pentry,Sentry
    KNN(entry1.get(),entry2.get(),entry3.get(), \
        combo1.get(),combo2.get(),combo3.get(), \
        Kentry.get(),Pentry.get(),Sentry.get() )
    #print(entry.get())

window = tk.Tk() # creates main application window

fields=["longitude", # lists fields from data
  "latitude",
  "housing_median_age",
  "total_rooms",
  "total_bedrooms",
  "population",
  "households",
  "median_income",
  "median_house_value"]

def makeCombo(frame,label,fields): # creates UI panel with a label, dropdown menu, and a slider
    f=tk.Frame(frame)
    tk.Label(f,text=label).pack()
    combo = ttk.Combobox(f,state="readonly",values=fields) # dropdown menu
    combo.pack() # this is packing Combobox into the f1 frame
    tk.Label(f,text="Target Value").pack()
    entry = tk.Scale(f,from_=0.0,to=1.0,resolution=.05) # slider
    entry.pack()
    f.pack(side=tk.LEFT)
    return (combo,entry) # returns dropdown and slider

def makeOneEntry(frame,label): # creates labeled text entry field (K size, sample size, seed)
    f=tk.Frame(frame)
    tk.Label(f,text=label).pack(side=tk.LEFT)
    entry = tk.Entry(f,width=10)
    entry.pack(side=tk.LEFT)
    f.pack()
    return entry # returns user input

f=tk.Frame(window)
(combo1,entry1)=makeCombo(f,"Field 1",fields) # display Field 1, 2, 3
(combo2,entry2)=makeCombo(f,"Field 2",fields)
(combo3,entry3)=makeCombo(f,"Field 3",fields)
f.pack()

Kentry=makeOneEntry(window,"K size")
Pentry=makeOneEntry(window,"Sample %")
Sentry=makeOneEntry(window,"Seed Number")

fB=tk.Frame(window)
button = tk.Button(fB,text="Chart Now")
button.bind("<Button-1>", handle_click) # when "Chart Now" is clicked, runs handle_click (runs KNN)
button.pack(side=tk.LEFT)
cancel = tk.Button(fB,text="Cancel") # "Cancel" button, not coded to anything yet
cancel.pack(side=tk.LEFT)
fB.pack()

window.mainloop() #s tarts event loop and displays window
