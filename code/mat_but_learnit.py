import tkinter as tk
import random



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
    global previous_eng_word, previous_button_eng, previous_button, previous_button_esp, previous_esp_word, button_check_spanish, button_check_english
    previous_eng_word = None
    previous_button_eng = None
    previous_button= None
    previous_word = None
    previous_button_esp = None
    previous_esp_word = None
    button_check_spanish = None
    button_check_english = None


# BUTTONS CODE
    
def spanish_button_func(spanish_word0_world, english_word0_world, spanish_word1_world, english_word1_world, spanish_word2_world, english_word2_world, spanish_word3_world, english_word3_world, spanish_word4_world, english_word4_world):
  if __name__ == "mat_but_learnit": 
       

    
    

    # UNCORRECT MATCHES
    def uncorrect():
         
         #  COLOR RED EFFECT
         def color_red(whatever_button, whatever_word, func):
           whatever_button.after(1000, lambda: whatever_button.config(fg='orange',command=lambda: func(whatever_button, whatever_word)))
        ######
           
         global clicked_buttons_count_eng, clicked_buttons_count_esp, previous_button, unknown_button_f,no_yellow, unknown_word_f, stay_green_eng, previous_word, button_check_spanish, button_check_english
         no_yellow = True
         unknown_button_f.config(fg='red', command = nothing)
         previous_button.config(fg='red', command = nothing)
         if unknown_button_f in spanish_list:
             color_red(unknown_button_f, unknown_word_f, button_connect_spanish)
             color_red(previous_button, previous_word, button_connect_english)

         else:
             print(f'unknown_button_f { unknown_button_f} and previous_button { previous_button}.')
             color_red(unknown_button_f, unknown_word_f, button_connect_english)
             color_red(previous_button, previous_word, button_connect_spanish)

         if not clicked_buttons_count_eng == 0:
             clicked_buttons_count_eng = clicked_buttons_count_eng - 1
         if not clicked_buttons_count_esp == 0:
             clicked_buttons_count_esp = clicked_buttons_count_esp - 1
         clear()

    # CORRECT MATCHES 
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

            if len(stay_green_eng) == 5 or len(stay_green_esp) == 5:
               print('nom')
               continue_button.grid(column=4, row=4, padx = 30, pady= 30)
            clear()


    # COLORING KEEPING ONLY ONE BUTTON YELLOW ENG        
    def one_orange_english(f_previous_eng_word):
        global stay_green_eng, clicked_buttons_count_eng
        if f_previous_eng_word == english_word0_world:
            print('one_orange_english(line96)')
            if not 'stay green0' in stay_green_eng:
                english_word0.configure(fg='orange', command=lambda: button_connect_english(english_word0, english_word0_world))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == english_word1_world:
            print('line(105)')
            if not 'stay green1' in stay_green_eng:
                print('line(107)')
                english_word1.configure(fg='orange', command=lambda: button_connect_english(english_word1, english_word1_world))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == english_word2_world:
            if not 'stay green2' in stay_green_eng:
                english_word2.configure(fg='orange', command=lambda: button_connect_english(english_word2, english_word2_world))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == english_word3_world:
            if not 'stay green3' in stay_green_eng:
                english_word3.configure(fg='orange', command=lambda: button_connect_english(english_word3, english_word3_world))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1
        if f_previous_eng_word == english_word4_world:
            if not 'stay green4' in stay_green_eng:
                english_word4.configure(fg='orange', command=lambda: button_connect_english(english_word4, english_word4_world))
                if not clicked_buttons_count_eng == 0:
                    clicked_buttons_count_eng = clicked_buttons_count_eng - 1

   # COLORING KEEPING ONLY ONE BUTTON YELLOW ESP
    def one_orange_esp(f_previous_esp_word):
        global stay_green_esp, clicked_buttons_count_esp
        if f_previous_esp_word == spanish_word0_world:
            if not 'stay green0' in stay_green_esp:
                spanish_word0.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word0, spanish_word0_world))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == spanish_word1_world:
            if not 'stay green1' in stay_green_esp:
                spanish_word1.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word1, spanish_word1_world))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == spanish_word2_world:
            if not 'stay green2' in stay_green_esp:
                spanish_word2.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word2, spanish_word2_world))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == spanish_word3_world:
            if not 'stay green3' in stay_green_esp:
                spanish_word3.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word3, spanish_word3_world))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1
        if f_previous_esp_word == spanish_word4_world:
            if not 'stay green4' in stay_green_esp:
                spanish_word4.configure(fg='orange', command=lambda: button_connect_spanish(spanish_word4, spanish_word4_world))
                if not clicked_buttons_count_esp == 0:
                    clicked_buttons_count_esp = clicked_buttons_count_esp - 1












