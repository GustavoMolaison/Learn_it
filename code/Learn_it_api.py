from tkinter import *
import pickle
global  clicked_buttons_count_eng, clicked_buttons_count_esp, previous_button
clicked_buttons_count_eng: int = 0
clicked_buttons_count_esp: int = 0
previous_button = None
def spanish_button_func():
    global button_connect
    def button_connect(unknown_button, unknown_word, clicked_buttons_pickle = []):
        global clicked_buttons_count_eng, clicked_buttons_count_esp, previous_esp_word, previous_eng_word, previous_button
        correct_value = 0
        no_yellow = False

        if unknown_button == spanish_word0 or unknown_button == spanish_word1 or unknown_button == spanish_word2 or unknown_button == spanish_word3 or unknown_button == spanish_word4:
            clicked_buttons_count_esp = clicked_buttons_count_esp + 1
        if unknown_button == english_word0 or unknown_button == english_word1 or unknown_button == english_word2 or unknown_button == english_word3 or unknown_button == english_word4:
            clicked_buttons_count_eng = clicked_buttons_count_eng + 1

        if clicked_buttons_count_esp > 1:

            if previous_esp_word == 'casa':
                spanish_word0.configure( fg='orange', command=lambda:button_connect(spanish_word0, 'casa'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'para':
                spanish_word1.configure(fg='orange', command=lambda: button_connect(spanish_word1, 'para'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'mismo':
                spanish_word2.configure(fg='orange', command=lambda: button_connect(spanish_word2,'mismo'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'acostar':
                spanish_word3.configure(fg='orange', command=lambda: button_connect(spanish_word3, 'acostar'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'pared':
                spanish_word4.configure(fg='orange', command=lambda: button_connect(spanish_word4, 'pared'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1

        if clicked_buttons_count_eng > 1:
            if previous_eng_word == 'house':
                english_word0.configure( fg='orange', command=lambda:button_connect(english_word0, 'house'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'for':
                english_word1.configure(fg='orange', command=lambda: button_connect(english_word1, 'for'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'same':
                english_word2.configure(fg='orange', command=lambda: button_connect(english_word2, 'same'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'go to bed':
                english_word3.configure(fg='orange', command=lambda: button_connect(english_word3,'go to bed'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'wall':
                english_word4.configure(fg='orange', command=lambda: button_connect(english_word4, 'wall'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1



        try:
         print(unknown_word)
         print(previous_button)
         if  previous_button == button_conections_dict[str(unknown_button)]:
             print('dziala')
             correct_value = 1
        except KeyError:
         try:
          print('2')
          if str(unknown_button) == button_conections_dict[previous_button]:
             print('dziala')
             correct_value = 1
         except KeyError:
             print('3')
             pass
        # except UnboundLocalError:
        #     print('undounderrior')
        #     pass
        if correct_value == 1:
            if unknown_word == 'casa' or unknown_word == 'house':
                no_yellow = True
                spanish_word0.configure(fg='green', command=None)
                english_word0.configure(fg='green', command=None)

            elif unknown_word == 'para' or unknown_word == 'for':
                no_yellow = True
                spanish_word1.configure(fg='purple', command=None)
                english_word1.configure(fg='purple', command=None)

            elif unknown_word == 'mismo' or unknown_word == 'same':
                no_yellow = True
                spanish_word2.configure(fg='purple', command=None)
                english_word2.configure(fg='purple', command=None)

            elif unknown_word == 'acostar' or unknown_word == 'go to bed':
                no_yellow = True
                spanish_word3.configure(fg='purple', command=None)
                english_word3.configure(fg='purple', command=None)

            elif unknown_word == 'pared' or unknown_word == 'wall':
                no_yellow = True
                spanish_word4.configure(fg='purple', command=None)
                english_word4.configure(fg='purple', command=None)

        if unknown_button == spanish_word0 or unknown_button == spanish_word1 or unknown_button == spanish_word2 or unknown_button == spanish_word3 or unknown_button == spanish_word4:
            previous_esp_word = None
            previous_esp_word = str(unknown_word)

        if unknown_button == english_word0 or unknown_button == english_word1 or unknown_button == english_word2 or unknown_button == english_word3 or unknown_button == english_word4:
            previous_eng_word = None
            previous_eng_word = str(unknown_word)

        previous_button = str(unknown_button)
        def button_connect2(unknown_button2):
            global clicked_buttons_count_esp, clicked_buttons_count_eng, previous_button
            previous_button = None
            if not clicked_buttons_count_esp == 0:
             if unknown_button == spanish_word0 or unknown_button == spanish_word1 or unknown_button == spanish_word2 or unknown_button == spanish_word3 or unknown_button == spanish_word4:
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1
             if not clicked_buttons_count_eng == 0:
              if unknown_button == english_word0 or unknown_button == english_word1 or unknown_button == english_word2 or unknown_button == english_word3 or unknown_button == english_word4:
                clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            unknown_button2.configure(bg='black', fg='orange', command=lambda:button_connect(unknown_button2, unknown_word))
        if no_yellow == False:
         unknown_button.configure(bg='black', fg='yellow', command=lambda:button_connect2(unknown_button))


    Learn_it_label.destroy()
    spanish_button.destroy()
    spanish_word0 = Button(text='casa', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(spanish_word0, 'casa'))
    spanish_word0.place(y=200, x=150)
    spanish_word1 = Button(text='para', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(spanish_word1, 'para'))
    spanish_word1.place(y=350, x=150)
    spanish_word2 = Button(text='mismo', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(spanish_word2, 'mismo'))
    spanish_word2.place(y=500, x=150)
    spanish_word3 = Button(text='acostar', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(spanish_word3, 'acostar'))
    spanish_word3.place(y=650, x=150)
    spanish_word4 = Button(text='pared', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(spanish_word4, 'pared'))
    spanish_word4.place(y=800, x=150)
    english_word0 = Button(text='house', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect(english_word0, 'house'))
    english_word0.place(y=200, x=750)
    english_word1 = Button(text='for', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect(english_word1, 'for'))
    english_word1.place(y=350, x=750)
    english_word2 = Button(text='same', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect(english_word2, 'same'))
    english_word2.place(y=500, x=750)
    english_word3 = Button(text='go to bed', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect(english_word3, 'go to bed'))
    english_word3.place(y=650, x=750)
    english_word4 = Button(text='wall', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(english_word4, 'wall'))
    english_word4.place(y=800, x=750)

    button_conections_dict = {'.!button2':'.!button7','.!button3':'.!button8','.!button4':'.!button9','.!button5':'.!button10','.!button6':'.!button11'}
    continue_button = Button(text='continue', bg='black', fg='yellow', font=basic_f)
    continue_button.place(y=800, x=1500)

    # if clicked_buttons_count > 1:
    #     print('dziala')
    #     with open('clicked_buttons_picklefile', 'rb') as file:
    #         clicked_buttons_pickle = pickle.load(file)
    #         butt_to_conf = clicked_buttons_pickle[0]
    #         clicked_buttons_pickle[0].configure(text=unknown_word, bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect(unknown_button2, unknown_word))






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
