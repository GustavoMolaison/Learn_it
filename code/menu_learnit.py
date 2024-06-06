from tkinter import *
from mat_but_learnit import spanish_button_func







def Learn_it_main(back_or_not = 0): 
    global Learn_it_label, spanish_button, basic_f, Ltm_screen 
     

    global Learn_it_label, spanish_button, basic_f, Ltm_screen
    if back_or_not == 0:
       Ltm_screen = Tk()
       Ltm_screen.title('LearnIt!')
       Ltm_screen.geometry('1920x1080')
       Ltm_screen.configure(bg='black')
       
    lil_f = ('Kozuka Mincho Pro M', 50, 'bold')
    basic_f = ('Lionel Classic', 50)
    Learn_it_label = Label(text='LearnIt!', bg='black', fg='yellow', height=2, width=10)
    Learn_it_label.configure(font=lil_f)
    Learn_it_label.place(y=0, x=725)
    spanish_button = Button(text='Spanish connect!', bg='black', fg='orange', height=1, width=len('Spanish connect'), command= lambda: spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife'))
    spanish_button.configure(font=basic_f)
    spanish_button.place(y=160, x=1400)


    Ltm_screen.mainloop()

Learn_it_main()