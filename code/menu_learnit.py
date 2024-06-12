import tkinter as tk



class screen():
 
  def __init__(self, back_or_not = 0, create_new_screen = 0): 
    super().__init__()
    global frist_label
        
    # if __name__ == '__main__' or create_new_screen == 1:
    if back_or_not == 0:
       self.root = tk.Tk()
       self.root.title('LearnIt!')
       self.root.geometry('1920x1080')
       self.root.configure(bg='black')
  
       
       
        
class clil():
     def __init__(self):
       super().__init__()
       if __name__ == 'menu_learnit':
        frist_screen.root.withdraw()  
       self.lil_f = ('Kozuka Mincho Pro M', 50, 'bold')
       self.basic_f = ('Lionel Classic', 50)
       self.Learn_it_label = tk.Label(frist_screen.root, text='LearnIt!', bg='black', fg='yellow', height=2, width=10)
       self.Learn_it_label.configure(font=self.lil_f)
       self.Learn_it_label.place(y=0, x=725)
       
       
       

class csb(): 
      def __init__(self):
        super().__init__()   
        def Learn_button_com():
            def back_button():
              frame_learn_button.destroy()
            self.small_f = ('Lionel Classic', 20)
            self.normal_f = ('Lionel Classic', 50)
            from inter_face import Learn_button_com, frame_learn_button
            from mat_but_learnit import spanish_button_func 
             
            Learn_button_com(frist_screen.root)
            frame_learn_button.pack()
            # self.frame_learn_button = tk.Frame(frist_screen.root)
            # self.frame_learn_button = tk.Frame(width= 1920, height=1080, padx = 25, pady = 25, bg = 'black')
            # self.frame_learn_button.propagate(False)
            # self.frame_learn_button.pack()

            self.latly_used_frame = tk.Frame(frame_learn_button, bg = 'gold')
            self.latly_used_frame.configure( width=400, height = 500, padx = 25, pady = 25)
            self.latly_used_frame.propagate(False)
            for i in range(0):
              self.latly_used_frame.columnconfigure(i, weight = 1, uniform = 'a')
            for i in range(4):
              self.latly_used_frame.rowconfigure(i, weight = 1, uniform = 'a')    
          
            self.spanish_button = tk.Button(self.latly_used_frame, text='Spanish connect!', bg='black', fg='orange', padx = 10, pady = 10, height=1, width=len('Spanish connect'), command= lambda: spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife'))
            self.spanish_button.configure(font=self.small_f)
            self.spanish_button.grid(column = 1, row = 0)
          
            self.back_button = tk.Button(frame_learn_button, text = '<---', bg = 'black', fg='yellow', width=10, height=2, command = lambda: back_button() )
            self.back_button.place(x = 25, y = 950)

            self.latly_used = tk.Label(frame_learn_button, text = 'Latly used', bg='black', fg='gold',  height=1, width=len('Latly used'))
            self.latly_used.configure(font=self.normal_f)
            self.latly_used.place(y=140, x=1335)

            
            self.latly_used_frame.place(x = 1390, y = 250)
            
        
          
        if __name__ == '__main__':
             
      
             self.learn_button = tk.Button(frist_screen.root, text='Learn!', bg='black', fg='orange', height=1, width=len('Learn!'), command= lambda: Learn_button_com())
             self.learn_button.configure(font=frist_label.basic_f)
             self.learn_button.place(y=160, x=1670)
             if __name__ == '__main__':
               frist_screen.root.mainloop()



# def commandside():
#    if __name__ == '__main__':
#          from mat_but_learnit import spanish_button_func 
#    frist_label.Learn_it_label.destroy()
#    frist_button.spanish_button.destroy()
#    frist_screen.root.withdraw()
#    spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife'))


frist_screen = screen()
print('1')
frist_label = clil()
print('2')
frist_button = csb()
print('3')