# ENGLISH BUTTONS

    def button_connect_english(unknown_button, unknown_word):
        global clicked_buttons_count_eng, previous_eng_word, previous_button_eng, stay_green_eng, previous_button, button_check_english, previous_esp_word, unknown_word_f, clicked_buttons_count_esp, previous_word, no_yellow, unknown_button_f
        correct_value = 0
        no_yellow = False
        button_check_english = str(unknown_word)
        unknown_button_f = unknown_button
        unknown_word_f = unknown_word

         # COUNTING BUTTONS
        clicked_buttons_count_eng = clicked_buttons_count_eng + 1
        clicked_buttons_count = clicked_buttons_count_eng + clicked_buttons_count_esp

        # BUTTONS INTERACTIONS 
        if clicked_buttons_count > 1:
            print('clicked_buttons_count(line:179)')
            if clicked_buttons_count_eng > 1:
             print('one orange english(line:181)')
             one_orange_english(str(previous_eng_word))
            if clicked_buttons_count_esp == 1:
             try:
              print('clicked_buttons_count(line:185)')
              if button_conections_dict[button_check_english] == button_check_spanish or button_conections_dict[button_check_spanish] == button_check_english:
               print('clicked_buttons_count(line:187)')
               correct(english_word0_world, 0, 'eng')
               correct(english_word1_world, 1, 'eng')
               correct(english_word2_world, 2,'eng')
               correct(english_word3_world, 3,'eng')
               correct(english_word4_world, 4,'eng')
              if clicked_buttons_count_eng == 1:
               if not button_check_spanish == None:
                if not button_conections_dict[button_check_english] == button_check_spanish or not button_conections_dict[button_check_spanish] == button_check_english:
                 uncorrect()
             except NameError:
                pass
             except KeyError:
                 pass


        # CHANGING DATA FOR NEW AFTER INTERACTIONS
        previous_eng_word = str(unknown_word)
        previous_button_eng = str(unknown_button)
        previous_button = unknown_button
        previous_word = unknown_word
        
         # DOUBLE CLICK
        def button_connect22(unknown_button2):
            global clicked_buttons_count_esp, clicked_buttons_count_eng, previous_button
            previous_button = None
            previous_word = None
       
            if not clicked_buttons_count_eng == 0:
             clicked_buttons_count_eng = clicked_buttons_count_eng - 1
            unknown_button2.configure(bg='black', fg='orange', command=lambda:button_connect_english(unknown_button2, unknown_word))
        # ONE CLICK    
        if no_yellow == False:
         unknown_button.configure(bg='black', fg='yellow', command=lambda:button_connect22(unknown_button))



