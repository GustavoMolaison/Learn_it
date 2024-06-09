from tkinter import *



class screen():
 
  def __init__(self, back_or_not = 0): 
    super().__init__()
   
    self.root = Tk()
    if __name__ == 'menu_learnit':
        try:
         frist_screen.root.withdraw()
        except NameError:
         pass 
    if back_or_not == 0:
       self.root = Tk()
       self.root.title('LearnIt!')
       self.root.geometry('1920x1080')
       self.root.configure(bg='black')
        
class clil():
     def __init__(self):
       super().__init__()
       self.lil_f = ('Kozuka Mincho Pro M', 50, 'bold')
       self.basic_f = ('Lionel Classic', 50)
       self.Learn_it_label = Label(frist_screen.root, text='LearnIt!', bg='black', fg='yellow', height=2, width=10)
       self.Learn_it_label.configure(font=self.lil_f)
       if __name__ == '__main__':
         self.Learn_it_label.place(y=0, x=725)
       
       

class csb(): 
      def __init__(self):
        super().__init__()   
        from mat_but_learnit import spanish_button_func 
        self.spanish_button = Button(frist_screen.root, text='Spanish connect!', bg='black', fg='orange', height=1, width=len('Spanish connect'), command= lambda: spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife'))
        self.spanish_button.configure(font=frist_label.basic_f)
        self.spanish_button.place(y=160, x=1400)
        if __name__ == '__main__':
         frist_screen.root.mainloop()

    


frist_screen = screen()
frist_label = clil()
frist_button = csb()


