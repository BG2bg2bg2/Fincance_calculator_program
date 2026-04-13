# GNB - Gov Stuff (Budgeting + Savings Goal Tracker)

# End up here from Edwing's menu if user selects budgeting/savings options

# Before user gets here:
# - Categories already exist (Rent,Food,Transportation,etc.)
# - Income/expenses may already be stored by Edwing/Liam
import utill_functions
import tkinter as tk
from tkinter import messagebox

# Ask user:
# 1. Set budget limits
# 2. View budgeting plan
# 3. Compare expenses to budget
# 4. Savings goal tracker
# 5. Go back to main menu

class budgeting_and_saveings(tk.Frame):
    def __init__(self, gui_manager, manager, user_data):
        super().__init__(gui_manager)
        self.manager = manager
        self.user_data = user_data
    def refresh(self):
        #makes a button for setting budget limits
        tk.Button(self,text="set budget limits",command=lambda: self.manager.show_screen("set_budget_limits")).pack()
        #makes a button for saving goal
        tk.Button(self,text="set savings goal",command=lambda: self.manager.show_screen("savings_goals_tracker")).pack()
        #button for going back to main menu
        tk.Button(self,text="go back",command=lambda: self.manager.show_screen("main_menu")).pack()
class set_budget_limits(tk.Frame):
    def __init__(self, gui_manager, manager, user_data):
        super().__init__(gui_manager)
        self.manager = manager
        self.user_data = user_data
        self.limits = []

    def refresh(self):
        self.limits = []

        for x in self.user_data:
            if x["username"] == self.manager.user and self.manager.password == x["password"]:
                tk.Button(self, text="go back", command=lambda: self.manager.show_screen("budgeting_and_saveings")).pack()
                
                expenses_name = utill_functions.csv_file.from_underscore(x["expenses_name"])
                expenses_amount = utill_functions.csv_file.from_underscore(x["expenses_amount"])
                budget_limits = utill_functions.csv_file.from_underscore(x["budget_limits"])

                for num, y in enumerate(budget_limits):
                    cost = expenses_amount[num]
                    name = expenses_name[num]
                    
                    warning = f"!!!OVER BUDGET by {int(cost) - int(y)}!!!" if int(cost) > int(y) else ""
                    tk.Label(self, text=f"{warning} name: {name}, cost: {cost} budget limit: ").pack()
                    
                    ent = tk.Entry(self, validate='key', validatecommand=self.manager.valid_int)
                    ent.insert(0, int(y))
                    ent.pack()
                    self.limits.append(ent)
                
                tk.Button(self, text="change", command=self.get_info).pack()

    def get_info(self):
        new_values = [ent.get() for ent in self.limits]
        
        for x in self.user_data:
            if x["username"] == self.manager.user and x["password"] == self.manager.password:
                x["budget_limits"] = utill_functions.csv_file.to_underscore(new_values)
                self.user_data.update_data(self.manager.user, x)
                self.manager.show_screen("budgeting_and_saveings")
                break

class savings_goals_tracker(tk.Frame):
    def __init__(self, gui_manager, manager, user_data):
        super().__init__(gui_manager)
        self.manager = manager
        self.user_data = user_data
        self.limits = []
    def refresh(self):

        for x in self.user_data:
            if x["username"] == self.manager.user and self.manager.password == x["password"]:
                tk.Button(self, text="go back", command=lambda: self.manager.show_screen("budgeting_and_saveings")).pack()
                thing =utill_functions.csv_file.from_underscore(x["savings_over_time"])
                if thing==[""]:
                    messagebox.showinfo("invalid choise","you do not have any savings history")
                else:
                    for num,y in enumerate(thing):
                        tk.Label(self,text=f"item {num}:{y}")
#this is just for reference

