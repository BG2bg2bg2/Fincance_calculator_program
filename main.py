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
    def __init__(self,gui_manager,manager):
        super().__init__(gui_manager)
        self.manager=manager
        tk.Button(self,text="see stats",command=lambda: manager.show_screen("see_stats")).pack()
        tk.Button(self,text="change stats",command=lambda: manager.show_screen("change_stats")).pack()
        tk.Button(self,text="manage overtime savings",command=lambda: manager.show_screen("make_acount")).pack()
        tk.Button(self,text="quit",command=quit).pack()
class see_stats(tk.Frame):
    def __init__(self,gui_manager,manager):
        super().__init__(gui_manager)
        self.manager=manager
        for x in data:
            if x["username"]==username and password==x["password"]:
                formating={}
                tk.Label(self,text=f"username:{x["username"]}")
                tk.Label(self,text=f"password:{x["password"]}")
                tk.Label(self,text=f"password:{x["income"]}")
                tk.Label(self,text=f"password:{x["savings"]}")
                tk.Label(self,text="refer to the popup window for more information (close when done)")
                tk.Button(self,text="go back",command=lambda: manager.show_screen("main_menu")).pack()
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
    def __init__(self,gui_manager,manager):
        super().__init__(gui_manager)
        self.manager=manager
        tk.Button(self,text="go back",command=lambda: manager.show_screen("see_stats")).pack()
        tk.Button(self,text="add expenses",command=lambda: manager.show_screen("add_expenses")).pack()
        tk.Button(self,text="remove expenses",command=lambda: manager.show_screen("remove_expenses")).pack()
        tk.Button(self,text="change expenses",command=lambda: manager.show_screen("change_expenses")).pack()
        tk.Button(self,text="change savings",command=lambda: manager.show_screen("change_savings")).pack()
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
    gooy=gui.gui_manager(title="financial manager")
    main(gooy)
    gooy.root.mainloop()
