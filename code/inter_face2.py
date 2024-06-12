import tkinter as tk

def Learn_button_com(importt = False):
            def back_button():
              frame_learn_button.destroy()

            small_f = ('Lionel Classic', 20)
            normal_f = ('Lionel Classic', 50)
            from inter_face import Learn_button_com2, frame_learn_button
            from mat_but_learnit import spanish_button_func 
            def spanish_but_fun2():
                frame_learn_button.forget()
                spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife')
            Learn_button_com2(frist_screen.root)
            frame_learn_button.pack()
            # frame_learn_button = tk.Frame(frist_screen.root)
            # frame_learn_button = tk.Frame(width= 1920, height=1080, padx = 25, pady = 25, bg = 'black')
            # frame_learn_button.propagate(False)
            # frame_learn_button.pack()

            latly_used_frame = tk.Frame(frame_learn_button, bg = 'gold')
            latly_used_frame.configure( width=400, height = 500, padx = 25, pady = 25)
            latly_used_frame.propagate(False)
            for i in range(0):
              latly_used_frame.columnconfigure(i, weight = 1, uniform = 'a')
            for i in range(4):
              latly_used_frame.rowconfigure(i, weight = 1, uniform = 'a')    
          
            spanish_button = tk.Button(latly_used_frame, text='Spanish connect!', bg='black', fg='orange', padx = 10, pady = 10, height=1, width=len('Spanish connect'), command= lambda: spanish_but_fun2())
            spanish_button.configure(font=small_f)
            spanish_button.grid(column = 1, row = 0)
          
            back_button = tk.Button(frame_learn_button, text = '<---', bg = 'black', fg='yellow', width=10, height=2, command = lambda: back_button() )
            back_button.place(x = 25, y = 950)

            latly_used = tk.Label(frame_learn_button, text = 'Latly used', bg='black', fg='gold',  height=1, width=len('Latly used'))
            latly_used.configure(font=normal_f)
            latly_used.place(y=140, x=1335)

            
            latly_used_frame.place(x = 1390, y = 250)
Learn_button_com()            