def create_budget_plan(data,spendings,gooy):
    choice=input("Do you want to make a budget plan? (y/n): ").lower

    # get user's incomepass    income=gooy.get_valid_type(float,"Enter how much money you have right now: ")
    if choice=="y":
    # get all category limits
        income=gooy.get_valid_type(float,"How much money do you have?")

        budget_plan=gooy.get_valid_type(float,"Enter how much money do you want to save: ")
    # calculate total planned spending
        budget=budget_plan - income
    # calculate remaining money:
        remaining=income - spendings
        # remaining=income - total planned spending

    # display:
        messagebox.showinfo(f"Your income is ${income}\nspendings is ${spendings}\nmoney left after budgeting: ${remaining}")
        # "Your income is $___"
        # "Your total planned spending is $___"
        # "Money left after budgeting: $___"
        
    elif choice =="n":
        return 
    
 


# define function as compare_expenses_to_budget()
def compare_expenses_to_budget(data,gooy):
    with open("data.csv","r+") as data:
        # for each category:
        for spending in data:    
            # compare actual spending vs budget limit
            spending=0
            limit=0
            # if spending > limit:
            if spending > limit:
            # display warning:
                messagebox.showinfo("WARNING")
                # "You went over budget in [category]"                
                messagebox.showinfo("You are over budget in {}")

            #else:
            else:
                #display:
                    #"You are within budget for [category]"
                messagebox.showinfo("fYou are within the budget category")

    # calculate total remaining money:
        # income - total expenses


    # display:
        # "You have $___ left this month"


# SAVINGS GOAL SECTION


# define function as savings_goal_tracker()

def savings_goals_tracker(data,gooy):
    # ask user:
            # "What is your savings goal amount?"
    goal=gooy.get_valid_type(float,"What is your savings goal amount?: ")
    # ask user:
            # "What is your income?"
    income=gooy.get_valid_type(float,"What is your monthly income?: ")
    # ask user:
            # "What percentage of your income goes to savings?"
    percentage_to_savings=gooy.get_valid_type(float,"What percentage of your income goes to savings?: ",valid=(0,100))
# convert percent to decimal
    goal_progress=gooy.get_valid_type(float,"How close are you to your savings goal? (enter amount of money in savings currently): ")
    # calculate monthly savings:
            # savings=income * percent
    convert_percent_to_decimal=percentage_to_savings / 100
# ask user:
            # "What is your current savings amount?"
    savings_per_month=income * convert_percent_to_decimal
        # calculate progress:
            # progress=current savings / goal * 100


        # display:
            # "You save $___ per month"
            # "You are ___% towards your goal"
    goal_time=goal / savings_per_month
    goal_time_rounded=round(goal_time,0)




        # INTEREST CALCULATION (concerning SAVINGS)

def interest_calculation(data,savings,gooy):
        # ask user:
        interest_rate=0
        interest_rate=gooy.get_valid_type(float,"Optional, what is your interest rate?\nenter 0 to skip: ")
            # "Enter interest rate (optional,press enter to skip)"

        # if user enters rate:
            # convert rate to decimal
        if interest_rate != 0:
            # calculate interest:
            interest_amount=savings_goals_tracker(data,gooy) * interest_rate
                # interest_amount=current savings * rate
    
            # add interest to savings
            savings +=interest_amount
            # display:crea
            messagebox.showinfo(f"With interest,your savings is now {savings}")
                # "With interest,your savings is now $___"
        elif interest_rate == "0":
            return


        # FUTURE PROJECTION


        # calculate months needed:
            # months=(goal - current savings) / monthly savings

        # display:
            # "You will reach your goal in ___ months"

        # if goal reached:
            # display:
                # "Congrats! You reached your savings goal!"

        # ask user:
            # "Press enter to continue or type exit to go back"

        # if user types exit:
            # break loop
            
def BG_main(username,password,data,gooy):
    messagebox.showinfo("Welcome to the Budgeting/Savings Goal sector.")

    choice=gooy.get_valid_type(int,"0 Go back to main menu\n1 to set budget limits\n2 to Compare expenses to budget\n3 to Savings goal tracker\nWhat do you want: ",valid=(0,3))
    if choice=="0": 
        return
    elif choice=="1":
        create_budget_plan(data,gooy)
    elif choice=="2":
        compare_expenses_to_budget(data,gooy)
    elif choice=="3":
        savings_goals_tracker(data,gooy)




















        