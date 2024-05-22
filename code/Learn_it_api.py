from tkinter import *
import pickle
global  clicked_buttons_count_eng, clicked_buttons_count_esp, previous_button, stay_green
clicked_buttons_count_eng: int = 0
clicked_buttons_count_esp: int = 0
previous_button_esp = None
previous_button_eng = None
stay_green=[]
def nothing():
    pass
def spanish_button_func():
    global button_connect
    def button_connect(unknown_button, unknown_word, clicked_buttons_pickle = []):
        global clicked_buttons_count_eng, clicked_buttons_count_esp, previous_esp_word, previous_eng_word, previous_button_esp, previous_button_eng,stay_green, previous_button
        correct_value = 0
        no_yellow = False

        if unknown_button == spanish_word0 or unknown_button == spanish_word1 or unknown_button == spanish_word2 or unknown_button == spanish_word3 or unknown_button == spanish_word4:
            clicked_buttons_count_esp = clicked_buttons_count_esp + 1
        if unknown_button == english_word0 or unknown_button == english_word1 or unknown_button == english_word2 or unknown_button == english_word3 or unknown_button == english_word4:
            clicked_buttons_count_eng = clicked_buttons_count_eng + 1

        if clicked_buttons_count_esp > 1:

            if previous_esp_word == 'casa':
                if not 'stay green1' in stay_green:
                 spanish_word0.configure( fg='orange', command=lambda:button_connect(spanish_word0, 'casa'))
                 if not clicked_buttons_count_esp == 0:
                     clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'para':
                if not 'stay green2' in stay_green:
                 spanish_word1.configure(fg='orange', command=lambda: button_connect(spanish_word1, 'para'))
                 if not clicked_buttons_count_esp == 0:
                     clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'mismo':
                if not 'stay green3' in stay_green:
                 spanish_word2.configure(fg='orange', command=lambda: button_connect(spanish_word2,'mismo'))
                 if not clicked_buttons_count_esp == 0:
                     clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'acostar':
                if not 'stay green4' in stay_green:
                 spanish_word3.configure(fg='orange', command=lambda: button_connect(spanish_word3, 'acostar'))
                 if not clicked_buttons_count_esp == 0:
                     clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if previous_esp_word == 'pared':
                if not 'stay green5' in stay_green:
                 spanish_word4.configure(fg='orange', command=lambda: button_connect(spanish_word4, 'pared'))
                 if not clicked_buttons_count_esp == 0:
                     clicked_buttons_count_esp = clicked_buttons_count_esp - 1

        if clicked_buttons_count_eng > 1:
            if previous_eng_word == 'house':
                if not 'stay green1' in stay_green:
                 english_word0.configure( fg='orange', command=lambda:button_connect(english_word0, 'house'))
                 if not clicked_buttons_count_eng == 0:
                     clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'for':
                if not 'stay green2' in stay_green:
                 english_word1.configure(fg='orange', command=lambda: button_connect(english_word1, 'for'))
                 if not clicked_buttons_count_eng == 0:
                     clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'same':
                if not 'stay green3' in stay_green:
                 english_word2.configure(fg='orange', command=lambda: button_connect(english_word2, 'same'))
                 if not clicked_buttons_count_eng == 0:
                     clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'go to bed':
                if not 'stay green4' in stay_green:
                 english_word3.configure(fg='orange', command=lambda: button_connect(english_word3,'go to bed'))
                 if not clicked_buttons_count_eng == 0:
                     clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if previous_eng_word == 'wall':
                if not 'stay green5' in stay_green:
                 english_word4.configure(fg='orange', command=lambda: button_connect(english_word4, 'wall'))
                 if not clicked_buttons_count_eng == 0:
                     clicked_buttons_count_eng = clicked_buttons_count_eng - 1


        if clicked_buttons_count_eng + clicked_buttons_count_esp > 1:
          if  previous_button_esp == button_conections_dict[str(unknown_button)] or previous_button_eng == button_conections_dict[str(unknown_button)]:
             correct_value = 1
          else:
              previous_button.config(bg='orange', fg='red')
              unknown_button.config(bg='orange', fg='red')
              no_yellow = True




        if correct_value == 1:
            if unknown_word == 'casa' or unknown_word == 'house':
                no_yellow = True
                stay_green.append('stay green1')
                spanish_word0.config(fg='green', command=nothing)
                english_word0.config(fg='green', command=nothing)
                clicked_buttons_count_eng = clicked_buttons_count_eng - 1
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1

            elif unknown_word == 'para' or unknown_word == 'for':
                no_yellow = True
                stay_green.append('stay green2')
                spanish_word1.configure(fg='green', command=nothing)
                english_word1.configure(fg='green', command=nothing)
                clicked_buttons_count_eng = clicked_buttons_count_eng - 1
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1

            elif unknown_word == 'mismo' or unknown_word == 'same':
                no_yellow = True
                stay_green.append('stay green3')
                spanish_word2.configure(fg='green', command=nothing)
                english_word2.configure(fg='green', command=nothing)
                clicked_buttons_count_eng = clicked_buttons_count_eng - 1
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1

            elif unknown_word == 'acostar' or unknown_word == 'go to bed':
                no_yellow = True
                stay_green.append('stay green4')
                spanish_word3.configure(fg='green', command=nothing)
                english_word3.configure(fg='green', command=nothing)
                clicked_buttons_count_eng = clicked_buttons_count_eng - 1
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1

            elif unknown_word == 'pared' or unknown_word == 'wall':
                no_yellow = True
                stay_green.append('stay green5')
                spanish_word4.configure(fg='green', command=nothing)
                english_word4.configure(fg='green', command=nothing)
                clicked_buttons_count_eng = clicked_buttons_count_eng - 1
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1

        if unknown_button == spanish_word0 or unknown_button == spanish_word1 or unknown_button == spanish_word2 or unknown_button == spanish_word3 or unknown_button == spanish_word4:
            previous_esp_word = None
            previous_esp_word = str(unknown_word)
            previous_button_esp = str(unknown_button)
        if unknown_button == english_word0 or unknown_button == english_word1 or unknown_button == english_word2 or unknown_button == english_word3 or unknown_button == english_word4:
            previous_eng_word = None
            previous_eng_word = str(unknown_word)
            previous_button_eng = str(unknown_button)
        previous_button = unknown_button

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

    button_conections_dict = {'.!button2':'.!button7','.!button7':'.!button2','.!button3':'.!button8','.!button8':'.!button3','.!button4':'.!button9','.!button9':'.!button4','.!button5':'.!button10','.!button10':'.!button5','.!button6':'.!button11', '.!button6':'.!button11'}
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
