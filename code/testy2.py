import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Nie wierze')
root.geometry('1920x1080')
root.configure(bg='black')
 
from testy3 import xd, Frame1


def xa():
#  for widget in Frame1.winfo_children():
#                  widget.destroy()
 Frame1.destroy()
 root.configure(bg='black')


xd(root)
Frame1.pack()

but = tk.Button(Frame1, text = 'nice', width=50, height = 5, command = lambda: xa()) 
but.pack()
lael11 = tk.Label(Frame1, text = 'wow', bg = 'purple', width=230, height = 50)
lael11.pack()


root.mainloop()








# usefull staff

#  for widget in self.latly_used_frame.winfo_children():
              #    widget.destroy()