print('Welcome to LearnIt!')
import pickle
from tkinter import *



def usernamepass_def(x, y):
    if backer == 1:
        return

    def username_def(q):
        global backer
        backer = 0
        global username2
        global z
        print('Go back')
        print(f'Pick your username:', end=' ')
        z = input()
        if z == 'Go back' or z == 'go back' or z == 'gb':
            backer = 1
            return
        if len(z) < q:
            print(f'username have to be made at least from {q} letters')
            username_def(q)

        with open('usernames_and_passwords', 'rb') as file:
            username_and_password = pickle.load(file)
        if z in username_and_password.keys():
            print('Sadly this name is occupied by another user, pick diffrent one!')
            username_def(q)
        username2 = str(z)

    def password_def(q):
        luz = True
        global password2
        big_letter = 0
        print('Go back')
        print(f'Pick your password:', end=' ')
        z = input()
        if z == 'Go back' or z == 'go back' or z == 'gb':
            username_def(3)
            usernamepass_def('password', 6)
            luz = False

        if luz:
            if len(z) < q:
                print(f'password have to be made at least from {q} letters')
                password_def(q)

            test_x = str(z)
            for smt in test_x:
                if smt.isupper():
                    big_letter += 1
            if big_letter < 1:
                print('Password must contain at least one big letter')
                password_def(q)
            if big_letter >= 1:
                m = 0
                for pan in test_x:
                    special_character = ['!', '@', "#", "$", '%', '^', '&', "*", "(", ')', '-', '_', '=', '+', '/', "?",
                                         '>', '<', "`"]
                    if pan in special_character:
                        m = True

                if m:
                    with open('usernames_and_passwords', 'rb') as file:
                        username_and_password = pickle.load(file)
                    if test_x in username_and_password.values():
                        print('Sadly this password is occupied by another user, pick diffrent one!')
                        password_def(q)
                    else:
                        password2 = str(z)
                if not True == m:
                    print('Password must contain at least one special character')
                    password_def(q)

    if x == 'username':
        username_def(y)
    if x == 'password':
        password_def(y)


def registration():
    global backer
    backer = 0
    print('Welcome to Calorie Counter!\n')
    usernamepass_def('username', 3)
    if backer == 1:
        return
    usernamepass_def('password', 6)
    with open('usernames_and_passwords', 'rb') as file:
        username_and_password = pickle.load(file)
    username_and_password[username2] = password2
    with open('usernames_and_passwords', 'wb') as file:
        pickle.dump(username_and_password, file)
    print('Account created succesfully, thanks!\n')


def login():
    global backer
    backer = 0
    global username
    global password

    def give_username():
        global backer
        global username
        global password
        print('Username:')
        print('go back')
        username = input()
        if username == 'go back' or username == 'gb':
            backer = 1
            return

    def give_password():
        global backer
        global username
        global password
        print('password:')
        password = input()
        if password == 'go back' or password == 'gb':
            backer = 1
            return

    def remberme():
        global rem
        print('Rememmber you?')
        rem = input()
        if rem != 'yes' and rem != 'y' and rem != 'no' and rem != 'n':
            remberme()

    def give_logs():
        global backer
        global username
        global password
        global backer
        global dont_log
        global pararacordarme
        print('Welcome to Calorie Counter!')
        print('Username:')
        username = input()
        if username == 'go back' or username == 'gb':
            backer = 1
            return
        print('Password:')
        password = input()
        if password == 'go back' or password == 'gb':
            backer = 1
            return

    def login_in_login():
        global backer
        global dont_log
        global pararacordarme
        with open('usernames_and_passwords', 'rb') as file:
            username_and_password = pickle.load(file)
        if username in username_and_password.keys():
            print('correct username')
            if username_and_password[username] == password:
                print('correct password')
                # with open('diet', 'rb') as file:
                #     udict = pickle.load(file)
                # if not username in udict.keys():
                #     new_user_package(str(username))
                print('Rememmber your password and username? (yes/no)')
                rem = input().lower()
                if rem != 'yes' and rem != 'y' and rem != 'no' and rem != 'n':
                    remberme()
                if rem == 'yes' or rem == 'y':
                    dont_log = True
                    with open('dont_log_file', 'wb') as file:
                        pickle.dump(dont_log, file)
                    recordarme = [username]
                    with open('recordarme_file', 'wb') as file:
                        pickle.dump(recordarme, file)
                if rem == 'no' or rem == 'n':
                    dont_log = False
                from Learn_it_api import calorie_shedule
                calorie_shedule(str(username))
                backer = 1
                dont_log = False
                with open('dont_log_file', 'wb') as file:
                    pickle.dump(dont_log, file)
                return
            else:
                print('incorect password')
                give_password()
                if backer == 1:
                    return
                login_in_login()
        else:
            print('incorect username')
            give_username()
            if backer == 1:
                return
            login_in_login()

    if backer == 1:
        return
    give_logs()
    if backer == 1:
        return
    login_in_login()
    if backer == 1:
        return


def wtd_try():
    global wtd
    print('login', end='')
    print('  registration', end='')
    print('  quit')
    wtd = input().lower()
    if wtd == 'quit':
        quit()
    if wtd != 'login' and wtd != 'log' and wtd != 'registration' and wtd != 'reg' and wtd != 'quit':
        wtd_try()


def entering():
    global pararacordarme
    global backer
    global wtd
    global dont_log
    backer = 0
    print('           Hello!\n')
    print('login', end='')
    print('  registration', end='')
    print('  quit')
    wtd = input().lower()
    if wtd != 'login' and wtd != 'log' and wtd != 'registration' and wtd != 'reg' and wtd != 'quit':
        wtd_try()
    if wtd == 'quit':
        quit
    if wtd == 'login' or wtd == 'log':
        with open('dont_log_file', 'rb') as file:
            dont_log = pickle.load(file)
        if dont_log:
            with open('recordarme_file', 'rb') as file:
                recordarme = pickle.load(file)
            username = recordarme[0]
            # from CALORIECOUNTERNOWAY import calorie_shedule
            # calorie_shedule(str(username))
            dont_log = False
            with open('dont_log_file', 'wb') as file:
                pickle.dump(dont_log, file)
            backer = 1
            entering()
        if not dont_log:
            login()
        if backer == 1:
            backer = 0
            entering()

    if wtd == 'registration' or wtd == 'reg':
        registration()
        backer = 0
        entering()
# def run():
#     new_text = Label(text = 'you just clicked me', fg = 'yellow', bg = 'black')
#     new_text.place(x = 195, y = 230)
# def run2():
#     name1 = name_storage.get()
#     print(name1)
#     name.delete(0, END)
#
# screen = Tk()
# screen.title("Learn_It!")
# screen.geometry("500x500")
# welcome_text = Label(text='Welcome to Learn_It!', fg='yellow', bg='black')
# welcome_text.pack()
# click_me = Button(text='Click me', fg='orange', bg='black', height = 2, width = 7, command = run2)
# click_me.place(x = 10, y = 20)
#
# name_storage = StringVar()
# name = Entry(textvariable= name_storage)
# name.pack()
# screen.mainloop()
entering()
