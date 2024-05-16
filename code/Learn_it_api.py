from tkinter import *

def spanish_button_func():
    global button_connect

    def button_connect(unknown_button, unknown_word):
        def button_connect2(unknown_button2):
            unknown_button2.configure(text=unknown_word, bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(unknown_button2, unknown_word))
        unknown_button.configure(bg='black', fg='yellow', command=lambda:button_connect2(unknown_button))


    Learn_it_label.destroy()
    spanish_button.destroy()
    spanish_word0 = Button(text='casa', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(spanish_word0, 'casa'))
    spanish_word0.place(y=200, x=150)
    spanish_word1 = Button(text='para', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    spanish_word1.place(y=350, x=150)
    spanish_word2 = Button(text='mismo', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    spanish_word2.place(y=500, x=150)
    spanish_word3 = Button(text='acostar', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    spanish_word3.place(y=650, x=150)
    spanish_word4 = Button(text='pared', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    spanish_word4.place(y=800, x=150)
    english_word0 = Button(text='house', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    english_word0.place(y=200, x=750)
    english_word1 = Button(text='for', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    english_word1.place(y=350, x=750)
    english_word2 = Button(text='same', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    english_word2.place(y=500, x=750)
    english_word3 = Button(text='go to bed', bg='black', fg='orange', height=1, width=10, font=basic_f, )
    english_word3.place(y=650, x=750)
    english_word4 = Button(text='wall', bg='black', fg='orange', height=1, width=10, font=basic_f)
    english_word4.place(y=800, x=750)

    continue_button = Button(text='continue', bg='black', fg='yellow', font=basic_f)
    continue_button.place(y=800, x=1500)






def Learn_it_main():
    global Learn_it_label, spanish_button, basic_f
    Ltm_screen = Tk()
    # Ltm_screen.configure(bg='black')
    # Ltm_screen.attributes('-fullscreen',True)
    Ltm_screen.title('LearnIt!')
    Ltm_screen.geometry('1920x1080')
    Ltm_screen.configure(bg='black')
    lil_f = ('Kozuka Mincho Pro M', 50, 'bold')
    basic_f = ('Lionel Classic', 50)

    Learn_it_label = Label(text='LearnIt!', bg='black', fg='yellow', height=2, width=10)
    Learn_it_label.configure(font=lil_f)
    Learn_it_label.place(y=0, x=725)
    spanish_button = Button(text='Spanish!', bg='black', fg='orange', height=1, width=len('Spanish!'), command=spanish_button_func)
    spanish_button.configure(font=basic_f)
    spanish_button.place(y=160, x=1600)


    Ltm_screen.mainloop()

Learn_it_main()
