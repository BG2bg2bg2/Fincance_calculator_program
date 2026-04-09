# GNB - Gov Stuff (Budgeting + Savings Goal Tracker)

# End up here from Edwing's menu if user selects budgeting/savings options

# Before user gets here:
# - Categories already exist (Rent, Food, Transportation, etc.)
# - Income/expenses may already be stored by Edwing/Liam
import utill_functions


# Ask user:
# 1. Set budget limits
# 2. View budgeting plan
# 3. Compare expenses to budget
# 4. Savings goal tracker
# 5. Go back to main menu


# BUDGETING SECTION


# define function as set_budget_limits()
def set_budget_limits():
    # ask user for total monthly income
    income = utill_functions.get_valid_type(float, "What is your monthly income?: $")
    # for each category:
        # ask user to set a spending limit
    spending_limit = utill_functions.get_valid_type(float, "What is your spending limit?: $")
    # store budget limits (will be saved by Liam's data system)

    # display:
        # "Budget limits successfully set"

# If 2 is the option, then all this: 

# define function as create_budget_plan()
def add_budget_categories(data):
#make thing so user just keeps listing categories till they say some -- sike, I changed my mind
    budget_categories = []
    budget_category_maxes = []
    category_amount = utill_functions.get_valid_type(int, "How many budgeting categories will you have? (Enter number): ", invalid_prompt = 0)
    for i in range(category_amount):
            category_names = input(f"Name each of your {category_amount} categories {i + 1}: ")
            budget_categories.append(category_names)

    for category in budget_categories: 
            max = utill_functions.get_valid_type(int, f"Here are your categories: {budget_categories} \nWhat is the max amount of money you'll spend on each category? (enter one category's amount then enter, and continue until all categories are satisfied): ", invalid_prompt = 0)
            budget_category_maxes.append(max)
            
def create_budget_plan(data,spendings):
    choice = input("Do you want to make a budget plan? (y/n): ").lower

    # get user's incomepass    income = utill_functions.get_valid_type(float,"Enter how much money you have right now: ")
    if choice == "y":
    # get all category limits
        income = utill_functions.get_valid_type(float, "How much money do you have?")

        budget_plan = utill_functions.get_valid_type(float,"Enter how much money do you want to save: ")
    # calculate total planned spending
        budget = budget_plan - income
    # calculate remaining money:
        remaining = income - spendings
        # remaining = income - total planned spending

    # display:
        print(f"Your income is ${income}\nspendings is ${spendings}\nmoney left after budgeting: ${remaining}")
        # "Your income is $___"
        # "Your total planned spending is $___"
        # "Money left after budgeting: $___"


# define function as compare_expenses_to_budget()
def compare_expenses_to_budget(data):
    with open("data.csv", "r+") as data:
        # for each category:
        for spending in data:    
            # compare actual spending vs budget limit
            spending = 0
            limit = 0
            # if spending > limit:
            if spending > limit:
            # display warning:
                print("WARNING")
                # "You went over budget in [category]"                
                print("You are over budget in {}")

            #else:
            else:
                #display:
                    #"You are within budget for [category]"
                print("fYou are within the budget category")

    # calculate total remaining money:
        # income - total expenses


    # display:
        # "You have $___ left this month"


# SAVINGS GOAL SECTION


# define function as savings_goal_tracker()

def savings_goals_tracker(data):
    # ask user:
            # "What is your savings goal amount?"
    goal = utill_functions.get_valid_type(float, "What is your savings goal amount?: ")
    # ask user:
            # "What is your income?"
    income = utill_functions.get_valid_type(float, "What is your monthly income?: ")
    # ask user:
            # "What percentage of your income goes to savings?"
    percentage_to_savings = utill_functions.get_valid_type(float, "What percentage of your income goes to savings?: ", valid = (0, 100))
# convert percent to decimal
    goal_progress = utill_functions.get_valid_type(float, "How close are you to your savings goal? (enter amount of money in savings currently): ")
    # calculate monthly savings:
            # savings = income * percent
    convert_percent_to_decimal = percentage_to_savings / 100
# ask user:
            # "What is your current savings amount?"
    savings_per_month = income * convert_percent_to_decimal
        # calculate progress:
            # progress = current savings / goal * 100


        # display:
            # "You save $___ per month"
            # "You are ___% towards your goal"
    goal_time = goal / savings_per_month
    goal_time_rounded = round(goal_time, 0)




        # INTEREST CALCULATION (concerning savings)

def intrest_calculation(data, savings):
        # ask user:
        intrest_rate = 0
        intrest_rate = utill_functions.get_valid_type(float,"Optional, what is your interest rate?\npress enter to skip: ")
            # "Enter interest rate (optional, press enter to skip)"

        # if user enters rate:
            # convert rate to decimal
        if intrest_rate != 0:
            # calculate interest:
            intrest_amount = savings_goals_tracker * intrest_rate
                # interest_amount = current savings * rate
    
            # add interest to savings
            savings += intrest_amount
            # display:crea
            print(f"With intrest, your savings is now {savings}")
                # "With interest, your savings is now $___"


        # FUTURE PROJECTION


        # calculate months needed:
            # months = (goal - current savings) / monthly savings

        # display:
            # "You will reach your goal in ___ months"

        # if goal reached:
            # display:
                # "Congrats! You reached your savings goal!"

        # ask user:
            # "Press enter to continue or type exit to go back"

        # if user types exit:
            # break loop
            
def BG_main(username, password,data):
    print("Welcome to the Budgeting/Savings Goal sector.")

    choice = utill_functions.get_valid_type(int,"0 Go back to main men\n1 to set budget limits\n2 to Compare expenses to budget\n3 to Savings goal tracker\nWhat do you want: ",valid=(0,4))
    if choice == "0": 
        return
    elif choice == "1":
        create_budget_plan()
    elif choice == "2":
        compare_expenses_to_budget(data)
    elif choice == "3":
        savings_goals_tracker()
    else:
        print("Must enter a valid choice")