#ES main function 

#Liam imports the init csv class with the file path 

#BG from every file needed to be imputed input/bring in all/everything onto this file
#from BG_code file import enter new account
#from budgeting_&_savings file import all functions
#from login_logout file import all
#from randm_password_generator file import all


#make a function called main 


    #make a while true loop 
    
        #ask user if they want to create an account,log in,or exit 

        #if user choice is 1 then 
        
            #call create account
            
        #else if user choice is 2 then
            
            #call login
        
        #else if user choice is 3 then tell the user to select again,continue 
            
            #display thanks for using the FINANCE CALCULATOR PROGRAM
import budgeting_and_savings_goal,helper,login_logout,utill_functions,random_password_generator,gui
import tkinter as tk
from tkinter import messagebox

#everything we want to happen in here

#this keeps it on the screen 

class main_menu(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
    def refresh(self):
        tk.Button(self,text="see stats",command=lambda: self.manager.show_screen("see_stats")).pack()
        tk.Button(self,text="change stats",command=lambda: self.manager.show_screen("change_stats")).pack()
        tk.Button(self,text="manage overtime savings",command=lambda: self.manager.show_screen("manage_overtime_savings")).pack()
        tk.Button(self,text="quit",command=quit).pack()
class see_stats(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
        self.data=user_data
    def refresh(self):
        for x in self.data:
            if x["username"]==self.manager.user and self.manager.password==x["password"]:
                formating={}
                tk.Label(self,text=f"username:{x["username"]}").pack()
                tk.Label(self,text=f"password:{x["password"]}").pack()
                tk.Label(self,text=f"password:{x["income"]}").pack()
                tk.Label(self,text=f"password:{x["savings"]}").pack()
                tk.Label(self,text="refer to the popup window for more information (do not close when done)").pack()
                tk.Button(self,text="go back",command=lambda: self.manager.show_screen("main_menu")).pack()
                expens=utill_functions.csv_file.from_underscore(x["expenses_name"])
                mount=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                budg=utill_functions.csv_file.from_underscore(x["budget_expense"])
                totalcost=sum(int(m) for m in mount if m.strip()) 
                userrow=x
                for num,x in enumerate(expens):
                    percentage=(int(mount[num])/int(totalcost))*100 if int(totalcost)>0 else 0
                    current_amt=int(mount[num])
                    history=[int(v) for v in utill_functions.csv_file.from_underscore(userrow["savings_over_time"]) if v.strip()]
                    if not history: history=[0]
                    formating[x]=[percentage,current_amt,history]
                    utill_functions.parse_turtle_data(formating)
class change_stats(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
    def refresh(self):
        tk.Button(self,text="go back",command=lambda: self.manager.show_screen("see_stats")).pack()
        tk.Button(self,text="add expenses",command=lambda: self.manager.show_screen("add_expenses")).pack()
        tk.Button(self,text="remove expenses",command=lambda: self.manager.show_screen("remove_expenses")).pack()
        tk.Button(self,text="change expenses",command=lambda: self.manager.show_screen("change_expenses")).pack()
        tk.Button(self,text="change savings",command=lambda: self.manager.show_screen("change_savings")).pack()
class change_savings(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
        self.user_data=user_data
    def refresh(self):
        tk.Button(self,text="go back",command=lambda: self.manager.show_screen("change_stats")).pack()
        for x in self.user_data:
            if x["username"]==self.manager.user and self.manager.password==x["password"]:
                tk.Label(self,text=f"old savings amount: {x["savings"]}").pack()
        self.savings=tk.Entry(self,validate='key',validatecommand=self.manager.valid_int).pack()
        tk.Button(self,text="enter",command=self.change_thy_saveings).pack()
    def change_thy_saveings(self):
        for x in self.user_data:
            if x["username"] == self.manager.user and x["password"] ==self.manager.password:
                x["savings"] = self.savings.get()
                self.user_data.update_data(self.manager.user, x)
                self.manager.show_screen("change_stats")
class change_expenses(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
        self.user_data=user_data
    def refresh(self):
        tk.Button(self,text="go back",command=lambda: self.manager.show_screen("change_stats")).pack()
        for x in self.user_data:
            if x["username"] == self.manager.user and x["password"] == self.manager.password:
                names= utill_functions.csv_file.from_underscore(x["expenses_name"])
                vals=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                budgets=utill_functions.csv_file.from_underscore(x["budget_expense"])
                self.boxes=[]
                for num,z in enumerate(names):
                    row = tk.Frame(self)
                    row.pack(pady=2)
                    name=tk.Entry(row, width=10)
                    name.insert(0,str(names[num]))
                    name.pack(side="left")
                    cost=tk.Entry(row,width=10,validate='key',validatecommand=self.manager.valid_int)
                    cost.insert(0, int(vals[num]))
                    cost.pack(side="left")
                    budget_entry = tk.Entry(row, width=10,validate='key',validatecommand=self.manager.valid_int)
                    budget_entry.insert(0, int(budgets[num]))
                    budget_entry.pack()
                    self.boxes.append({"name":name,"cost":cost,"budget":budget_entry})
                tk.Button(self, text="SAVE ALL CHANGES", fg="green",command=self.save_all).pack(pady=10)
    def save_all(self):
        new_names = []
        new_costs = []
        new_budgets = []
        for x in self.boxes:
            new_names.append(x["name"].get() if x["name"].get() else "Unnamed")
            new_costs.append(x["cost"].get() if x["cost"].get() else "0")
            new_budgets.append(x["budget"].get() if x["budget"].get() else "0")
        for x in self.user_data:
            if x["username"] == self.manager.user and x["password"] ==self.manager.password:
                x["expenses_name"] = utill_functions.csv_file.to_list(new_names)
                x["expenses_amount"] = utill_functions.csv_file.to_list(new_costs)
                x["budget_expense"] = utill_functions.csv_file.to_list(new_budgets)
                self.user_data.update_data(self.manager.user, x)
                self.manager.show_screen("change_stats")
class remove_expenses(tk.Frame):
    def __init__(self,gui_manager,manager,user_data):
        super().__init__(gui_manager)
        self.manager=manager
        self.user_data=user_data
    def refresh(self):
        for x in self.user_data:
            if x["username"] == self.manager.user and x["password"] == self.manager.password:
                if len(self.user_data["expenses_name"]) <=1:
                    messagebox.showinfo("invalid input","You cannot have 0 expenses.")
                    self.manager.show_screen("change_stats")
                names= utill_functions.csv_file.from_underscore(x["expenses_name"])
                vals=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                budgets=utill_functions.csv_file.from_underscore(x["budget_expense"])
                tk.Button(self,text="go back",command=lambda: self.manager.show_screen("change_stats")).pack()
                for num,x in enumerate(names):
                    tk.Label(self,text=x)
                    for num, name in enumerate(names):
                        row = tk.Frame(self)
                        row.pack(pady=2, fill="x", padx=20)
                        
                        tk.Label(row, text=f"name:{name}, cost:{vals[num]}, budget:{budgets[num]}", width=20, anchor="w").pack(side="left")
                        tk.Button(row, text="Remove", fg="red", command=lambda i=num: self.delete_expense(i)).pack(side="right")
                break
class add_expenses(tk.Frame):
    def __init__(self, gui_manager, manager, user_data):
        super().__init__(gui_manager)
        self.manager = manager
        self.user_data = user_data
    def refresh(self):
        tk.Button(self, text="go back", command=lambda: self.manager.show_screen("change_stats")).pack()
        tk.Label(self, text="Add New Expense", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self, text="Expense Name:").pack()
        self.new_name = tk.Entry(self)
        self.new_name.pack()
        tk.Label(self, text="Cost:").pack()
        self.new_cost = tk.Entry(self, validate='key', validatecommand=self.manager.valid_int)
        self.new_cost.pack()
        tk.Label(self, text="Budget:").pack()
        self.new_budget = tk.Entry(self, validate='key', validatecommand=self.manager.valid_int)
        self.new_budget.pack()
        tk.Button(self, text="ADD EXPENSE", bg="blue", fg="white", 
                  command=self.add_item).pack(pady=20)
    def add_item(self):
        name = self.new_name.get().strip()
        cost = self.new_cost.get().strip()
        budget = self.new_budget.get().strip()
        if not name or not cost or not budget:
            messagebox.showwarning("Error", "All fields must be filled out.")
            return
        for x in self.user_data:
            if x["username"] == self.manager.user:
                names = utill_functions.csv_file.from_underscore(x["expenses_name"])
                costs = utill_functions.csv_file.from_underscore(x["expenses_amount"])
                budgets = utill_functions.csv_file.from_underscore(x["budget_expense"])
                names.append(name.replace("_", " ")) # Clean name
                costs.append(cost)
                budgets.append(budget)
                x["expenses_name"] = utill_functions.csv_file.to_list(names)
                x["expenses_amount"] = utill_functions.csv_file.to_list(costs)
                x["budget_expense"] = utill_functions.csv_file.to_list(budgets)
                self.user_data.update_data(self.manager.user, x)
                
                messagebox.showinfo("Success", f"Added {name}!")
                self.manager.show_screen("change_stats")
                break
class manage_overtime_savings(tk.Frame):
    def __init__(self, gui_manager, manager, user_data):
        super().__init__(gui_manager)
        self.manager = manager
        self.user_data = user_data

    def refresh(self):
        # 1. Navigation
        tk.Button(self, text="go back", command=lambda: self.manager.show_screen("main_menu")).pack(anchor="w")
        
        tk.Label(self, text="Manage Savings Over Time", font=("Arial", 12, "bold")).pack(pady=10)

        for x in self.user_data:
            if x["username"] == self.manager.user and x["password"] == self.manager.password:
                history = utill_functions.csv_file.from_underscore(x["savings_over_time"])
                history = [h for h in history if h.strip()]
                tk.Label(self, text=f"Current History: {', '.join(history) if history else 'No data'}").pack()
                tk.Label(self, text="Add New Monthly Saving:").pack(pady=(10, 0))
                self.new_saving = tk.Entry(self, validate='key', validatecommand=self.manager.valid_int)
                self.new_saving.pack()
                tk.Button(self, text="ADD TO HISTORY", bg="blue", fg="white", 
                          command=lambda row=x: self.add_history(row)).pack(pady=10)
                tk.Button(self, text="Clear All History", fg="red", 
                          command=lambda row=x: self.clear_history(row)).pack(pady=20)
                break
    def add_history(self, row):
        val = self.new_saving.get()
        if val:
            history = utill_functions.csv_file.from_underscore(row["savings_over_time"])
            history = [h for h in history if h.strip()]
            history.append(val)
            row["savings_over_time"] = utill_functions.csv_file.to_list(history)
            self.user_data.update_data(self.manager.user, row)
            
            messagebox.showinfo("Success", "Savings history updated!")
            self.manager.show_screen("manage_overtime_savings")

    def clear_history(self, row):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all history?"):
            row["savings_over_time"] = ""
            self.user_data.update_data(self.manager.user, row)
            self.manager.show_screen("manage_overtime_savings")
def main(gooy):
    
    data=utill_functions.csv_file("data.csv")
    username,password=login_logout.login(data,gooy)
    if not(username):
        return
    while True:
        choise=gooy.get_valid_type(int,"0 to log out\n1 to see stats\n2 to change stats\n3 to see and modify overtime savings: ",valid=(0,3))
        if choise==0:
            return
        elif choise==1:
            for x in data:
                if x["username"]==username and password==x["password"]:
                    formating={}
                    messagebox.showinfo(f"username:{x["username"]}\npassword:{x["password"]}\nincome:{x["income"]}\nsavings:{x["savings"]}")
                    expens=utill_functions.csv_file.from_underscore(x["expenses_name"])
                    mount=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                    budg=utill_functions.csv_file.from_underscore(x["budget_expense"])
                    totalcost=sum(int(m) for m in mount if m.strip()) 
                    userrow=x
                    for num,x in enumerate(expens):
                        percentage=(int(mount[num])/int(totalcost))*100 if int(totalcost)>0 else 0
                        current_amt=int(mount[num])
                        history=[int(v) for v in utill_functions.csv_file.from_underscore(userrow["savings_over_time"]) if v.strip()]
                        if not history: history=[0]
                        formating[x]=[percentage,current_amt,history]
                        utill_functions.parse_turtle_data(formating)
        elif choise==2:
            while True:
                choise=gooy.get_valid_type(int,"0 to return\n1 to add expenses\n2 to remove expenses\n3 to change expense\n4 to change income\n5 to change savings: ",valid=(0,5))
                if choise==0:
                    break
                elif choise==1:
                    userrow=None
                    for x in data:
                        if x["username"]==username and password==x["password"]:
                            expenses=utill_functions.csv_file.from_underscore(x["expenses_name"])
                            amounts=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                            budgets=utill_functions.csv_file.from_underscore(x["budget_expense"])
                            userrow=x
                    count=0
                    while True:
                        count+=1
                        expence=gooy.get_valid_type(str,f"what is the name of your #{count} expence(0 to stop adding more): ").replace(",","").replace('"',"").replace("`","").replace("_","")
                        if expence=="0":
                            if len(expenses)>0:
                                break
                            else:
                                messagebox.showinfo("you cant have 0 expenses")
                                continue
                        amount=gooy.get_valid_type(int,f"what is the cost of {expence}: ")
                        budget=gooy.get_valid_type(int,f"what is your budget for {expence}: ")
                        if gooy.get_valid_type(str,f"do you want to add {expence}:{amount}:{budget}(y/n): ",valid=["y","n"])=="y":
                            expenses.append(expence)
                            amounts.append(amount)
                            budgets.append(budget)
                            userrow["expenses_name"]=utill_functions.csv_file.to_list(expenses)
                            userrow["expenses_amount"]=utill_functions.csv_file.to_list(amounts)
                            userrow["budget_expense"]=utill_functions.csv_file.to_list(budgets)
                            data.update_data(username,userrow)
                            data.update_data(username,userrow)
                elif choise==2:
                    for x in data:
                        if x["username"]==username and x["password"]==password:
                            expenses=utill_functions.csv_file.from_underscore(x["expenses_name"])
                            amounts=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                            budgets=utill_functions.csv_file.from_underscore(x["budget_expense"])
                            userrow=x
                    if len(expenses) <=1:
                        messagebox.showinfo("You cannot have 0 expenses. Add one before removing this one.")
                        continue
                    messagebox.showinfo("0 to return")
                    for num,x in enumerate(expens):
                        messagebox.showinfo(f"{num+1} for: expense name: {x} amount: ${mount[num]} budget: ${budg[num]}")
                        maxi=num+1
                    inp=gooy.get_valid_type(int,"what do you want:",valid=(0,maxi))
                    if inp==0:
                        continue
                    if gooy.get_valid_type(str,f"do you want to delete {expenses[inp-1]}(y/n): ",valid=["y","n"])=="y":
                        expenses.pop(inp-1)
                        amounts.pop(inp-1)
                        budgets.pop(inp-1)
                    userrow["expenses_name"]=utill_functions.csv_file.to_list(expenses)
                    userrow["expenses_amount"]=utill_functions.csv_file.to_list(amounts)
                    userrow["budget_expense"]=utill_functions.csv_file.to_list(budgets)                
                    data.update_data(username,userrow)
                elif choise==3:
                    for x in data:
                        if x["username"]==username and x["password"]==password:
                            expenses=utill_functions.csv_file.from_underscore(x["expenses_name"])
                            amounts=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                            budgets=utill_functions.csv_file.from_underscore(x["budget_expense"])
                            expens=utill_functions.csv_file.from_underscore(x["expenses_name"])
                            mount=utill_functions.csv_file.from_underscore(x["expenses_amount"])
                            budg=utill_functions.csv_file.from_underscore(x["budget_expense"])
                            userrow=x
                    messagebox.showinfo("0 to return")
                    for num,x in enumerate(expens):
                        messagebox.showinfo(f"{num+1} for: expense name: {x} amount: ${mount[num]} budget: ${budg[num]}")
                        maxi=num+1
                    inp=gooy.get_valid_type(int,"what do you want to change:",valid=(0,maxi))
                    if inp==0:
                        continue
                    expense=gooy.get_valid_type(str,"what is the new name: ")
                    amount=gooy.get_valid_type(int,"what is the new amount: ")
                    budget=gooy.get_valid_type(int,"what is the new budget: ")
                    if gooy.get_valid_type(str,f"do you want to change {expenses[inp-1]} to {expense}:{amount}:{budget}(y/n): ",valid=["y","n"])=="y":
                        expenses[inp-1]=expense
                        amounts[inp-1]=amount
                        budgets[inp-1]=budget
                    userrow["expenses_name"]=utill_functions.csv_file.to_list(expenses)
                    userrow["expenses_amount"]=utill_functions.csv_file.to_list(amounts)
                    userrow["budget_expense"]=utill_functions.csv_file.to_list(budgets)                
                    data.update_data(username,userrow)
                elif choise==4:
                    for x in data:
                        if x["username"]==username and x["password"]==password:
                            userrow=x
                    new_val=gooy.get_valid_type(int,f"what do you want to change income ({userrow["income"]}) to (0 to return): ")
                    if new_val==0:
                        continue
                    userrow["income"]=new_val
                    data.update_data(username,userrow)
                elif choise==5:
                    for x in data:
                        if x["username"]==username and x["password"]==password:
                            userrow=x
                    new_val=gooy.get_valid_type(int,f"what do you want to change savings ({userrow["savings"]}) to (0 to return): ")
                    if new_val==0:
                        continue
                    userrow["savings"]=new_val
                    data.update_data(username,userrow)
        elif choise==3:
            while True:
                choise=gooy.get_valid_type(int,"0 to return\n1 to add an entry\n2 to remove an entry\n3 to import the current savings amount: ",valid=(0,3))
                if choise==0:
                    break
                elif choise==1:
                    for x in data:
                        if x["username"]==username and x["password"]==password:
                            userrow=x
                            savings_over_time=utill_functions.csv_file.from_underscore(x["savings_over_time"])
                    if len(savings_over_time)==0:
                        pass
                    else:
                        for num,x in enumerate(savings_over_time):
                            messagebox.showinfo(f"entry {num+1}: ${x}")
                    while True:
                        val=gooy.get_valid_type(int,"what is the new entry: ")
                        if gooy.get_valid_type(str,f"are you sure you want to add ${val} to your overtime savings(y/n): ",valid=["y","n"])=="y":
                            break
                    savings_over_time.append(val)
                    userrow["savings_over_time"]=utill_functions.csv_file.to_list(savings_over_time)
                    data.update_data(username,userrow)
                elif choise==2:
                    for x in data:
                        if x["username"]==username and x["password"]==password:
                            userrow=x
                            savings_over_time=utill_functions.csv_file.from_underscore(x["savings_over_time"])
                    if len(savings_over_time)==0:
                        messagebox.showinfo("you cant remove any entries because there are none")
                        continue
                    else:
                        messagebox.showinfo("0 to return")
                        for num,x in enumerate(savings_over_time):
                            messagebox.showinfo(f"{num+1} to remove entry {num+1}: ${x}")
                            maxi=num+1
                        while True:
                            val=gooy.get_valid_type(int,"what do you want to remove: ",valid=(0,maxi))
                            if val==0:
                                break
                            to_remove=savings_over_time[val-1]
                            if gooy.get_valid_type(str,f"are you sure you want to remove ${val} from your overtime savings(y/n): ",valid=["y","n"])=="y":
                                savings_over_time.remove(to_remove)
                                userrow["savings_over_time"]=utill_functions.csv_file.to_list(savings_over_time)
                                data.update_data(username,userrow)
                                break
                if choise==3:
                    for x in data:
                        if x["username"]==username and x["password"]==password:
                            userrow=x
                            savings_over_time=utill_functions.csv_file.from_underscore(x["savings_over_time"])
                    savings_over_time.append(userrow["savings"])
                    data.update_data(username,userrow)
                    messagebox.showinfo(f"done\nadded {userrow["savings"]} to entries")
                        
                        
if __name__=="__main__":
    data=utill_functions.csv_file("data.csv")
    gooy=gui.gui_manager(data=data)
    root=tk.Tk()
    root.mainloop()
