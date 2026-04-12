import tkinter as tk
import utill_functions
#import all the menus as themselfs
class GUIManager(tk.Tk):
    def __init__(self,data):
        super().__init__()
        self.data=data
        self.title("Finance manager")
        self.geometry("400x400")
        container=tk.Frame(self)
        container.pack(fill="both",expand=True)
        self.valid_int=(self.register(self.int_input),'%P')
        self.valid_float=(self.register(self.float_input),'%P')
        self.valid_str=(self.register(self.str_input),'%P')
        self.valid_tuple=(self.register(self.tuple_input),'%P')
        self.valid_list=(self.register(self.list_input),'%P')
        self.user=""
        self.password="" 
        self.frames={}
        for x in (MainMenu,StatsPage): #put all the menus here
            page_name=x.__name__.replace("Page","")
            frame=x(parent=container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_screen("Menu")
    def show_screen(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()
    def int_input(self,P):
        if P.isdigit():
            return True
        return False
    def float_input(self,P):
        try:
            float(P)
            return True
        except:
            return False
    def str_input(self,P):
        try:
            str(P)
            return True
        except:
            return False
    def tuple_input(self,P):
        try:
            tuple(P)
            return True
        except:
            return False
    def list_input(self,P):
        try:
            list(P)
            return True
        except:
            return False
class MainMenu(tk.Frame):
    def __init__(self,gui_manager,manager):
        super().__init__(gui_manager)
        tk.Label(self,text="Main Menu").pack()
        tk.Button(self,text="View Stats",
                  command=lambda: manager.show_screen("Stats")).pack()

if __name__=="__main__":
    data=utill_functions.csv_file("data.csv")
    app=GUIManager(data)
    app.mainloop()