# SPANISH BUTTTONS

    def button_connect_spanish(unknown_button, unknown_word):
        global clicked_buttons_count_esp, clicked_buttons_count_esp, previous_esp_word, previous_button_esp, stay_green_esp, previous_button, button_check_spanish, previous_word, clicked_buttons_count_eng, unknown_button_f, no_yellow, unknown_word_f
        correct_value = 0
        no_yellow = False
        unknown_button_f = unknown_button
        unknown_word_f = unknown_word
        button_check_spanish = str(unknown_word)

        # COUNTING BUTTONS
        clicked_buttons_count_esp = clicked_buttons_count_esp + 1
        clicked_buttons_count = clicked_buttons_count_eng + clicked_buttons_count_esp

        # BUTTONS INTERACTIONS 
        if clicked_buttons_count > 1:
            if clicked_buttons_count_esp > 1:
             print('ssak')
             one_orange_esp(previous_esp_word)
            if clicked_buttons_count_esp == 1:
             try:
              if button_conections_dict[button_check_english] == button_check_spanish or button_conections_dict[button_check_spanish] == button_check_english:
                 correct(spanish_word0_world, 0, 'esp')
                 correct(spanish_word1_world, 1, 'esp')
                 correct(spanish_word2_world, 2, 'esp')
                 correct(spanish_word3_world, 3, 'esp')
                 correct(spanish_word4_world, 4, 'esp')
              if clicked_buttons_count_esp == 1:
                  if not button_check_english == None:
                      if not button_conections_dict[button_check_english] == button_check_spanish or not button_conections_dict[button_check_spanish] == button_check_english:
                        uncorrect()
             except NameError:
                pass
             except KeyError:
                 pass

        # CHANGING DATA FOR NEW AFTER INTERACTIONS
        previous_esp_word = str(unknown_word)
        previous_button_esp = str(unknown_button)
        previous_word = unknown_word
        previous_button = unknown_button
        # DOUBLE CLICK
        def button_connect2(unknown_button2):
            global clicked_buttons_count_esp, clicked_buttons_count_eng, previous_button
            previous_button = None
            previous_word = None
            if not clicked_buttons_count_esp == 0:
                clicked_buttons_count_esp = clicked_buttons_count_esp - 1

            unknown_button2.configure(bg='black', fg='orange', command=lambda:button_connect_spanish(unknown_button2, unknown_word))
        # ONE CLICK     
        if no_yellow == False:
           unknown_button.configure( fg = 'yellow', command=lambda:button_connect2(unknown_button))  

    # SETTING UP SCREEN ###################################################################################################################################################################################################
    from inter_face import frame_learn_button
    words_frame = tk.Frame(frame_learn_button, bg = 'black')
    for i in range(5):
     words_frame.columnconfigure( i, weight =1, uniform = 'a')
    for i in range(5): 
     words_frame.rowconfigure(i, weight = 1, uniform = 'a')
    
    
    # RANDOM ORDER OF WORDS##################################################################################################################################################################################
    rng_rows = [0,1,2,3,4]
    random_row_esp0 = random.choice(rng_rows)
    rng_rows.remove(random_row_esp0)
    random_row_esp1 = random.choice(rng_rows)
    rng_rows.remove(random_row_esp1)
    random_row_esp2 = random.choice(rng_rows)
    rng_rows.remove(random_row_esp2)
    random_row_esp3 = random.choice(rng_rows)
    rng_rows.remove(random_row_esp3)
    random_row_esp4 = random.choice(rng_rows)
    rng_rows.remove(random_row_esp4)

    rng_rows = [0,1,2,3,4]
    random_row_eng0 = random.choice(rng_rows)
    rng_rows.remove(random_row_eng0)
    random_row_eng1 = random.choice(rng_rows)
    rng_rows.remove(random_row_eng1)
    random_row_eng2 = random.choice(rng_rows)
    rng_rows.remove(random_row_eng2)
    random_row_eng3 = random.choice(rng_rows)
    rng_rows.remove(random_row_eng3)
    random_row_eng4 = random.choice(rng_rows)
    rng_rows.remove(random_row_eng4)
    ###################################################################################################################################################################################################
    basic_font = ('Lionel Classic', 50)
    # WORD PLACEMENT ##################################################################################################################################################################################
    spanish_word0 = tk.Button(words_frame, text=spanish_word0_world, bg='black', fg='orange', height=1, width=10, font=basic_font, command=lambda:button_connect_spanish(spanish_word0, spanish_word0_world))
    spanish_word0.grid(column=1, row=random_row_esp0, padx = 30, pady= 30)
    spanish_word1 = tk.Button(words_frame, text=spanish_word1_world, bg='black', fg='orange', height=1, width=10, font=basic_font, command=lambda:button_connect_spanish(spanish_word1, spanish_word1_world))
    spanish_word1.grid(column=1, row=random_row_esp1, padx = 30, pady= 30)
    spanish_word2 = tk.Button(words_frame, text=spanish_word2_world, bg='black', fg='orange', height=1, width=10, font=basic_font, command=lambda:button_connect_spanish(spanish_word2, spanish_word2_world))
    spanish_word2.grid(column=1, row=random_row_esp2, padx = 30, pady= 30)
    spanish_word3 = tk.Button(words_frame, text=spanish_word3_world, bg='black', fg='orange', height=1, width=10, font=basic_font, command=lambda:button_connect_spanish(spanish_word3, spanish_word3_world))
    spanish_word3.grid(column=1, row=random_row_esp3, padx = 30, pady= 30)
    spanish_word4 = tk.Button(words_frame, text=spanish_word4_world, bg='black', fg='orange', height=1, width=10, font=basic_font, command=lambda:button_connect_spanish(spanish_word4, spanish_word4_world))
    spanish_word4.grid(column=1, row=random_row_esp4, padx = 30, pady= 30)
    
    english_word0 = tk.Button(words_frame, text=english_word0_world, bg='black', fg='orange', height=1, width=10, font=basic_font,command=lambda:button_connect_english(english_word0, english_word0_world))
    english_word0.grid(column=3, row=random_row_eng0)
    english_word1 = tk.Button(words_frame, text=english_word1_world, bg='black', fg='orange', height=1, width=10, font=basic_font,command=lambda:button_connect_english(english_word1, english_word1_world))
    english_word1.grid(column=3, row=random_row_eng1)
    english_word2 = tk.Button(words_frame, text=english_word2_world, bg='black', fg='orange', height=1, width=10, font=basic_font,command=lambda:button_connect_english(english_word2, english_word2_world))
    english_word2.grid(column=3, row=random_row_eng2)
    english_word3 = tk.Button(words_frame, text=english_word3_world, bg='black', fg='orange', height=1, width=10, font=basic_font,command=lambda:button_connect_english(english_word3, english_word3_world))
    english_word3.grid(column=3, row=random_row_eng3)
    english_word4 = tk.Button(words_frame, text=english_word4_world, bg='black', fg='orange', height=1, width=10, font=basic_font, command=lambda:button_connect_english(english_word4, english_word4_world))
    english_word4.grid(column=3, row=random_row_eng4)
    ###################################################################################################################################################################################################
    
    # LISTS AND DICTS##################################################################################################################################################################################
    spanish_list=[spanish_word0, spanish_word1, spanish_word2, spanish_word3, spanish_word4]
    english_list =[english_word0, english_word1, english_word2, english_word3, english_word4]
    button_conections_dict = {spanish_word0_world : english_word0_world, english_word0_world : spanish_word0_world, spanish_word1_world : english_word1_world, english_word1_world : spanish_word1_world, spanish_word2_world : english_word2_world, english_word2_world : spanish_word2_world, spanish_word3_world : english_word3_world, english_word3_world : spanish_word3_world, spanish_word4_world : english_word4_world, english_word4_world : spanish_word4_world}
    ###################################################################################################################################################################################################

    # CONTINUE BUTTON
    def con_but_fun():
       global  clicked_buttons_count_eng, clicked_buttons_count_esp, clicked_buttons_count
       clear()
       clicked_buttons_count_eng = 0
       clicked_buttons_count_esp = 0
       clicked_buttons_count = 0
       stay_green_esp.clear()
       stay_green_eng.clear()
       frame_learn_button.destroy()
       from congrats import congrat_fun, congrats_frame
       congrats_frame.pack()
       congrat_fun()
    continue_button = tk.Button(words_frame, text='continue', bg='black', fg='yellow', font=basic_font, command = lambda: con_but_fun())
    # continue_button.grid(column=4, row=4, padx = 30, pady= 30)
    words_frame.pack()
    frame_learn_button.pack()
    # words_frame.mainloop()
 
###################################################################################################################################################################################################

    

# frist page

# def Learn_it_main( back_or_not = 0): 
#     global Learn_it_label, spanish_button, basic_f, Ltm_screen 
     

#     global Learn_it_label, spanish_button, basic_f, Ltm_screen
#     if back_or_not == 0:
#        Ltm_screen = Tk()
#        Ltm_screen.title('LearnIt!')
#        Ltm_screen.geometry('1920x1080')
#        Ltm_screen.configure(bg='black')
       
#     lil_f = ('Kozuka Mincho Pro M', 50, 'bold')
#     basic_f = ('Lionel Classic', 50)
#     Learn_it_label = Label(text='LearnIt!', bg='black', fg='yellow', height=2, width=10)
#     Learn_it_label.configure(font=lil_f)
#     Learn_it_label.place(y=0, x=725)
#     spanish_button = Button(text='Spanish!', bg='black', fg='orange', height=1, width=len('Spanish!'), command= lambda: spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife'))
#     spanish_button.configure(font=basic_f)
#     spanish_button.place(y=160, x=1600)


#     Ltm_screen.mainloop()

# Learn_it_main()
