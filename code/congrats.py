import tkinter as tk

def interwal():
    # from menu_learnit import csb
    congrats_frame.forget()
    csb(importt = True)

normal_f = ('Lionel Classic', 50)
normal_f2 = ('Lionel Classic', 100)
congrats_frame = tk.Frame( bg = 'black', width= 1920, height=1080)
congrats_label = tk.Label(text = 'good job!', width= len('good job') , height=1, fg = 'yellow', bg = 'black')
congrats_button = tk.Button(text = 'Thanks', width=len('Thanks'), height = 1, fg = 'orange', bg = 'black', command= lambda: interwal())
congrats_label.config(font = normal_f2)
congrats_button.config(font = normal_f)
congrats_label.place(x = 650, y = 200)
congrats_button.place(x = 840, y = 700)

congrats_frame.pack()
congrats_frame.mainloop()

