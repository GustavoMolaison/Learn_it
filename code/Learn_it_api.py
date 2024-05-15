from tkinter import *
def Learn_it_main():
    Ltm_screen = Tk()
    # Ltm_screen.configure(bg='black')
    # Ltm_screen.attributes('-fullscreen',True)
    Ltm_screen.title('LearnIt!')
    Ltm_screen.geometry('1920x1080')
    lil = ('Kozuka Mincho Pro M', 50, 'bold')
    Learn_it_label = Label(text='LearnIt!', bg='black', fg='yellow', height=2, width=10)
    Learn_it_label.configure(font=lil)
    Learn_it_label.place(y=0, x=725)
    Ltm_screen.mainloop()

Learn_it_main()
