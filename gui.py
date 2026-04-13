import tkinter as tk
from tkinter import messagebox
import utill_functions
#import all the menus as themselfs
from login_logout import make_acount,login_logout
from main import see_stats,change_savings,change_stats,main_menu,change_expenses,manage_overtime_savings
from budgeting_and_savings_goal import budgeting_and_saveings
class gui_manager(tk.Tk):
    def __init__(self,data):
        self.data=data
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
        for x in (main_menu,login_logout,make_acount,see_stats,change_savings,change_stats,change_expenses,manage_overtime_savings,budgeting_and_saveings): #put all the menus here
            page_name=x.__name__.replace("Page","")
            frame=x(gui_manager=container,manager=self,user_data=self.data)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_screen("login_logout")
    def show_screen(self,page_name):
        if page_name not in self.frames:
            messagebox.showerror("Error", f"There is no window named: {page_name}")
            return
        for x in self.frames.values():
            x.pack_forget()
        frame=self.frames[page_name]
        for x in frame.winfo_children():
            x.destroy()
        if hasattr(frame, "refresh"):
            frame.refresh()
        frame.tkraise()
        
    def change_vars(self,user,password):
        self.user=user
        self.password=password
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


if __name__=="__main__":
    data=utill_functions.csv_file("data.csv")
    app=GUIManager(data)
    app.mainloop()
