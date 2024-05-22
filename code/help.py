from tkinter import *
import time
from datetime import timedelta

def delete():
    screen1.destroy()
def delete1():
    screen2.destroy()


def error():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry('150x90')
    screen1.title('Warning!')
    Label(screen1, text='All fields required', fg='red').pack()
    Button(screen1, text = 'OK', command=delete).pack()
def succes():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry('150x90')
    screen2.title('Warning!')
    Label(screen2, text='registration succes', fg='red').pack()
    Button(screen2, text='OK', command=delete1).pack()


# def register():
#     global reg_com
#     username_text = username.get()
#     password_text = password.get()
#     if username_text == '':
#         error()
#
#     elif password_text == '':
#         error()
#
#     else:
#         succes()
        # reg_com = Label(screen, text='Registration complete!', width=20)
        # reg_com.place(x=175, y=260)
        # user_entry.delete(0, END)
        # pass_entry.delete(0, END)



# screen = Tk()
# screen.geometry('500x500')
# screen.title('Python form validation')
#
# Label(text='Python Form Validation', fg='black', bg='grey', height='2', width='500').pack()
#
# Label(text='Username *').place(x=215, y=50)
# Label(text='Password *').place(x=215, y=130)
# username = StringVar()
# password = StringVar()
# user_entry = Entry(textvariable=username, width=17)
# pass_entry = Entry(textvariable=password, width=17)
# user_entry.place(x=195, y=90)
# pass_entry.place(x=195, y=170)
#
# Button(screen, text='Register', width=20, bg='grey', command=register).place(x=175, y=210)
#
#
# screen.mainloop()
