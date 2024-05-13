from tkinter import *
import pickle


def login_error(le_variable):
    error_screen = Toplevel(screen)
    error_screen.geometry('150x90')
    error_screen.title('error')
    # Label(error_screen, bg='black', height=500, width=500).pack()
    Label(error_screen, text=f'{le_variable}', fg='black').pack()


def login():
    username_text = username.get()
    password_text = password.get()
    if username_text == '':
        login_error('Fill every necessary gap')
    elif password_text == '':
        login_error('Fill every necessary gap')
    else:
        with open('usernames_and_passwords', 'rb') as file:
            username_and_password = pickle.load(file)
            if not username_text in username_and_password.keys() and not password_text in username_and_password.values():
                login_error('incorrect username and password')
            elif not username_text in username_and_password.keys():
                login_error('incorrect username')
            elif not username_and_password[username_text] == password_text:
                login_error('incorrect password')
            else:
                print('you loged in')


def gb():
    screen.destroy()
    login_screen()
    # global backer
    # backer = 1
    # return()


def registration():
    global len_error
    with open('usernames_and_passwords', 'rb') as file:
        username_and_password = pickle.load(file)
    username_text = str(username.get())
    password_text = str(password.get())
    if not len(username_text) >= 3:
        len_error = Label(text='username must contain at least 3 letters', fg='white', bg='black', height=2,
                          width=len('username must contain at least 3 letters'))
        len_error.place(x=400, y=120)
    elif username_text in username_and_password.keys():
        len_error = Label(text='Sadly this username is occupied by another user', fg='white', bg='black', height=2,
                          width=len('Sadly username is occupied by another user'))
        len_error.place(x=400, y=120)
    else:
        if password_text in username_and_password.values():
            len_error = Label(text='Sadly this password is occupied by another user', fg='white', bg='black', height=2,
                              width=len('Sadly this password is occupied by another user'))
            len_error.place(x=400, y=120)
        elif not len(password_text) >= 6:
            len_error = Label(text='password must contain at least 6 letters', fg='white', bg='black', height=2,
                              width=len('password must contain at least 6 letters'))
            len_error.place(x=400, y=120)
        m = False
        if True:
            for pan in password_text:
                special_character = ['!', '@', "#", "$", '%', '^', '&', "*", "(", ')', '-', '_', '=', '+', '/', "?",
                                     '>', '<', "`"]
                if pan in special_character:
                    m = True
            if m:
                username_and_password[username_text] = password_text
                with open('usernames_and_passwords', 'wb') as file:
                    pickle.dump(username_and_password, file)
                len_error = Label(text='Registration complete!', fg='white', bg='black',
                                  height=2, width=len('Registration complete!'))
                Button(text='Go back?', fg='black', bg='grey', command=gb).place(x=500, y=120)
            else:
                len_error = Label(text='password must contain at least 1 special character', fg='white', bg='black',
                                  height=2, width=len('password must contain at least 1 special character'))
                len_error.place(x=400, y=120)


def register():
    login_button.destroy()
    reg_button = Button(screen, text='registration', width=20, bg='black', fg='yellow', command=registration)
    reg_button.place(x=465, y=320)
    goback_button = Button(screen, text='go back', bg='black', fg='yellow', width=15, command=gb)
    goback_button.place(x=480, y=360)


def login_screen():
    global screen, password, username, login_button, reg_button
    screen = Tk()
    screen.geometry('1000x500')
    screen.title('Python form validation')
    Label(bg='black', height=500, width=500).pack()

    Label(text='Python Form Validation', fg='black', bg='grey', height='2', width='500').pack()

    Label(text='Username *', fg='white', bg='black', height=2, width=25).place(x=450, y=160)
    Label(text='Password *', fg='white', bg='black', height=2, width=25).place(x=450, y=240)
    username = StringVar()
    password = StringVar()
    user_entry = Entry(textvariable=username, width=17, bg='white')
    pass_entry = Entry(textvariable=password, width=17, bg='white')
    user_entry.place(x=485, y=200)
    pass_entry.place(x=485, y=280)

    login_button = Button(screen, text='login', width=20, bg='black', fg='yellow', command=login)
    reg_button = Button(screen, text='registration', width=20, bg='black', fg='yellow', command=register)
    login_button.place(x=465, y=320)
    reg_button.place(x=465, y=360)
    screen.mainloop()


login_screen()
