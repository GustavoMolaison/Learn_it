from tkinter import *




class menu:
 def __init__(self, root = None, back_or_not = 0): 
    from mat_but_learnit import spanish_button_func 
    
    
    if back_or_not == 0:
       self.Ltm_screen = Tk()
       self.Ltm_screen.title('LearnIt!')
       self.Ltm_screen.geometry('1920x1080')
       self.Ltm_screen.configure(bg='black')
       
    self.lil_f = ('Kozuka Mincho Pro M', 50, 'bold')
    self.basic_f = ('Lionel Classic', 50)
    self.Learn_it_label = Label(root, text='LearnIt!', bg='black', fg='yellow', height=2, width=10)
    self.Learn_it_label.configure(font=self.lil_f)
    self.Learn_it_label.place(y=0, x=725)
    self.spanish_button = Button(root, text='Spanish connect!', bg='black', fg='orange', height=1, width=len('Spanish connect'), command= lambda: spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife'))
    self.spanish_button.configure(font=self.basic_f)
    self.spanish_button.place(y=160, x=1400)


    self.Ltm_screen.mainloop()

Ltm_screen = Tk()
Ltm_screen.title('LearnIt!')
Ltm_screen.geometry('1920x1080')
Ltm_screen.configure(bg='black')
menu(Ltm_screen)
Ltm_screen.mainloop()
