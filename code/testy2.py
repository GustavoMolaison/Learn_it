import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1920x1080')
root.configure(bg='black')

Frame1 = tk.Frame(root, bg = 'red', width=1000, height=500, padx = 25, pady = 25)
Frame1.pack()

root.mainloop()