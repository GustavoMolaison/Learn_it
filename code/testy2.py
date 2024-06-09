import tkinter as tk
from tkinter import ttk
def destr():
    screen1.withdraw() 
screen1 = tk.Tk()
screen1.geometry('500x500')
but = tk.Button(screen1, text = 'destroy', command = destr ) 
but.pack()
screen1.mainloop()
destr()
