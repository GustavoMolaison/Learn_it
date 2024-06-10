import tkinter as tk



class screen():
 
  def __init__(self, back_or_not = 0, create_new_screen = 0): 
    super().__init__()
    global unknown_screen, frist_label
        
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
        print('XXOXOOXOXOXXOXOXOXOXOXOXOXXOXOXOOXOXOXXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXXOXO')
        from mat_but_learnit import spanish_button_func 
        self.spanish_button = tk.Button(frist_screen.root, text='Spanish connect!', bg='black', fg='orange', height=1, width=len('Spanish connect'), command= lambda: spanish_button_func('pronto', 'soon', 'frio', 'cold', 'calor', 'hot', 'silla', 'chair', 'cuchillo', 'knife'))
        print('XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
        self.spanish_button.configure(font=frist_label.basic_f)
        self.spanish_button.place(y=160, x=1400)
        if __name__ == '__main__':
          frist_screen.root.mainloop()

    

print('ohujghcoidiz')
frist_screen = screen()
print('1')
frist_label = clil()
print('2')
frist_button = csb()
print('3')

