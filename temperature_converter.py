import tkinter as tk
from tkinter import *
window = Tk()

window.geometry("750x500") #Setting screen size (width,height)
window.title("Temperature Converter")

c_input = StringVar()
f_input = StringVar()
results = StringVar()

#Functions


#Entry widget
c_entry= Entry(window, textvariable=c_input, state=DISABLED)
f_entry = Entry(window, textvariable=f_input, state=DISABLED)

#Label
results_label = Label(window, textvariable=results, bg="green", width=35, height=10 )
celcius_to_farenheid_label = Label(window, text="Celcius To Farenheidt", state=DISABLED)
farenheid_to_celcius_label = Label(window, text="Farenheidt To Celcius", state=DISABLED )

#Button widgets
#Activation Buttons
activate_c_button = Button(window, text="Activate Celcius to Farenheidt Converter")
activate_f_button = Button(window, text="Activate Farenheidt to Celcius Converter")

#Calculation Button
calc_conversion_button = Button(window, text="Calculating Conversion")

#Exit and Clear Buttons
exit_button = Button(window, text="Exit")
clear_button = Button(window, text="Clear")

#placing widgets
celcius_to_farenheid_label.place(x=250, y=100)
farenheid_to_celcius_label.place(x=500, y=100)

f_entry.place(x=250, y=150)
c_entry.place(x=500, y=150)
results_label.place(x=300, y=300)
calc_conversion_button.place()
clear_button.place(x=600, y=300)
exit_button.place(x=600, y=350)

window.mainloop()