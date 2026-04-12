#ES log in log out 

#make file_path be the file path to the csv or where the accounts are kept

import utill_functions
import random_password_generator
import tkinter as tk
from tkinter import messagebox
#make a function called login 
class login_logout(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
        self.user_data=user_data
    def refresh(self):
        tk.Button(self,text="make acount",command=lambda: self.manager.show_screen("make_acount")).pack()
        tk.Button(self,text="quit",command=quit).pack()
        tk.Label(self,text="username",font=("Arial",5)).pack()
        self.username=tk.Entry(self)
        self.username.pack()
        tk.Label(self,text="password",font=("Arial",5)).pack()
        self.password=tk.Entry(self,show="*")
        self.password.pack()
        tk.Button(self,text="login",command=self.validate).pack()
    def validate(self):
        user=self.username.get()
        passw=self.password.get()
        found=False
        for x in self.user_data:
            if x["username"] == user and x["password"] == passw:
                self.manager.change_vars(user,passw)
                self.manager.show_screen("main_menu")
                found=True
                break
        if not found:
            tk.messagebox.showerror("Error","Invalid username or password")
class make_acount(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
        self.user_data=user_data
        self.expenses,self.amounts,self.budgets=[],[],[]
    def refresh(self):
        tk.Button(self,text="Go Back",command=lambda: self.manager.show_screen("login_logout")).pack(anchor="w")
        
        tk.Label(self,text="Username").pack()
        self.username=tk.Entry(self)
        self.username.pack()

        tk.Label(self,text="Password (leave blank for random)").pack()
        self.password=tk.Entry(self)
        self.password.pack()

        tk.Label(self,text="Hourly Income").pack()
        self.income=tk.Entry(self,validate='key',validatecommand=self.manager.valid_int)
        self.income.pack()

        tk.Label(self,text="Savings").pack()
        self.savings=tk.Entry(self,validate='key',validatecommand=self.manager.valid_int)
        self.savings.pack()

        tk.Label(self,text="Add Expenses",font=("Arial",10,"bold")).pack(pady=5)
        exp_frame=tk.Frame(self)
        exp_frame.pack()
        
        tk.Label(exp_frame,text="Name").grid(row=0,column=0)
        self.exp_name=tk.Entry(exp_frame,width=10,validate='key',validatecommand=self.manager.valid_int)
        self.exp_name.grid(row=1,column=0)

        tk.Label(exp_frame,text="Cost").grid(row=0,column=1)
        self.exp_cost=tk.Entry(exp_frame,width=8,validate='key',validatecommand=self.manager.valid_int)
        self.exp_cost.grid(row=1,column=1)

        tk.Label(exp_frame,text="Budget").grid(row=0,column=2)
        self.exp_budget=tk.Entry(exp_frame,width=8,validate='key',validatecommand=self.manager.valid_int)
        self.exp_budget.grid(row=1,column=2)

        tk.Button(self,text="Add Expense",command=self.add_expense_to_list).pack(pady=5)
        self.expense_listbox=tk.Listbox(self,height=4)
        self.expense_listbox.pack(fill="x",padx=20)
        tk.Button(self,text="CREATE ACCOUNT",bg="green",command=self.create_user).pack(pady=20)
    def add_expense_to_list(self):
        name=self.exp_name.get().strip().replace(",","")
        cost=self.exp_cost.get()
        budget=self.exp_budget.get()
        
        if name and cost.isdigit() and budget.isdigit():
            self.expenses.append(name)
            self.amounts.append(int(cost))
            self.budgets.append(int(budget))
            self.expense_listbox.insert(tk.END,f"{name}: ${cost}, budget: ${budget}")
            
            self.exp_name.delete(0,tk.END)
            self.exp_cost.delete(0,tk.END)
            self.exp_budget.delete(0,tk.END)
        else:
            messagebox.showwarning("Invalid input(s)","Input a valid input")

    def create_user(self):
        user=self.username.get().strip()
        passw=self.password.get()
        income=self.income.get()
        savings=self.savings.get()

        if not user or not income or not savings:
            messagebox.showwarning("Invalid input(s)","Input a valid input")
            return

        if not passw:
            passw=random_password_generator.make_password()
            messagebox.showinfo("Generated Password",f"Your password is: {passw}")

        self.user_data.add([user,passw,int(income),utill_functions.csv_file.to_list(self.expenses),utill_functions.csv_file.to_list(self.amounts),utill_functions.csv_file.to_list(self.budgets),int(savings),0])
        self.manager.show_screen("main_menu")
