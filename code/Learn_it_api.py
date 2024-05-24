from tkinter import *
import pickle
import asyncio

import time
global  clicked_buttons_count_eng, clicked_buttons_count_esp, previous_button, previous_eng_word, previous_esp_word, stay_green_esp, stay_green_eng
clicked_buttons_count_eng: int = 0
clicked_buttons_count_esp: int = 0
previous_button_esp = None
previous_button_eng = None
previous_eng_word = None
previous_esp_word = None
stay_green_eng=[]
stay_green_esp=[]
def nothing():
    pass
def clear():
    global previous_eng_word, previous_button_eng, previous_button, previous_button_esp, previous_esp_word
    previous_eng_word = None
    previous_button_eng = None
    previous_button = None
    previous_button_esp = None
    previous_esp_word = None




def spanish_button_func():
    def uncorrect():

         global clicked_buttons_count_eng, clicked_buttons_count_esp, previous_button, unknown_button_f,no_yellow, stay_green_eng
         print('xd')
         no_yellow = True
         unknown_button_f.config(fg='red')
         previous_button.config(fg='red')
         await asyncio.sleep(2)



         if not clicked_buttons_count_eng == 0:
             clicked_buttons_count_eng = clicked_buttons_count_eng - 1
         if not clicked_buttons_count_esp == 0:
             clicked_buttons_count_esp = clicked_buttons_count_esp - 1
         clear()
    def correct(f_unknown_word, sg_number, idiom):
        global clicked_buttons_count_eng,no_yellow, clicked_buttons_count_esp, stay_green_eng, stay_green_esp
        if unknown_word_f == f_unknown_word:
            print('xd')
            no_yellow = True
            if sg_number == 0:
             spanish_word0.config(fg='green', command=nothing)
             english_word0.config(fg='green', command=nothing)

            if sg_number == 1:
                spanish_word1.config(fg='green', command=nothing)
                english_word1.config(fg='green', command=nothing)

            if sg_number == 2:
                spanish_word2.config(fg='green', command=nothing)
                english_word2.config(fg='green', command=nothing)

            if sg_number == 3:
                spanish_word3.config(fg='green', command=nothing)
                english_word3.config(fg='green', command=nothing)

            if sg_number == 4:
                spanish_word4.config(fg='green', command=nothing)
                english_word4.config(fg='green', command=nothing)

            if not clicked_buttons_count_eng == 0:
                clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            if not clicked_buttons_count_esp == 0:
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1
            if idiom == 'eng':
                print('stay green' + str(sg_number))
                stay_green_eng.append('stay green' + str(sg_number))
            if idiom == 'esp':
                stay_green_esp.append('stay green' + str(sg_number))
            clear()
    def one_orange_english(f_previous_eng_word):
        global stay_green_eng, clicked_buttons_count_eng
        if f_previous_eng_word == 'house':
            if not 'stay green0' in stay_green_eng:
                english_word0.configure(fg='orange', command=lambda: button_connect_english(english_word0, 'house'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == 'for':
            if not 'stay green1' in stay_green_eng:
                english_word1.configure(fg='orange', command=lambda: button_connect_english(english_word1, 'for'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == 'same':
            if not 'stay green2' in stay_green_eng:
                english_word2.configure(fg='orange', command=lambda: button_connect_english(english_word2, 'same'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == 'go to bed':
            if not 'stay green3' in stay_green_eng:
                english_word3.configure(fg='orange', command=lambda: button_connect_english(english_word3, 'go to bed'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == 'wall':
            if not 'stay green4' in stay_green_eng:
                english_word4.configure(fg='orange', command=lambda: button_connect_english(english_word4, 'wall'))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
    def one_orange_esp(f_previous_esp_word):
        global stay_green_esp, clicked_buttons_count_esp
        if f_previous_esp_word == 'casa':
            if not 'stay green0' in stay_green_esp:
                spanish_word0.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word0, 'casa'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == 'para':
            if not 'stay green1' in stay_green_esp:
                spanish_word1.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word1, 'para'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == 'mismo':
            if not 'stay green2' in stay_green_esp:
                spanish_word2.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word2, 'mismo'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == 'acostar':
            if not 'stay green3' in stay_green_esp:
                spanish_word3.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word3, 'acostar'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == 'pared':
            if not 'stay green4' in stay_green_esp:
                spanish_word4.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word4, 'pared'))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1














    def button_connect_english(unknown_button, unknown_word):
        global clicked_buttons_count_eng, previous_eng_word, previous_button_eng, stay_green_eng, previous_button, button_check_english, previous_esp_word, unknown_word_f, clicked_buttons_count_esp, no_yellow, unknown_button_f
        correct_value = 0
        no_yellow = False
        button_check_english = str(unknown_button)
        unknown_button_f = unknown_button
        unknown_word_f = unknown_word
        clicked_buttons_count_eng = clicked_buttons_count_eng + 1
        clicked_buttons_count = clicked_buttons_count_eng + clicked_buttons_count_esp


        if clicked_buttons_count > 1:
            one_orange_english(str(previous_eng_word))
            try:
             if button_conections_dict[button_check_english] == button_check_spanish or button_conections_dict[button_check_spanish] == button_check_english:
              correct('house', 0, 'eng')
              correct('for', 1, 'eng')
              correct('same', 2,'eng')
              correct('go to bed', 3,'eng')
              correct('wall', 4,'eng')
             else:
                 uncorrect()
            except NameError:
                pass
            # if not button_conections_dict[button_check_english] == button_check_spanish and not button_conections_dict[button_check_spanish] == button_check_english:
            #     uncorrect('house', 0)
            #     uncorrect('for', 1)
            #     uncorrect('same', 2)
            #     uncorrect('go to bed', 3)
            #     uncorrect('wall', 4)



        previous_eng_word = str(unknown_word)
        previous_button_eng = str(unknown_button)
        previous_button = unknown_button

        def button_connect22(unknown_button2):
            global clicked_buttons_count_esp, clicked_buttons_count_eng, previous_button
            previous_button = None

            if not clicked_buttons_count_eng == 0:
             clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            unknown_button2.configure(bg='black', fg='orange', command=lambda:button_connect_english(unknown_button2, unknown_word))
        if no_yellow == False:
         unknown_button.configure(bg='black', fg='yellow', command=lambda:button_connect22(unknown_button))
    def button_connect_spanish(unknown_button, unknown_word):
        global clicked_buttons_count_esp, clicked_buttons_count_esp, previous_esp_word, previous_button_esp, stay_green_esp, previous_button, button_check_spanish, clicked_buttons_count_eng, unknown_button_f, no_yellow, unknown_word_f
        correct_value = 0
        no_yellow = False
        unknown_button_f = unknown_button
        unknown_word_f = unknown_word
        button_check_spanish = str(unknown_button)
        clicked_buttons_count_esp = clicked_buttons_count_esp + 1
        clicked_buttons_count = clicked_buttons_count_eng + clicked_buttons_count_esp


        if clicked_buttons_count > 1:
            one_orange_esp(previous_esp_word)

            try:
             if button_conections_dict[button_check_english] == button_check_spanish or button_conections_dict[button_check_spanish] == button_check_english:
                 correct('casa', 0, 'esp')
                 correct('para', 1, 'esp')
                 correct('mismo', 2, 'esp')
                 correct('acostar', 3, 'esp')
                 correct('pared', 4, 'esp')
             else:
                 uncorrect()
            except NameError:
                pass
            # if not button_conections_dict[button_check_english] == button_check_spanish and not button_conections_dict[button_check_spanish] == button_check_english:
            #
            #     uncorrect('casa', 0)
            #     uncorrect('para', 1)
            #     uncorrect('mismo', 2)
            #     uncorrect('acostar', 3)
            #     uncorrect('pared', 4)

        previous_esp_word = str(unknown_word)
        previous_button_esp = str(unknown_button)
        previous_button = unknown_button

        def button_connect2(unknown_button2):
            global clicked_buttons_count_esp, clicked_buttons_count_eng, previous_button
            previous_button = None
            if not clicked_buttons_count_esp == 0:
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1

            unknown_button2.configure(bg='black', fg='orange', command=lambda:button_connect_spanish(unknown_button2, unknown_word))
        if no_yellow == False:
         unknown_button.configure(bg='black', fg='yellow', command=lambda:button_connect2(unknown_button))


    Learn_it_label.destroy()
    spanish_button.destroy()
    spanish_word0 = Button(text='casa', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect_spanish(spanish_word0, 'casa'))
    spanish_word0.place(y=200, x=150)
    spanish_word1 = Button(text='para', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect_spanish(spanish_word1, 'para'))
    spanish_word1.place(y=350, x=150)
    spanish_word2 = Button(text='mismo', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect_spanish(spanish_word2, 'mismo'))
    spanish_word2.place(y=500, x=150)
    spanish_word3 = Button(text='acostar', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect_spanish(spanish_word3, 'acostar'))
    spanish_word3.place(y=650, x=150)
    spanish_word4 = Button(text='pared', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect_spanish(spanish_word4, 'pared'))
    spanish_word4.place(y=800, x=150)

    english_word0 = Button(text='house', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect_english(english_word0, 'house'))
    english_word0.place(y=200, x=750)
    english_word1 = Button(text='for', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect_english(english_word1, 'for'))
    english_word1.place(y=350, x=750)
    english_word2 = Button(text='same', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect_english(english_word2, 'same'))
    english_word2.place(y=500, x=750)
    english_word3 = Button(text='go to bed', bg='black', fg='orange', height=1, width=10, font=basic_f,command=lambda:button_connect_english(english_word3, 'go to bed'))
    english_word3.place(y=650, x=750)
    english_word4 = Button(text='wall', bg='black', fg='orange', height=1, width=10, font=basic_f, command=lambda:button_connect_english(english_word4, 'wall'))
    english_word4.place(y=800, x=750)
    def con():
            print('esp ' + str(clicked_buttons_count_esp) + ' eng' + str(clicked_buttons_count_eng) + ' stay green:' + str(stay_green_eng))
    button_conections_dict = {'.!button2':'.!button7','.!button7':'.!button2','.!button3':'.!button8','.!button8':'.!button3','.!button4':'.!button9','.!button9':'.!button4','.!button5':'.!button10','.!button10':'.!button5','.!button6':'.!button11', '.!button11':'.!button6'}
    continue_button = Button(text='continue', bg='black', fg='yellow', font=basic_f, command = con)
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
